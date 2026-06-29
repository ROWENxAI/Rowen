---
title: "Core.EscapeNonASCIICharacters.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.EscapeNonASCIICharacters.txt"
---

# Core.EscapeNonASCIICharacters.txt 知识梳理

> 来源: `Core.EscapeNonASCIICharacters.txt` | 字数: 567

## 内容全文

Core.EscapeNonASCIICharacters

TYPE: bool

VERSION: 1.4.0

DEFAULT: false

--DESCRIPTION--

This directive overcomes a deficiency in %Core.Encoding by blindly

converting all non-ASCII characters into decimal numeric entities before

converting it to its native encoding. This means that even characters that

can be expressed in the non-UTF-8 encoding will be entity-ized, which can

be a real downer for encodings like Big5. It also assumes that the ASCII

repetoire is available, although this is the case for almost all encodings.

Anyway, use UTF-8!

--# vim: et sw=4 sts=4

