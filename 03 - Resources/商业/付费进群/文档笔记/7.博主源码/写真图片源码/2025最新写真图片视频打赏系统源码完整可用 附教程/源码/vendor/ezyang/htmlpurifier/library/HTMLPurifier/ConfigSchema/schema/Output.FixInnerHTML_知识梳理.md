---
title: "Output.FixInnerHTML.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Output.FixInnerHTML.txt"
---

# Output.FixInnerHTML.txt 知识梳理

> 来源: `Output.FixInnerHTML.txt` | 字数: 543

## 内容全文

Output.FixInnerHTML

TYPE: bool

VERSION: 4.3.0

DEFAULT: true

--DESCRIPTION--

<p>

If true, HTML Purifier will protect against Internet Explorer's

mishandling of the <code>innerHTML</code> attribute by appending

a space to any attribute that does not contain angled brackets, spaces

or quotes, but contains a backtick.  This slightly changes the

semantics of any given attribute, so if this is unacceptable and

you do not use <code>innerHTML</code> on any of your pages, you can

turn this directive off.

</p>

--# vim: et sw=4 sts=4

