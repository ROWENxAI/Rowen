---
title: "Core.AggressivelyFixLt.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.AggressivelyFixLt.txt"
---

# Core.AggressivelyFixLt.txt 知识梳理

> 来源: `Core.AggressivelyFixLt.txt` | 字数: 662

## 内容全文

Core.AggressivelyFixLt

TYPE: bool

VERSION: 2.1.0

DEFAULT: true

--DESCRIPTION--

<p>

This directive enables aggressive pre-filter fixes HTML Purifier can

perform in order to ensure that open angled-brackets do not get killed

during parsing stage. Enabling this will result in two preg_replace_callback

calls and at least two preg_replace calls for every HTML document parsed;

if your users make very well-formed HTML, you can set this directive false.

This has no effect when DirectLex is used.

</p>

<p>

<strong>Notice:</strong> This directive's default turned from false to true

in HTML Purifier 3.2.0.

</p>

--# vim: et sw=4 sts=4

