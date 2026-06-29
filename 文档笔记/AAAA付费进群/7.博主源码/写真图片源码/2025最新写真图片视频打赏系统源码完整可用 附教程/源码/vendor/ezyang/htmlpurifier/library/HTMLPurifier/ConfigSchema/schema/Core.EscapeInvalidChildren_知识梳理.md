---
title: "Core.EscapeInvalidChildren.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.EscapeInvalidChildren.txt"
---

# Core.EscapeInvalidChildren.txt 知识梳理

> 来源: `Core.EscapeInvalidChildren.txt` | 字数: 503

## 内容全文

Core.EscapeInvalidChildren

TYPE: bool

DEFAULT: false

--DESCRIPTION--

<p><strong>Warning:</strong> this configuration option is no longer does anything as of 4.6.0.</p>

<p>When true, a child is found that is not allowed in the context of the

parent element will be transformed into text as if it were ASCII. When

false, that element and all internal tags will be dropped, though text will

be preserved.  There is no option for dropping the element but preserving

child nodes.</p>

--# vim: et sw=4 sts=4

