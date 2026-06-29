---
title: "Core.RemoveProcessingInstructions.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.RemoveProcessingInstructions.txt"
---

# Core.RemoveProcessingInstructions.txt 知识梳理

> 来源: `Core.RemoveProcessingInstructions.txt` | 字数: 398

## 内容全文

Core.RemoveProcessingInstructions

TYPE: bool

VERSION: 4.2.0

DEFAULT: false

--DESCRIPTION--

Instead of escaping processing instructions in the form <code>&lt;? ...

?&gt;</code>, remove it out-right.  This may be useful if the HTML

you are validating contains XML processing instruction gunk, however,

it can also be user-unfriendly for people attempting to post PHP

snippets.

--# vim: et sw=4 sts=4

