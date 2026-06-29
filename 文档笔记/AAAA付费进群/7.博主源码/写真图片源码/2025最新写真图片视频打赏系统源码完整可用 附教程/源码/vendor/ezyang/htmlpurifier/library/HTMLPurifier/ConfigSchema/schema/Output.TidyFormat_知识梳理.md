---
title: "Output.TidyFormat.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Output.TidyFormat.txt"
---

# Output.TidyFormat.txt 知识梳理

> 来源: `Output.TidyFormat.txt` | 字数: 827

## 内容全文

Output.TidyFormat

TYPE: bool

VERSION: 1.1.1

DEFAULT: false

--DESCRIPTION--

<p>

Determines whether or not to run Tidy on the final output for pretty

formatting reasons, such as indentation and wrap.

</p>

<p>

This can greatly improve readability for editors who are hand-editing

the HTML, but is by no means necessary as HTML Purifier has already

fixed all major errors the HTML may have had. Tidy is a non-default

extension, and this directive will silently fail if Tidy is not

available.

</p>

<p>

If you are looking to make the overall look of your page's source

better, I recommend running Tidy on the entire page rather than just

user-content (after all, the indentation relative to the containing

blocks will be incorrect).

</p>

--ALIASES--

Core.TidyFormat

--# vim: et sw=4 sts=4

