---
title: "CSS.AllowTricky.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\CSS.AllowTricky.txt"
---

# CSS.AllowTricky.txt 知识梳理

> 来源: `CSS.AllowTricky.txt` | 字数: 461

## 内容全文

CSS.AllowTricky

TYPE: bool

DEFAULT: false

VERSION: 3.1.0

--DESCRIPTION--

This parameter determines whether or not to allow "tricky" CSS properties and

values. Tricky CSS properties/values can drastically modify page layout or

be used for deceptive practices but do not directly constitute a security risk.

For example, <code>display:none;</code> is considered a tricky property that

will only be allowed if this directive is set to true.

--# vim: et sw=4 sts=4

