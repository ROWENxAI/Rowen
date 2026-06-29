---
title: "Attr.IDBlacklistRegexp.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Attr.IDBlacklistRegexp.txt"
---

# Attr.IDBlacklistRegexp.txt 知识梳理

> 来源: `Attr.IDBlacklistRegexp.txt` | 字数: 317

## 内容全文

Attr.IDBlacklistRegexp

TYPE: string/null

VERSION: 1.6.0

DEFAULT: NULL

--DESCRIPTION--

PCRE regular expression to be matched against all IDs. If the expression is

matches, the ID is rejected. Use this with care: may cause significant

degradation. ID matching is done after all other validation.

--# vim: et sw=4 sts=4

