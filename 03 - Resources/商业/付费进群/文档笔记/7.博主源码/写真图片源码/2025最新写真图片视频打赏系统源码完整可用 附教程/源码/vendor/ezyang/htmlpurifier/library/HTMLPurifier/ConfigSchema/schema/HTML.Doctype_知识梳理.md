---
title: "HTML.Doctype.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.Doctype.txt"
---

# HTML.Doctype.txt 知识梳理

> 来源: `HTML.Doctype.txt` | 字数: 473

## 内容全文

HTML.Doctype

TYPE: string/null

DEFAULT: NULL

--DESCRIPTION--

Doctype to use during filtering. Technically speaking this is not actually

a doctype (as it does not identify a corresponding DTD), but we are using

this name for sake of simplicity. When non-blank, this will override any

older directives like %HTML.XHTML or %HTML.Strict.

--ALLOWED--

'HTML 4.01 Transitional', 'HTML 4.01 Strict', 'XHTML 1.0 Transitional', 'XHTML 1.0 Strict', 'XHTML 1.1'

--# vim: et sw=4 sts=4

