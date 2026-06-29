---
title: "HTML.ForbiddenElements.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.ForbiddenElements.txt"
---

# HTML.ForbiddenElements.txt 知识梳理

> 来源: `HTML.ForbiddenElements.txt` | 字数: 754

## 内容全文

HTML.ForbiddenElements

TYPE: lookup

VERSION: 3.1.0

DEFAULT: array()

--DESCRIPTION--

<p>

This was, perhaps, the most requested feature ever in HTML

Purifier. Please don't abuse it! This is the logical inverse of

%HTML.AllowedElements, and it will override that directive, or any

other directive.

</p>

<p>

If possible, %HTML.Allowed is recommended over this directive, because it

can sometimes be difficult to tell whether or not you've forbidden all of

the behavior you would like to disallow. If you forbid <code>img</code>

with the expectation of preventing images on your site, you'll be in for

a nasty surprise when people start using the <code>background-image</code>

CSS property.

</p>

--# vim: et sw=4 sts=4

