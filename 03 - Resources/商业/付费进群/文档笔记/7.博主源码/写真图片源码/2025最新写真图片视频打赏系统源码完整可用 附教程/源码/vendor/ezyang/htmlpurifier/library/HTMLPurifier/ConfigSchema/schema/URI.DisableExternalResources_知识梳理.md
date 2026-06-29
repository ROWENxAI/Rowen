---
title: "URI.DisableExternalResources.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.DisableExternalResources.txt"
---

# URI.DisableExternalResources.txt 知识梳理

> 来源: `URI.DisableExternalResources.txt` | 字数: 549

## 内容全文

URI.DisableExternalResources

TYPE: bool

VERSION: 1.3.0

DEFAULT: false

--DESCRIPTION--

Disables the embedding of external resources, preventing users from

embedding things like images from other hosts. This prevents access

tracking (good for email viewers), bandwidth leeching, cross-site request

forging, goatse.cx posting, and other nasties, but also results in a loss

of end-user functionality (they can't directly post a pic they posted from

Flickr anymore). Use it if you don't have a robust user-content moderation

team.

--# vim: et sw=4 sts=4

