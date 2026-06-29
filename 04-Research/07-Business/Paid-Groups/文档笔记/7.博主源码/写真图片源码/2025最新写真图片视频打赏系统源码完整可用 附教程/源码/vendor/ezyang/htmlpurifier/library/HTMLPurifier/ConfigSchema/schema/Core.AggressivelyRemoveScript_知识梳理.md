---
title: "Core.AggressivelyRemoveScript.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.AggressivelyRemoveScript.txt"
---

# Core.AggressivelyRemoveScript.txt 知识梳理

> 来源: `Core.AggressivelyRemoveScript.txt` | 字数: 573

## 内容全文

Core.AggressivelyRemoveScript

TYPE: bool

VERSION: 4.9.0

DEFAULT: true

--DESCRIPTION--

<p>

This directive enables aggressive pre-filter removal of

script tags.  This is not necessary for security,

but it can help work around a bug in libxml where embedded

HTML elements inside script sections cause the parser to

choke.  To revert to pre-4.9.0 behavior, set this to false.

This directive has no effect if %Core.Trusted is true,

%Core.RemoveScriptContents is false, or %Core.HiddenElements

does not contain script.

</p>

--# vim: et sw=4 sts=4

