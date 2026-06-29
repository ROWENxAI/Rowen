---
title: "URI.Host.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.Host.txt"
---

# URI.Host.txt 知识梳理

> 来源: `URI.Host.txt` | 字数: 818

## 内容全文

URI.Host

TYPE: string/null

VERSION: 1.2.0

DEFAULT: NULL

--DESCRIPTION--

<p>

Defines the domain name of the server, so we can determine whether or

an absolute URI is from your website or not.  Not strictly necessary,

as users should be using relative URIs to reference resources on your

website.  It will, however, let you use absolute URIs to link to

subdomains of the domain you post here: i.e. example.com will allow

sub.example.com.  However, higher up domains will still be excluded:

if you set %URI.Host to sub.example.com, example.com will be blocked.

<strong>Note:</strong> This directive overrides %URI.Base because

a given page may be on a sub-domain, but you wish HTML Purifier to be

more relaxed and allow some of the parent domains too.

</p>

--# vim: et sw=4 sts=4

