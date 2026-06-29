---
title: "CSS.AllowedProperties.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\CSS.AllowedProperties.txt"
---

# CSS.AllowedProperties.txt 知识梳理

> 来源: `CSS.AllowedProperties.txt` | 字数: 608

## 内容全文

CSS.AllowedProperties

TYPE: lookup/null

VERSION: 3.1.0

DEFAULT: NULL

--DESCRIPTION--

<p>

If HTML Purifier's style attributes set is unsatisfactory for your needs,

you can overload it with your own list of tags to allow.  Note that this

method is subtractive: it does its job by taking away from HTML Purifier

usual feature set, so you cannot add an attribute that HTML Purifier never

supported in the first place.

</p>

<p>

<strong>Warning:</strong> If another directive conflicts with the

elements here, <em>that</em> directive will win and override.

</p>

--# vim: et sw=4 sts=4

