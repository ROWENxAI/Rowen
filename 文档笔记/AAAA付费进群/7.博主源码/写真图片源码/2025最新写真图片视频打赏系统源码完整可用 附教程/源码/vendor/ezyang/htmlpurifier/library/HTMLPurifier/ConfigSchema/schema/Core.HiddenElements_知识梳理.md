---
title: "Core.HiddenElements.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.HiddenElements.txt"
---

# Core.HiddenElements.txt 知识梳理

> 来源: `Core.HiddenElements.txt` | 字数: 575

## 内容全文

Core.HiddenElements

TYPE: lookup

--DEFAULT--

array (

'script' => true,

'style' => true,

)

--DESCRIPTION--

<p>

This directive is a lookup array of elements which should have their

contents removed when they are not allowed by the HTML definition.

For example, the contents of a <code>script</code> tag are not

normally shown in a document, so if script tags are to be removed,

their contents should be removed to. This is opposed to a <code>b</code>

tag, which defines some presentational changes but does not hide its

contents.

</p>

--# vim: et sw=4 sts=4

