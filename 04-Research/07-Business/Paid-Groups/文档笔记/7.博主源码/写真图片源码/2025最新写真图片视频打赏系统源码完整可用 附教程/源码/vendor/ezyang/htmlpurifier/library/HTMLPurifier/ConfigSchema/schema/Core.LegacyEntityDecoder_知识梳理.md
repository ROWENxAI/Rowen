---
title: "Core.LegacyEntityDecoder.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.LegacyEntityDecoder.txt"
---

# Core.LegacyEntityDecoder.txt 知识梳理

> 来源: `Core.LegacyEntityDecoder.txt` | 字数: 1391

## 内容全文

Core.LegacyEntityDecoder

TYPE: bool

VERSION: 4.9.0

DEFAULT: false

--DESCRIPTION--

<p>

Prior to HTML Purifier 4.9.0, entities were decoded by performing

a global search replace for all entities whose decoded versions

did not have special meanings under HTML, and replaced them with

their decoded versions.  We would match all entities, even if they did

not have a trailing semicolon, but only if there weren't any trailing

alphanumeric characters.

</p>

<table>

<tr><th>Original</th><th>Text</th><th>Attribute</th></tr>

<tr><td>&amp;yen;</td><td>&yen;</td><td>&yen;</td></tr>

<tr><td>&amp;yen</td><td>&yen;</td><td>&yen;</td></tr>

<tr><td>&amp;yena</td><td>&amp;yena</td><td>&amp;yena</td></tr>

<tr><td>&amp;yen=</td><td>&yen;=</td><td>&yen;=</td></tr>

</table>

<p>

In HTML Purifier 4.9.0, we changed the behavior of entity parsing

to match entities that had missing trailing semicolons in less

cases, to more closely match HTML5 parsing behavior:

</p>

<table>

<tr><th>Original</th><th>Text</th><th>Attribute</th></tr>

<tr><td>&amp;yen;</td><td>&yen;</td><td>&yen;</td></tr>

<tr><td>&amp;yen</td><td>&yen;</td><td>&yen;</td></tr>

<tr><td>&amp;yena</td><td>&yen;a</td><td>&amp;yena</td></tr>

<tr><td>&amp;yen=</td><td>&yen;=</td><td>&amp;yen=</td></tr>

</table>

<p>

This flag reverts back to pre-HTML Purifier 4.9.0 behavior.

</p>

--# vim: et sw=4 sts=4

