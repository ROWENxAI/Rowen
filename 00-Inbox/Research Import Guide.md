# Research Import Guide

> ""如何将外部资料正确导入知识库""

## 导入流程

1. **收集** - 使用 Web Clipper / MarkDownload / 手动复制，保存到 `00-Inbox/Downloaded/`
2. **清洗** - 运行 Research Cleaner 处理后移至 `00-Inbox/Cleaned/`
3. **归类** - 根据内容主题移至 `04-Research/` 对应目录
4. **链接** - 添加内部链接和标签
5. **入库** - 确认无误后删除 `00-Inbox/` 中原始文件

## 导入规范

- 保留原文，禁止删减
- 提取来源 URL 和作者
- 添加标签 `source/xxx`
- 添加 Topic Hub 引用
- 保持 Markdown 格式整洁

## 快速模板

```markdown
---
title: ""
source: ""
author: ""
date: ""
tags: [source/web, status/unprocessed]
---

# 标题

> 摘要

## 正文

## 来源
- URL:
- Author:
- Published:
```
