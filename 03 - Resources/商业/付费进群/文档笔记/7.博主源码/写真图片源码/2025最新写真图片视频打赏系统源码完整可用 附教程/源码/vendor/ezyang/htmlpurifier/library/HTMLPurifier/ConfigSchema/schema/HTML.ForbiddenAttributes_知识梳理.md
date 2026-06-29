---
title: "HTML.ForbiddenAttributes.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.ForbiddenAttributes.txt"
---

# HTML.ForbiddenAttributes.txt 知识梳理

> 来源: `HTML.ForbiddenAttributes.txt` | 字数: 852

## 内容全文

HTML.ForbiddenAttributes

TYPE: lookup

VERSION: 3.1.0

DEFAULT: array()

--DESCRIPTION--

<p>

While this directive is similar to %HTML.AllowedAttributes, for

forwards-compatibility with XML, this attribute has a different syntax. Instead of

<code>tag.attr</code>, use <code>tag@attr</code>. To disallow <code>href</code>

attributes in <code>a</code> tags, set this directive to

<code>a@href</code>. You can also disallow an attribute globally with

<code>attr</code> or <code>*@attr</code> (either syntax is fine; the latter

is provided for consistency with %HTML.AllowedAttributes).

</p>

<p>

<strong>Warning:</strong> This directive complements %HTML.ForbiddenElements,

accordingly, check

out that directive for a discussion of why you

should think twice before using this directive.

</p>

--# vim: et sw=4 sts=4

