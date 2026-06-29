---
title: "HTML.SafeIframe.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.SafeIframe.txt"
---

# HTML.SafeIframe.txt 知识梳理

> 来源: `HTML.SafeIframe.txt` | 字数: 398

## 内容全文

HTML.SafeIframe

TYPE: bool

VERSION: 4.4.0

DEFAULT: false

--DESCRIPTION--

<p>

Whether or not to permit iframe tags in untrusted documents.  This

directive must be accompanied by a whitelist of permitted iframes,

such as %URI.SafeIframeRegexp, otherwise it will fatally error.

This directive has no effect on strict doctypes, as iframes are not

valid.

</p>

--# vim: et sw=4 sts=4

