---
title: "Core.RemoveInvalidImg.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.RemoveInvalidImg.txt"
---

# Core.RemoveInvalidImg.txt 知识梳理

> 来源: `Core.RemoveInvalidImg.txt` | 字数: 334

## 内容全文

Core.RemoveInvalidImg

TYPE: bool

DEFAULT: true

VERSION: 1.3.0

--DESCRIPTION--

<p>

This directive enables pre-emptive URI checking in <code>img</code>

tags, as the attribute validation strategy is not authorized to

remove elements from the document. Revert to pre-1.3.0 behavior by setting to false.

</p>

--# vim: et sw=4 sts=4

