---
title: "HTML.SafeObject.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.SafeObject.txt"
---

# HTML.SafeObject.txt 知识梳理

> 来源: `HTML.SafeObject.txt` | 字数: 441

## 内容全文

HTML.SafeObject

TYPE: bool

VERSION: 3.1.1

DEFAULT: false

--DESCRIPTION--

<p>

Whether or not to permit object tags in documents, with a number of extra

security features added to prevent script execution. This is similar to

what websites like MySpace do to object tags.  You should also enable

%Output.FlashCompat in order to generate Internet Explorer

compatibility code for your object tags.

</p>

--# vim: et sw=4 sts=4

