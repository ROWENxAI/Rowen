---
title: "HTML.AllowedElements.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.AllowedElements.txt"
---

# HTML.AllowedElements.txt 知识梳理

> 来源: `HTML.AllowedElements.txt` | 字数: 882

## 内容全文

HTML.AllowedElements

TYPE: lookup/null

VERSION: 1.3.0

DEFAULT: NULL

--DESCRIPTION--

<p>

If HTML Purifier's tag set is unsatisfactory for your needs, you can

overload it with your own list of tags to allow.  If you change

this, you probably also want to change %HTML.AllowedAttributes; see

also %HTML.Allowed which lets you set allowed elements and

attributes at the same time.

</p>

<p>

If you attempt to allow an element that HTML Purifier does not know

about, HTML Purifier will raise an error.  You will need to manually

tell HTML Purifier about this element by using the

<a href="http://htmlpurifier.org/docs/enduser-customize.html">advanced customization features.</a>

</p>

<p>

<strong>Warning:</strong> If another directive conflicts with the

elements here, <em>that</em> directive will win and override.

</p>

--# vim: et sw=4 sts=4

