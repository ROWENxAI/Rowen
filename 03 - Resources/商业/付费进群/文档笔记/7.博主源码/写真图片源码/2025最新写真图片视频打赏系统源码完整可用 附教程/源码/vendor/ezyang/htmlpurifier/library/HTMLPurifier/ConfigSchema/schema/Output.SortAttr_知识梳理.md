---
title: "Output.SortAttr.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Output.SortAttr.txt"
---

# Output.SortAttr.txt 知识梳理

> 来源: `Output.SortAttr.txt` | 字数: 509

## 内容全文

Output.SortAttr

TYPE: bool

VERSION: 3.2.0

DEFAULT: false

--DESCRIPTION--

<p>

If true, HTML Purifier will sort attributes by name before writing them back

to the document, converting a tag like: <code>&lt;el b="" a="" c="" /&gt;</code>

to <code>&lt;el a="" b="" c="" /&gt;</code>. This is a workaround for

a bug in FCKeditor which causes it to swap attributes order, adding noise

to text diffs. If you're not seeing this bug, chances are, you don't need

this directive.

</p>

--# vim: et sw=4 sts=4

