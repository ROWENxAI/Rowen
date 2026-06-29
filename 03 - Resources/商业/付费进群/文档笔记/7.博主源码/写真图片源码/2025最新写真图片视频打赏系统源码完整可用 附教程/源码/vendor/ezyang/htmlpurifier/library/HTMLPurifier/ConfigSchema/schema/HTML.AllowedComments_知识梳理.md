---
title: "HTML.AllowedComments.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.AllowedComments.txt"
---

# HTML.AllowedComments.txt 知识梳理

> 来源: `HTML.AllowedComments.txt` | 字数: 367

## 内容全文

HTML.AllowedComments

TYPE: lookup

VERSION: 4.4.0

DEFAULT: array()

--DESCRIPTION--

A whitelist which indicates what explicit comment bodies should be

allowed, modulo leading and trailing whitespace.  See also %HTML.AllowedCommentsRegexp

(these directives are union'ed together, so a comment is considered

valid if any directive deems it valid.)

--# vim: et sw=4 sts=4

