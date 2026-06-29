"""重新处理 X 平台数据 -> Obsidian 格式"""
import os, sys, json
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

OUTPUT = r"H:\转录\X平台知识库"
RAW_DIR = r"D:\转录\X平台知识库"
os.makedirs(OUTPUT, exist_ok=True)

def safe_fn(name):
    for ch in ['<','>',':','"','/','\\','|','?','*']:
        name = name.replace(ch, '_')
    return name[:150]

def load_json(fn):
    fp = os.path.join(RAW_DIR, fn)
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Load raw data
likes = load_json("likes_raw.json")
posts = load_json("posts_raw.json")
replies = load_json("replies_raw.json")
media = load_json("media_raw.json")

print(f"Loaded: likes={len(likes)}, posts={len(posts)}, replies={len(replies)}, media={len(media)}")

# Dedup
all_tweets = {}
for src, tweets in [("like", likes), ("post", posts), ("reply", replies), ("media", media)]:
    for t in tweets:
        tid = t.get("id", "") or str(hash(t.get("text","")[:100]))
        if tid not in all_tweets:
            t["source"] = src
            all_tweets[tid] = t
        else:
            if all_tweets[tid]["source"] == "like" and src != "like":
                all_tweets[tid]["source"] = src

unique = list(all_tweets.values())
print(f"Unique tweets: {len(unique)}")

# Classify
TOPICS = {
    "AI技术": ["ai","gpt","llm","openai","claude","gemini","model","transformer","neural","deep learning","machine learning","人工智能","大模型","训练","推理","inference","training","fine-tune","rag","embedding","vector","agent","multi-modal","多模态","diffusion","stable diffusion","midjourney","chatgpt","copilot","cursor","anthropic","deepseek","qwen","通义","prompt","token","context window","benchmark","agi","alignment","rlhf","lora","qlora","moe","attention","bpe","tokenizer","api","sdk","huggingface","pytorch","tensorflow"],
    "提示词工程": ["prompt engineering","prompt","提示词","system prompt","few-shot","chain of thought","cot","zero-shot","in-context learning","jailbreak","越狱","提示工程"],
    "创业商业": ["startup","founder","融资","vc","投资","估值","revenue","arr","saas","商业模式","business","创业","产品","product","growth","增长","用户","market","市场","竞争","盈利","变现","monetize","b2b","b2c","mvp","pmf"],
    "工具资源": ["tool","github","open source","开源","框架","library","plugin","extension","chrome extension","vscode","notion","obsidian","figma","资源","推荐","app","软件","效率","workflow","自动化","automation","script"],
    "编程技术": ["code","coding","programming","developer","engineer","python","javascript","typescript","rust","go","api","backend","frontend","fullstack","devops","docker","kubernetes","database","sql","nosql","git","linux","部署","服务器","cloud","aws","azure","编程","开发","架构","microservice"],
    "行业资讯": ["apple","google","microsoft","meta","amazon","nvidia","tesla","bytedance","字节","腾讯","阿里","百度","华为","小米","三星","samsung","发布","launch","release","acquisition","收购","裁员","layoff","ipo","上市"],
    "认知思维": ["思考","思维","认知","学习","成长","方法论","框架","心智模型","mental model","决策","decision","strategy","策略","哲学","philosophy","第一性原理","first principles","复利","compound","长期主义","概率","probability"],
    "Web3区块链": ["web3","crypto","bitcoin","btc","ethereum","eth","blockchain","链","defi","nft","dao","token","代币","钱包","wallet","交易所","dex","智能合约","smart contract","solana","polygon","layer2","l2","zk","零知识证明"],
    "内容创作": ["内容","创作","视频","公众号","自媒体","抖音","bilibili","b站","youtube","twitter","x.com","写文章","写作","writing","content","creator","创作者","粉丝","流量","运营","直播","播客","podcast"],
}

def classify(text):
    tl = text.lower()
    scores = {}
    for topic, kws in TOPICS.items():
        s = sum(1 for kw in kws if kw.lower() in tl)
        if s > 0:
            scores[topic] = s
    return max(scores, key=scores.get) if scores else "其他"

for t in unique:
    t["topic"] = classify(t.get("text",""))

