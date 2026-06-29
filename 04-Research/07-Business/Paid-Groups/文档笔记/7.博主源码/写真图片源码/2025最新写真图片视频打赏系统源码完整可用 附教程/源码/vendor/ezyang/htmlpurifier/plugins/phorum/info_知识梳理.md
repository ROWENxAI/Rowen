---
title: "info.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\plugins\phorum\info.txt"
---

# info.txt 知识梳理

> 来源: `info.txt` | 字数: 707

## 内容全文

title:   HTML Purifier Phorum Mod

desc:    This module enables standards-compliant HTML filtering on Phorum. Please check migrate.bbcode.php before enabling this mod.

author:  Edward Z. Yang

url:     http://htmlpurifier.org/

version: 4.0.0

hook:  format|phorum_htmlpurifier_format

hook:  quote|phorum_htmlpurifier_quote

hook:  posting_custom_action|phorum_htmlpurifier_posting

hook:  common|phorum_htmlpurifier_common

hook:  before_editor|phorum_htmlpurifier_before_editor

hook:  tpl_editor_after_subject|phorum_htmlpurifier_editor_after_subject

# This module is meant to be a drop-in for bbcode, so make it run last.

priority: run module after *

priority: run hook format after *

vim: et sw=4 sts=4

