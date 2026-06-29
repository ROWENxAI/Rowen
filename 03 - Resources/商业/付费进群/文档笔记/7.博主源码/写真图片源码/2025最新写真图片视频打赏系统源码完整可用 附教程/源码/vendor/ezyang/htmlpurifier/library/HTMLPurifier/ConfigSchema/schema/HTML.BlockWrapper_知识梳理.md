---
title: "HTML.BlockWrapper.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.BlockWrapper.txt"
---

# HTML.BlockWrapper.txt 知识梳理

> 来源: `HTML.BlockWrapper.txt` | 字数: 571

## 内容全文

HTML.BlockWrapper

TYPE: string

VERSION: 1.3.0

DEFAULT: 'p'

--DESCRIPTION--

<p>

String name of element to wrap inline elements that are inside a block

context.  This only occurs in the children of blockquote in strict mode.

</p>

<p>

Example: by default value,

<code>&lt;blockquote&gt;Foo&lt;/blockquote&gt;</code> would become

<code>&lt;blockquote&gt;&lt;p&gt;Foo&lt;/p&gt;&lt;/blockquote&gt;</code>.

The <code>&lt;p&gt;</code> tags can be replaced with whatever you desire,

as long as it is a block level element.

</p>

--# vim: et sw=4 sts=4

