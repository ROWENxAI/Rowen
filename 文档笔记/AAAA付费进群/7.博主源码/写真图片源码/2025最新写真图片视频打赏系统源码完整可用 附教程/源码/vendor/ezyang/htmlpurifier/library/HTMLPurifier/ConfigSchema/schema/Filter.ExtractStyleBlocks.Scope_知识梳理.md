---
title: "Filter.ExtractStyleBlocks.Scope.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Filter.ExtractStyleBlocks.Scope.txt"
---

# Filter.ExtractStyleBlocks.Scope.txt 知识梳理

> 来源: `Filter.ExtractStyleBlocks.Scope.txt` | 字数: 1200

## 内容全文

Filter.ExtractStyleBlocks.Scope

TYPE: string/null

VERSION: 3.0.0

DEFAULT: NULL

ALIASES: Filter.ExtractStyleBlocksScope, FilterParam.ExtractStyleBlocksScope

--DESCRIPTION--

<p>

If you would like users to be able to define external stylesheets, but

only allow them to specify CSS declarations for a specific node and

prevent them from fiddling with other elements, use this directive.

It accepts any valid CSS selector, and will prepend this to any

CSS declaration extracted from the document. For example, if this

directive is set to <code>#user-content</code> and a user uses the

selector <code>a:hover</code>, the final selector will be

<code>#user-content a:hover</code>.

</p>

<p>

The comma shorthand may be used; consider the above example, with

<code>#user-content, #user-content2</code>, the final selector will

be <code>#user-content a:hover, #user-content2 a:hover</code>.

</p>

<p>

<strong>Warning:</strong> It is possible for users to bypass this measure

using a naughty + selector. This is a bug in CSS Tidy 1.3, not HTML

Purifier, and I am working to get it fixed. Until then, HTML Purifier

performs a basic check to prevent this.

</p>

--# vim: et sw=4 sts=4

