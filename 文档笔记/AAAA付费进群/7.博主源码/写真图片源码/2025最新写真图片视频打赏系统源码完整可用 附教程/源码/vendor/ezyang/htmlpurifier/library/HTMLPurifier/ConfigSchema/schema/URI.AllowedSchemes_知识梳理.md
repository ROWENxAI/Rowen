---
title: "URI.AllowedSchemes.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.AllowedSchemes.txt"
---

# URI.AllowedSchemes.txt 知识梳理

> 来源: `URI.AllowedSchemes.txt` | 字数: 485

## 内容全文

URI.AllowedSchemes

TYPE: lookup

--DEFAULT--

array (

'http' => true,

'https' => true,

'mailto' => true,

'ftp' => true,

'nntp' => true,

'news' => true,

'tel' => true,

)

--DESCRIPTION--

Whitelist that defines the schemes that a URI is allowed to have.  This

prevents XSS attacks from using pseudo-schemes like javascript or mocha.

There is also support for the <code>data</code> and <code>file</code>

URI schemes, but they are not enabled by default.

--# vim: et sw=4 sts=4

