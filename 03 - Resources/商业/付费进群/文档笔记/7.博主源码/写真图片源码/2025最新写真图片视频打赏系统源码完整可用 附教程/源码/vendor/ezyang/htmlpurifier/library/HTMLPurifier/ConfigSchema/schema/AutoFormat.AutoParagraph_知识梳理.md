---
title: "AutoFormat.AutoParagraph.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\AutoFormat.AutoParagraph.txt"
---

# AutoFormat.AutoParagraph.txt 知识梳理

> 来源: `AutoFormat.AutoParagraph.txt` | 字数: 1138

## 内容全文

AutoFormat.AutoParagraph

TYPE: bool

VERSION: 2.0.1

DEFAULT: false

--DESCRIPTION--

<p>

This directive turns on auto-paragraphing, where double newlines are

converted in to paragraphs whenever possible. Auto-paragraphing:

</p>

<ul>

<li>Always applies to inline elements or text in the root node,</li>

<li>Applies to inline elements or text with double newlines in nodes

that allow paragraph tags,</li>

<li>Applies to double newlines in paragraph tags</li>

</ul>

<p>

<code>p</code> tags must be allowed for this directive to take effect.

We do not use <code>br</code> tags for paragraphing, as that is

semantically incorrect.

</p>

<p>

To prevent auto-paragraphing as a content-producer, refrain from using

double-newlines except to specify a new paragraph or in contexts where

it has special meaning (whitespace usually has no meaning except in

tags like <code>pre</code>, so this should not be difficult.) To prevent

the paragraphing of inline text adjacent to block elements, wrap them

in <code>div</code> tags (the behavior is slightly different outside of

the root node.)

</p>

--# vim: et sw=4 sts=4

