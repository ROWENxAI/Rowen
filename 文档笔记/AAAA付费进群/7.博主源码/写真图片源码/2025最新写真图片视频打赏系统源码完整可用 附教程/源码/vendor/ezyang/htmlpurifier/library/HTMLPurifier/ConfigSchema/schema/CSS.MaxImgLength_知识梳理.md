---
title: "CSS.MaxImgLength.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\CSS.MaxImgLength.txt"
---

# CSS.MaxImgLength.txt 知识梳理

> 来源: `CSS.MaxImgLength.txt` | 字数: 623

## 内容全文

CSS.MaxImgLength

TYPE: string/null

DEFAULT: '1200px'

VERSION: 3.1.1

--DESCRIPTION--

<p>

This parameter sets the maximum allowed length on <code>img</code> tags,

effectively the <code>width</code> and <code>height</code> properties.

Only absolute units of measurement (in, pt, pc, mm, cm) and pixels (px) are allowed. This is

in place to prevent imagecrash attacks, disable with null at your own risk.

This directive is similar to %HTML.MaxImgLength, and both should be

concurrently edited, although there are

subtle differences in the input format (the CSS max is a number with

a unit).

</p>

--# vim: et sw=4 sts=4

