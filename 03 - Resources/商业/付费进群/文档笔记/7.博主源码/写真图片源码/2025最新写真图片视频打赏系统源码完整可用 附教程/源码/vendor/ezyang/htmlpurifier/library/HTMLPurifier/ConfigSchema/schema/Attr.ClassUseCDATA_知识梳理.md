---
title: "Attr.ClassUseCDATA.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Attr.ClassUseCDATA.txt"
---

# Attr.ClassUseCDATA.txt 知识梳理

> 来源: `Attr.ClassUseCDATA.txt` | 字数: 926

## 内容全文

Attr.ClassUseCDATA

TYPE: bool/null

DEFAULT: null

VERSION: 4.0.0

--DESCRIPTION--

If null, class will auto-detect the doctype and, if matching XHTML 1.1 or

XHTML 2.0, will use the restrictive NMTOKENS specification of class. Otherwise,

it will use a relaxed CDATA definition.  If true, the relaxed CDATA definition

is forced; if false, the NMTOKENS definition is forced.  To get behavior

of HTML Purifier prior to 4.0.0, set this directive to false.

Some rational behind the auto-detection:

in previous versions of HTML Purifier, it was assumed that the form of

class was NMTOKENS, as specified by the XHTML Modularization (representing

XHTML 1.1 and XHTML 2.0).  The DTDs for HTML 4.01 and XHTML 1.0, however

specify class as CDATA.  HTML 5 effectively defines it as CDATA, but

with the additional constraint that each name should be unique (this is not

explicitly outlined in previous specifications).

--# vim: et sw=4 sts=4

