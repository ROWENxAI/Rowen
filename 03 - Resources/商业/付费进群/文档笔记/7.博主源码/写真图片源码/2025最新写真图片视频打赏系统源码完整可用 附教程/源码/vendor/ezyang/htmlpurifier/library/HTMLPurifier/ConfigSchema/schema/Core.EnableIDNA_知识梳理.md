---
title: "Core.EnableIDNA.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.EnableIDNA.txt"
---

# Core.EnableIDNA.txt 知识梳理

> 来源: `Core.EnableIDNA.txt` | 字数: 303

## 内容全文

Core.EnableIDNA

TYPE: bool

DEFAULT: false

VERSION: 4.4.0

--DESCRIPTION--

Allows international domain names in URLs.  This configuration option

requires the PEAR Net_IDNA2 module to be installed.  It operates by

punycoding any internationalized host names for maximum portability.

--# vim: et sw=4 sts=4

