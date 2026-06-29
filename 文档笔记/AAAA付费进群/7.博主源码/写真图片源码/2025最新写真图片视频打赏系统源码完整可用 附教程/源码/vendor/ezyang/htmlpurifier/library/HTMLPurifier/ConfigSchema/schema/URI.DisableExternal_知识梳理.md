---
title: "URI.DisableExternal.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.DisableExternal.txt"
---

# URI.DisableExternal.txt 知识梳理

> 来源: `URI.DisableExternal.txt` | 字数: 443

## 内容全文

URI.DisableExternal

TYPE: bool

VERSION: 1.2.0

DEFAULT: false

--DESCRIPTION--

Disables links to external websites.  This is a highly effective anti-spam

and anti-pagerank-leech measure, but comes at a hefty price: nolinks or

images outside of your domain will be allowed.  Non-linkified URIs will

still be preserved.  If you want to be able to link to subdomains or use

absolute URIs, specify %URI.Host for your website.

--# vim: et sw=4 sts=4

