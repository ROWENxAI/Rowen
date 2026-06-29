---
title: "Core.MaintainLineNumbers.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.MaintainLineNumbers.txt"
---

# Core.MaintainLineNumbers.txt 知识梳理

> 来源: `Core.MaintainLineNumbers.txt` | 字数: 556

## 内容全文

Core.MaintainLineNumbers

TYPE: bool/null

VERSION: 2.0.0

DEFAULT: NULL

--DESCRIPTION--

<p>

If true, HTML Purifier will add line number information to all tokens.

This is useful when error reporting is turned on, but can result in

significant performance degradation and should not be used when

unnecessary. This directive must be used with the DirectLex lexer,

as the DOMLex lexer does not (yet) support this functionality.

If the value is null, an appropriate value will be selected based

on other configuration.

</p>

--# vim: et sw=4 sts=4

