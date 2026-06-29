---
title: "URI.HostBlacklist.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.HostBlacklist.txt"
---

# URI.HostBlacklist.txt 知识梳理

> 来源: `URI.HostBlacklist.txt` | 字数: 310

## 内容全文

URI.HostBlacklist

TYPE: list

VERSION: 1.3.0

DEFAULT: array()

--DESCRIPTION--

List of strings that are forbidden in the host of any URI. Use it to kill

domain names of spam, etc. Note that it will catch anything in the domain,

so <tt>moo.com</tt> will catch <tt>moo.com.example.com</tt>.

--# vim: et sw=4 sts=4

