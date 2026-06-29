---
title: "Core.AllowHostnameUnderscore.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.AllowHostnameUnderscore.txt"
---

# Core.AllowHostnameUnderscore.txt 知识梳理

> 来源: `Core.AllowHostnameUnderscore.txt` | 字数: 575

## 内容全文

Core.AllowHostnameUnderscore

TYPE: bool

VERSION: 4.6.0

DEFAULT: false

--DESCRIPTION--

<p>

By RFC 1123, underscores are not permitted in host names.

(This is in contrast to the specification for DNS, RFC

2181, which allows underscores.)

However, most browsers do the right thing when faced with

an underscore in the host name, and so some poorly written

websites are written with the expectation this should work.

Setting this parameter to true relaxes our allowed character

check so that underscores are permitted.

</p>

--# vim: et sw=4 sts=4

