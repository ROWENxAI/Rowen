---
title: "URI.Base.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.Base.txt"
---

# URI.Base.txt 知识梳理

> 来源: `URI.Base.txt` | 字数: 654

## 内容全文

URI.Base

TYPE: string/null

VERSION: 2.1.0

DEFAULT: NULL

--DESCRIPTION--

<p>

The base URI is the URI of the document this purified HTML will be

inserted into.  This information is important if HTML Purifier needs

to calculate absolute URIs from relative URIs, such as when %URI.MakeAbsolute

is on.  You may use a non-absolute URI for this value, but behavior

may vary (%URI.MakeAbsolute deals nicely with both absolute and

relative paths, but forwards-compatibility is not guaranteed).

<strong>Warning:</strong> If set, the scheme on this URI

overrides the one specified by %URI.DefaultScheme.

</p>

--# vim: et sw=4 sts=4

