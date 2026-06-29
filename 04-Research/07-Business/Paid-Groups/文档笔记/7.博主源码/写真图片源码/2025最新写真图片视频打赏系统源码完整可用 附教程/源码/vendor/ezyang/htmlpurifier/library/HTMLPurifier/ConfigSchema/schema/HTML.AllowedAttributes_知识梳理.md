---
title: "HTML.AllowedAttributes.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.AllowedAttributes.txt"
---

# HTML.AllowedAttributes.txt 知识梳理

> 来源: `HTML.AllowedAttributes.txt` | 字数: 607

## 内容全文

HTML.AllowedAttributes

TYPE: lookup/null

VERSION: 1.3.0

DEFAULT: NULL

--DESCRIPTION--

<p>

If HTML Purifier's attribute set is unsatisfactory, overload it!

The syntax is "tag.attr" or "*.attr" for the global attributes

(style, id, class, dir, lang, xml:lang).

</p>

<p>

<strong>Warning:</strong> If another directive conflicts with the

elements here, <em>that</em> directive will win and override. For

example, %HTML.EnableAttrID will take precedence over *.id in this

directive.  You must set that directive to true before you can use

IDs at all.

</p>

--# vim: et sw=4 sts=4

