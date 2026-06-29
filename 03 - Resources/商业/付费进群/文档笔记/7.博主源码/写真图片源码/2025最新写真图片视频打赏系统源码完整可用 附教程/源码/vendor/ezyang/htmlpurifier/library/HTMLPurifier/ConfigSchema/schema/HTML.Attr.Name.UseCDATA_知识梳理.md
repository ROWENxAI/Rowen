---
title: "HTML.Attr.Name.UseCDATA.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.Attr.Name.UseCDATA.txt"
---

# HTML.Attr.Name.UseCDATA.txt 知识梳理

> 来源: `HTML.Attr.Name.UseCDATA.txt` | 字数: 471

## 内容全文

HTML.Attr.Name.UseCDATA

TYPE: bool

DEFAULT: false

VERSION: 4.0.0

--DESCRIPTION--

The W3C specification DTD defines the name attribute to be CDATA, not ID, due

to limitations of DTD.  In certain documents, this relaxed behavior is desired,

whether it is to specify duplicate names, or to specify names that would be

illegal IDs (for example, names that begin with a digit.) Set this configuration

directive to true to use the relaxed parsing rules.

--# vim: et sw=4 sts=4

