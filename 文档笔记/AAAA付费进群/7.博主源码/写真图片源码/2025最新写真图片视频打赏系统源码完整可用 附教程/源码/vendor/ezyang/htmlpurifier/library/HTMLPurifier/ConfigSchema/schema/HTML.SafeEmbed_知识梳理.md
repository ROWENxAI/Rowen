---
title: "HTML.SafeEmbed.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.SafeEmbed.txt"
---

# HTML.SafeEmbed.txt 知识梳理

> 来源: `HTML.SafeEmbed.txt` | 字数: 483

## 内容全文

HTML.SafeEmbed

TYPE: bool

VERSION: 3.1.1

DEFAULT: false

--DESCRIPTION--

<p>

Whether or not to permit embed tags in documents, with a number of extra

security features added to prevent script execution. This is similar to

what websites like MySpace do to embed tags. Embed is a proprietary

element and will cause your website to stop validating; you should

see if you can use %Output.FlashCompat with %HTML.SafeObject instead

first.</p>

--# vim: et sw=4 sts=4

