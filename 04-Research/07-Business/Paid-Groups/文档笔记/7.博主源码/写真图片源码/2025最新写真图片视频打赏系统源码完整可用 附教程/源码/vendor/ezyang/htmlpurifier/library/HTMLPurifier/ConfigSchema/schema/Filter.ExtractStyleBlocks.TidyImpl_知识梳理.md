---
title: "Filter.ExtractStyleBlocks.TidyImpl.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Filter.ExtractStyleBlocks.TidyImpl.txt"
---

# Filter.ExtractStyleBlocks.TidyImpl.txt 知识梳理

> 来源: `Filter.ExtractStyleBlocks.TidyImpl.txt` | 字数: 576

## 内容全文

Filter.ExtractStyleBlocks.TidyImpl

TYPE: mixed/null

VERSION: 3.1.0

DEFAULT: NULL

ALIASES: FilterParam.ExtractStyleBlocksTidyImpl

--DESCRIPTION--

<p>

If left NULL, HTML Purifier will attempt to instantiate a <code>csstidy</code>

class to use for internal cleaning. This will usually be good enough.

</p>

<p>

However, for trusted user input, you can set this to <code>false</code> to

disable cleaning. In addition, you can supply your own concrete implementation

of Tidy's interface to use, although I don't know why you'd want to do that.

</p>

--# vim: et sw=4 sts=4

