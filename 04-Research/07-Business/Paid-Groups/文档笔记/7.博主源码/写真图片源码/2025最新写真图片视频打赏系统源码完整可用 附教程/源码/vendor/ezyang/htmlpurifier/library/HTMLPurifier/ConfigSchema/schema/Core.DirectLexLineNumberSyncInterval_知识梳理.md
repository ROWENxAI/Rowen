---
title: "Core.DirectLexLineNumberSyncInterval.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.DirectLexLineNumberSyncInterval.txt"
---

# Core.DirectLexLineNumberSyncInterval.txt 知识梳理

> 来源: `Core.DirectLexLineNumberSyncInterval.txt` | 字数: 632

## 内容全文

Core.DirectLexLineNumberSyncInterval

TYPE: int

VERSION: 2.0.0

DEFAULT: 0

--DESCRIPTION--

<p>

Specifies the number of tokens the DirectLex line number tracking

implementations should process before attempting to resyncronize the

current line count by manually counting all previous new-lines. When

at 0, this functionality is disabled. Lower values will decrease

performance, and this is only strictly necessary if the counting

algorithm is buggy (in which case you should report it as a bug).

This has no effect when %Core.MaintainLineNumbers is disabled or DirectLex is

not being used.

</p>

--# vim: et sw=4 sts=4