from collections import defaultdict
by_topic = defaultdict(list)
for t in unique:
    by_topic[t["topic"]].append(t)

sorted_topics = sorted(by_topic.items(), key=lambda x: -len(x[1]))

now = datetime.now().strftime('%Y-%m-%d')

# Write per-topic files with Obsidian format
for topic, tweets in sorted_topics:
    sorted_t = sorted(tweets, key=lambda t: t.get("favorite_count",0)+t.get("retweet_count",0), reverse=True)
    fn = safe_fn(f"分类_{topic}") + ".md"
    fp = os.path.join(OUTPUT, fn)

    md = f"---\ntitle: \"{topic}\"\ntype: x-topic\ncount: {len(tweets)}\ndate: {now}\ntags: [X平台, {topic}]\n---\n\n"
    md += f"# {topic}\n\n"
    md += f"> 共 {len(tweets)} 条内容 | 抓取时间: {now}\n\n"
    md += "## 核心内容\n\n"

    for i, t in enumerate(sorted_t, 1):
        text = t.get("text","").strip()
        author = t.get("author","")
        handle = t.get("handle","")
        url = t.get("url","")
        time_str = t.get("created_at","")
        likes = t.get("favorite_count",0)
        rts = t.get("retweet_count",0)
        src = t.get("source","")
        media_urls = t.get("media",[])
        link_urls = t.get("urls",[])

        md += f"### {i}. {text[:60]}{'...' if len(text)>60 else ''}\n\n"
        md += f"- **作者**: @{author} ({handle})\n"
        md += f"- **时间**: {time_str}\n"
        md += f"- **来源**: {src} | ❤️ {likes} | 🔄 {rts}\n"
        if url:
            md += f"- **链接**: [{url}]({url})\n"
        md += f"\n{text}\n\n"
        if media_urls:
            md += f"![]({media_urls[0]})\n\n"
        if link_urls:
            for lu in link_urls:
                md += f"- [{lu}]({lu})\n"
            md += "\n"
        md += "---\n\n"

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"  {topic}: {len(tweets)} tweets -> {fn}")

# TOP50
all_sorted = sorted(unique, key=lambda t: t.get("favorite_count",0)+t.get("retweet_count",0)*2, reverse=True)
top50 = all_sorted[:50]
md50 = f"---\ntitle: \"高价值收藏TOP50\"\ntype: x-top50\ndate: {now}\ntags: [X平台, 精选]\n---\n\n"
md50 += "# 高价值收藏 TOP50\n\n"
md50 += f"> 按互动量排序 | 抓取时间: {now}\n\n"
for i, t in enumerate(top50, 1):
    text = t.get("text","").strip()
    author = t.get("author","")
    url = t.get("url","")
    likes = t.get("favorite_count",0)
    rts = t.get("retweet_count",0)
    topic = t.get("topic","")
    md50 += f"## {i}. [{topic}] {text[:80]}\n\n"
    md50 += f"- @{author} | ❤️ {likes} | 🔄 {rts}\n"
    if url:
        md50 += f"- 链接: [{url}]({url})\n"
    md50 += f"\n{text}\n\n---\n\n"

with open(os.path.join(OUTPUT, "高价值收藏TOP50.md"), 'w', encoding='utf-8') as f:
    f.write(md50)

# Main index
index = f"---\ntitle: \"X平台知识库总目录\"\ntype: x-moc\ndate: {now}\ntags: [X平台, MOC]\n---\n\n"
index += "# X平台知识库总目录\n\n"
index += f"- 账号: @0xR0wen\n"
index += f"- 抓取时间: {now}\n"
index += f"- 总计: {len(unique)} 条去重内容\n\n"
index += "## 分类导航\n\n"
for topic, tweets in sorted_topics:
    fn = safe_fn(f"分类_{topic}") + ".md"
    index += f"- [[{fn}|{topic}]] ({len(tweets)} 条)\n"
index += f"\n- [[高价值收藏TOP50.md|高价值收藏TOP50]]\n"

with open(os.path.join(OUTPUT, "X平台个人知识库总目录.md"), 'w', encoding='utf-8') as f:
    f.write(index)

print(f"\nDone! {len(unique)} tweets, {len(sorted_topics)} topics")
