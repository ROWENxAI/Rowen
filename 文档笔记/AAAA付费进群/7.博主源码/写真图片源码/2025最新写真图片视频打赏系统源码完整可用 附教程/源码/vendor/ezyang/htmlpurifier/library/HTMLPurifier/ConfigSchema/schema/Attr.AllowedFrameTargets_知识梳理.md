---
title: "Attr.AllowedFrameTargets.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Attr.AllowedFrameTargets.txt"
---

# Attr.AllowedFrameTargets.txt 知识梳理

> 来源: `Attr.AllowedFrameTargets.txt` | 字数: 578

## 内容全文

Attr.AllowedFrameTargets

TYPE: lookup

DEFAULT: array()

--DESCRIPTION--

Lookup table of all allowed link frame targets.  Some commonly used link

targets include _blank, _self, _parent and _top. Values should be

lowercase, as validation will be done in a case-sensitive manner despite

W3C's recommendation. XHTML 1.0 Strict does not permit the target attribute

so this directive will have no effect in that doctype. XHTML 1.1 does not

enable the Target module by default, you will have to manually enable it

(see the module documentation for more details.)

--# vim: et sw=4 sts=4

