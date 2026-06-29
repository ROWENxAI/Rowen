---
title: "Core.DisableExcludes.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.DisableExcludes.txt"
---

# Core.DisableExcludes.txt 知识梳理

> 来源: `Core.DisableExcludes.txt` | 字数: 458

## 内容全文

Core.DisableExcludes

TYPE: bool

DEFAULT: false

VERSION: 4.5.0

--DESCRIPTION--

<p>

This directive disables SGML-style exclusions, e.g. the exclusion of

<code>&lt;object&gt;</code> in any descendant of a

<code>&lt;pre&gt;</code> tag.  Disabling excludes will allow some

invalid documents to pass through HTML Purifier, but HTML Purifier

will also be less likely to accidentally remove large documents during

processing.

</p>

--# vim: et sw=4 sts=4

