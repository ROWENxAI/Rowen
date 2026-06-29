---
title: "HTML.CoreModules.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.CoreModules.txt"
---

# HTML.CoreModules.txt 知识梳理

> 来源: `HTML.CoreModules.txt` | 字数: 622

## 内容全文

HTML.CoreModules

TYPE: lookup

VERSION: 2.0.0

--DEFAULT--

array (

'Structure' => true,

'Text' => true,

'Hypertext' => true,

'List' => true,

'NonXMLCommonAttributes' => true,

'XMLCommonAttributes' => true,

'CommonAttributes' => true,

)

--DESCRIPTION--

<p>

Certain modularized doctypes (XHTML, namely), have certain modules

that must be included for the doctype to be an conforming document

type: put those modules here. By default, XHTML's core modules

are used. You can set this to a blank array to disable core module

protection, but this is not recommended.

</p>

--# vim: et sw=4 sts=4

