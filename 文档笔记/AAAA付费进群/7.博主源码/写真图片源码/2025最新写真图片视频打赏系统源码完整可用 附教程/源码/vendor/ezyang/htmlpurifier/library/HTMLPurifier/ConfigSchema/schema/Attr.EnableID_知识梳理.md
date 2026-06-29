---
title: "Attr.EnableID.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Attr.EnableID.txt"
---

# Attr.EnableID.txt 知识梳理

> 来源: `Attr.EnableID.txt` | 字数: 645

## 内容全文

Attr.EnableID

TYPE: bool

DEFAULT: false

VERSION: 1.2.0

--DESCRIPTION--

Allows the ID attribute in HTML.  This is disabled by default due to the

fact that without proper configuration user input can easily break the

validation of a webpage by specifying an ID that is already on the

surrounding HTML.  If you don't mind throwing caution to the wind, enable

this directive, but I strongly recommend you also consider blacklisting IDs

you use (%Attr.IDBlacklist) or prefixing all user supplied IDs

(%Attr.IDPrefix).  When set to true HTML Purifier reverts to the behavior of

pre-1.2.0 versions.

--ALIASES--

HTML.EnableAttrID

--# vim: et sw=4 sts=4

