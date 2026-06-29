---
title: "Cache.DefinitionImpl.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\Cache.DefinitionImpl.txt"
---

# Cache.DefinitionImpl.txt 知识梳理

> 来源: `Cache.DefinitionImpl.txt` | 字数: 374

## 内容全文

Cache.DefinitionImpl

TYPE: string/null

VERSION: 2.0.0

DEFAULT: 'Serializer'

--DESCRIPTION--

This directive defines which method to use when caching definitions,

the complex data-type that makes HTML Purifier tick. Set to null

to disable caching (not recommended, as you will see a definite

performance degradation).

--ALIASES--

Core.DefinitionCache

--# vim: et sw=4 sts=4

