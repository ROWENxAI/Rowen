---
title: "Attr.DefaultImageAlt.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Attr.DefaultImageAlt.txt"
---

# Attr.DefaultImageAlt.txt 知识梳理

> 来源: `Attr.DefaultImageAlt.txt` | 字数: 479

## 内容全文

Attr.DefaultImageAlt

TYPE: string/null

DEFAULT: null

VERSION: 3.2.0

--DESCRIPTION--

This is the content of the alt tag of an image if the user had not

previously specified an alt attribute.  This applies to all images without

a valid alt attribute, as opposed to %Attr.DefaultInvalidImageAlt, which

only applies to invalid images, and overrides in the case of an invalid image.

Default behavior with null is to use the basename of the src tag for the alt.

--# vim: et sw=4 sts=4

