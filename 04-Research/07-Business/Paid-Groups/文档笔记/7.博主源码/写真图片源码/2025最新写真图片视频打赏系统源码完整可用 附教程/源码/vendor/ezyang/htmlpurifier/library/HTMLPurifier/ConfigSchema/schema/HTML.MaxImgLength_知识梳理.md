---
title: "HTML.MaxImgLength.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.MaxImgLength.txt"
---

# HTML.MaxImgLength.txt 知识梳理

> 来源: `HTML.MaxImgLength.txt` | 字数: 490

## 内容全文

HTML.MaxImgLength

TYPE: int/null

DEFAULT: 1200

VERSION: 3.1.1

--DESCRIPTION--

<p>

This directive controls the maximum number of pixels in the width and

height attributes in <code>img</code> tags. This is

in place to prevent imagecrash attacks, disable with null at your own risk.

This directive is similar to %CSS.MaxImgLength, and both should be

concurrently edited, although there are

subtle differences in the input format (the HTML max is an integer).

</p>

--# vim: et sw=4 sts=4

