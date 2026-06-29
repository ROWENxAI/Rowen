---
title: "URI.MakeAbsolute.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.MakeAbsolute.txt"
---

# URI.MakeAbsolute.txt 知识梳理

> 来源: `URI.MakeAbsolute.txt` | 字数: 390

## 内容全文

URI.MakeAbsolute

TYPE: bool

VERSION: 2.1.0

DEFAULT: false

--DESCRIPTION--

<p>

Converts all URIs into absolute forms. This is useful when the HTML

being filtered assumes a specific base path, but will actually be

viewed in a different context (and setting an alternate base URI is

not possible). %URI.Base must be set for this directive to work.

</p>

--# vim: et sw=4 sts=4

