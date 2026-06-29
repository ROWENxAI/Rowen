---
title: "HTML.DefinitionRev.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.DefinitionRev.txt"
---

# HTML.DefinitionRev.txt 知识梳理

> 来源: `HTML.DefinitionRev.txt` | 字数: 533

## 内容全文

HTML.DefinitionRev

TYPE: int

VERSION: 2.0.0

DEFAULT: 1

--DESCRIPTION--

<p>

Revision identifier for your custom definition specified in

%HTML.DefinitionID.  This serves the same purpose: uniquely identifying

your custom definition, but this one does so in a chronological

context: revision 3 is more up-to-date then revision 2.  Thus, when

this gets incremented, the cache handling is smart enough to clean

up any older revisions of your definition as well as flush the

cache.

</p>

--# vim: et sw=4 sts=4

