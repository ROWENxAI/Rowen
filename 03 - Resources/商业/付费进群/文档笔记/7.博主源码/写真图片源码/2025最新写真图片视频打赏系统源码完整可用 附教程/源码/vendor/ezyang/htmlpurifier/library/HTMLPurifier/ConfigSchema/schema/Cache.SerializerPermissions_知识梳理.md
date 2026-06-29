---
title: "Cache.SerializerPermissions.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Cache.SerializerPermissions.txt"
---

# Cache.SerializerPermissions.txt 知识梳理

> 来源: `Cache.SerializerPermissions.txt` | 字数: 407

## 内容全文

Cache.SerializerPermissions

TYPE: int/null

VERSION: 4.3.0

DEFAULT: 0755

--DESCRIPTION--

<p>

Directory permissions of the files and directories created inside

the DefinitionCache/Serializer or other custom serializer path.

</p>

<p>

In HTML Purifier 4.8.0, this also supports <code>NULL</code>,

which means that no chmod'ing or directory creation shall

occur.

</p>

--# vim: et sw=4 sts=4

