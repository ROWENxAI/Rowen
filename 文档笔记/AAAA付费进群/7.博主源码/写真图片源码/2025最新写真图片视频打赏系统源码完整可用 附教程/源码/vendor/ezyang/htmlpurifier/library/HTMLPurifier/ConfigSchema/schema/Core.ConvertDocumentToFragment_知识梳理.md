---
title: "Core.ConvertDocumentToFragment.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Core.ConvertDocumentToFragment.txt"
---

# Core.ConvertDocumentToFragment.txt 知识梳理

> 来源: `Core.ConvertDocumentToFragment.txt` | 字数: 433

## 内容全文

Core.ConvertDocumentToFragment

TYPE: bool

DEFAULT: true

--DESCRIPTION--

This parameter determines whether or not the filter should convert

input that is a full document with html and body tags to a fragment

of just the contents of a body tag. This parameter is simply something

HTML Purifier can do during an edge-case: for most inputs, this

processing is not necessary.

--ALIASES--

Core.AcceptFullDocuments

--# vim: et sw=4 sts=4

