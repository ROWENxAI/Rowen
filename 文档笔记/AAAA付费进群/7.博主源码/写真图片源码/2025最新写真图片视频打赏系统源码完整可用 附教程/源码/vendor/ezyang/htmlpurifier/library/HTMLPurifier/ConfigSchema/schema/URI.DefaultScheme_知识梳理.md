---
title: "URI.DefaultScheme.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.DefaultScheme.txt"
---

# URI.DefaultScheme.txt 知识梳理

> 来源: `URI.DefaultScheme.txt` | 字数: 404

## 内容全文

URI.DefaultScheme

TYPE: string/null

DEFAULT: 'http'

--DESCRIPTION--

<p>

Defines through what scheme the output will be served, in order to

select the proper object validator when no scheme information is present.

</p>

<p>

Starting with HTML Purifier 4.9.0, the default scheme can be null, in

which case we reject all URIs which do not have explicit schemes.

</p>

--# vim: et sw=4 sts=4

