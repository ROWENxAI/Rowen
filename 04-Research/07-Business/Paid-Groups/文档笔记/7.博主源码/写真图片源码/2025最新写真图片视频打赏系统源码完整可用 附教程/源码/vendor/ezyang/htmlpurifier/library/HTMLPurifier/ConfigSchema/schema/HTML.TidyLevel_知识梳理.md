---
title: "HTML.TidyLevel.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.TidyLevel.txt"
---

# HTML.TidyLevel.txt 知识梳理

> 来源: `HTML.TidyLevel.txt` | 字数: 620

## 内容全文

HTML.TidyLevel

TYPE: string

VERSION: 2.0.0

DEFAULT: 'medium'

--DESCRIPTION--

<p>General level of cleanliness the Tidy module should enforce.

There are four allowed values:</p>

<dl>

<dt>none</dt>

<dd>No extra tidying should be done</dd>

<dt>light</dt>

<dd>Only fix elements that would be discarded otherwise due to

lack of support in doctype</dd>

<dt>medium</dt>

<dd>Enforce best practices</dd>

<dt>heavy</dt>

<dd>Transform all deprecated elements and attributes to standards

compliant equivalents</dd>

</dl>

--ALLOWED--

'none', 'light', 'medium', 'heavy'

--# vim: et sw=4 sts=4

