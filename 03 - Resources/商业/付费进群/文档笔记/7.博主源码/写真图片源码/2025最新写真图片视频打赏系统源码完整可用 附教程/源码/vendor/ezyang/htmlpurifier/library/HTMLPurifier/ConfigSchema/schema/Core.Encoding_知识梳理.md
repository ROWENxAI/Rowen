---
title: "Core.Encoding.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.Encoding.txt"
---

# Core.Encoding.txt 知识梳理

> 来源: `Core.Encoding.txt` | 字数: 767

## 内容全文

Core.Encoding

TYPE: istring

DEFAULT: 'utf-8'

--DESCRIPTION--

If for some reason you are unable to convert all webpages to UTF-8, you can

use this directive as a stop-gap compatibility change to let HTML Purifier

deal with non UTF-8 input.  This technique has notable deficiencies:

absolutely no characters outside of the selected character encoding will be

preserved, not even the ones that have been ampersand escaped (this is due

to a UTF-8 specific <em>feature</em> that automatically resolves all

entities), making it pretty useless for anything except the most I18N-blind

applications, although %Core.EscapeNonASCIICharacters offers fixes this

trouble with another tradeoff. This directive only accepts ISO-8859-1 if

iconv is not enabled.

--# vim: et sw=4 sts=4

