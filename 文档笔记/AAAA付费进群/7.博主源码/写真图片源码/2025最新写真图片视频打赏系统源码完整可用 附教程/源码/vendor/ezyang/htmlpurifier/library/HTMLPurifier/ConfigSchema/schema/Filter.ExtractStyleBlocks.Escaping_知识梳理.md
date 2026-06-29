---
title: "Filter.ExtractStyleBlocks.Escaping.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Filter.ExtractStyleBlocks.Escaping.txt"
---

# Filter.ExtractStyleBlocks.Escaping.txt 知识梳理

> 来源: `Filter.ExtractStyleBlocks.Escaping.txt` | 字数: 485

## 内容全文

Filter.ExtractStyleBlocks.Escaping

TYPE: bool

VERSION: 3.0.0

DEFAULT: true

ALIASES: Filter.ExtractStyleBlocksEscaping, FilterParam.ExtractStyleBlocksEscaping

--DESCRIPTION--

<p>

Whether or not to escape the dangerous characters &lt;, &gt; and &amp;

as \3C, \3E and \26, respectively. This is can be safely set to false

if the contents of StyleBlocks will be placed in an external stylesheet,

where there is no risk of it being interpreted as HTML.

</p>

--# vim: et sw=4 sts=4

