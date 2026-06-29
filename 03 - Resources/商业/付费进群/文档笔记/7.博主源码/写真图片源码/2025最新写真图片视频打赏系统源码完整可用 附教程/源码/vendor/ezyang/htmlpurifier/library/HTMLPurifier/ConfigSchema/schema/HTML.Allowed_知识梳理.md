---
title: "HTML.Allowed.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.Allowed.txt"
---

# HTML.Allowed.txt 知识梳理

> 来源: `HTML.Allowed.txt` | 字数: 996

## 内容全文

HTML.Allowed

TYPE: itext/null

VERSION: 2.0.0

DEFAULT: NULL

--DESCRIPTION--

<p>

This is a preferred convenience directive that combines

%HTML.AllowedElements and %HTML.AllowedAttributes.

Specify elements and attributes that are allowed using:

<code>element1[attr1|attr2],element2...</code>.  For example,

if you would like to only allow paragraphs and links, specify

<code>a[href],p</code>.  You can specify attributes that apply

to all elements using an asterisk, e.g. <code>*[lang]</code>.

You can also use newlines instead of commas to separate elements.

</p>

<p>

<strong>Warning</strong>:

All of the constraints on the component directives are still enforced.

The syntax is a <em>subset</em> of TinyMCE's <code>valid_elements</code>

whitelist: directly copy-pasting it here will probably result in

broken whitelists. If %HTML.AllowedElements or %HTML.AllowedAttributes

are set, this directive has no effect.

</p>

--# vim: et sw=4 sts=4

