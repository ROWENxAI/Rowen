---
title: "Attr.IDPrefix.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Attr.IDPrefix.txt"
---

# Attr.IDPrefix.txt 知识梳理

> 来源: `Attr.IDPrefix.txt` | 字数: 475

## 内容全文

Attr.IDPrefix

TYPE: string

VERSION: 1.2.0

DEFAULT: ''

--DESCRIPTION--

String to prefix to IDs.  If you have no idea what IDs your pages may use,

you may opt to simply add a prefix to all user-submitted ID attributes so

that they are still usable, but will not conflict with core page IDs.

Example: setting the directive to 'user_' will result in a user submitted

'foo' to become 'user_foo'  Be sure to set %HTML.EnableAttrID to true

before using this.

--# vim: et sw=4 sts=4

