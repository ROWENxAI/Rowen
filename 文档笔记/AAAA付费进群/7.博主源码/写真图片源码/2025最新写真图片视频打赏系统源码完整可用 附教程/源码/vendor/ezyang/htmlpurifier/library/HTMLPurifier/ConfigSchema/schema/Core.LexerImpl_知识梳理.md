---
title: "Core.LexerImpl.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.LexerImpl.txt"
---

# Core.LexerImpl.txt 知识梳理

> 来源: `Core.LexerImpl.txt` | 字数: 1044

## 内容全文

Core.LexerImpl

TYPE: mixed/null

VERSION: 2.0.0

DEFAULT: NULL

--DESCRIPTION--

<p>

This parameter determines what lexer implementation can be used. The

valid values are:

</p>

<dl>

<dt><em>null</em></dt>

<dd>

Recommended, the lexer implementation will be auto-detected based on

your PHP-version and configuration.

</dd>

<dt><em>string</em> lexer identifier</dt>

<dd>

This is a slim way of manually overridding the implementation.

Currently recognized values are: DOMLex (the default PHP5

implementation)

and DirectLex (the default PHP4 implementation). Only use this if

you know what you are doing: usually, the auto-detection will

manage things for cases you aren't even aware of.

</dd>

<dt><em>object</em> lexer instance</dt>

<dd>

Super-advanced: you can specify your own, custom, implementation that

implements the interface defined by <code>HTMLPurifier_Lexer</code>.

I may remove this option simply because I don't expect anyone

to use it.

</dd>

</dl>

--# vim: et sw=4 sts=4

