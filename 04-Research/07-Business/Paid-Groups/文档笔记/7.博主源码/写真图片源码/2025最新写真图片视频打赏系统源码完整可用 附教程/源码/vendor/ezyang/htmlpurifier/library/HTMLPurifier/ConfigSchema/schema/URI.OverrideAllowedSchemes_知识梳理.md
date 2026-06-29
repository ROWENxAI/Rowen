---
title: "URI.OverrideAllowedSchemes.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.OverrideAllowedSchemes.txt"
---

# URI.OverrideAllowedSchemes.txt 知识梳理

> 来源: `URI.OverrideAllowedSchemes.txt` | 字数: 326

## 内容全文

URI.OverrideAllowedSchemes

TYPE: bool

DEFAULT: true

--DESCRIPTION--

If this is set to true (which it is by default), you can override

%URI.AllowedSchemes by simply registering a HTMLPurifier_URIScheme to the

registry.  If false, you will also have to update that directive in order

to add more schemes.

--# vim: et sw=4 sts=4

