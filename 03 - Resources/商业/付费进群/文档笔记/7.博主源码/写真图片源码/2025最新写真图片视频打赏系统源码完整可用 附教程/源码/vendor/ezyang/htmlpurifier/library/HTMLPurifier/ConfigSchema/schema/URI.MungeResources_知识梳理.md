---
title: "URI.MungeResources.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.MungeResources.txt"
---

# URI.MungeResources.txt 知识梳理

> 来源: `URI.MungeResources.txt` | 字数: 611

## 内容全文

URI.MungeResources

TYPE: bool

VERSION: 3.1.1

DEFAULT: false

--DESCRIPTION--

<p>

If true, any URI munging directives like %URI.Munge

will also apply to embedded resources, such as <code>&lt;img src=""&gt;</code>.

Be careful enabling this directive if you have a redirector script

that does not use the <code>Location</code> HTTP header; all of your images

and other embedded resources will break.

</p>

<p>

<strong>Warning:</strong> It is strongly advised you use this in conjunction

%URI.MungeSecretKey to mitigate the security risk of an open redirector.

</p>

--# vim: et sw=4 sts=4

