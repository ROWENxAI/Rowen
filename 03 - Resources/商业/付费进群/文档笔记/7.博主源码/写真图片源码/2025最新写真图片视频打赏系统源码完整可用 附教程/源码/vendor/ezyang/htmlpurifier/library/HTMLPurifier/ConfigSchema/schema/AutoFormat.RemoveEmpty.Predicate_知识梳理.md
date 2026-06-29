---
title: "AutoFormat.RemoveEmpty.Predicate.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\AutoFormat.RemoveEmpty.Predicate.txt"
---

# AutoFormat.RemoveEmpty.Predicate.txt 知识梳理

> 来源: `AutoFormat.RemoveEmpty.Predicate.txt` | 字数: 632

## 内容全文

AutoFormat.RemoveEmpty.Predicate

TYPE: hash

VERSION: 4.7.0

DEFAULT: array('colgroup' => array(), 'th' => array(), 'td' => array(), 'iframe' => array('src'))

--DESCRIPTION--

<p>

Given that an element has no contents, it will be removed by default, unless

this predicate dictates otherwise.  The predicate can either be an associative

map from tag name to list of attributes that must be present for the element

to be considered preserved: thus, the default always preserves <code>colgroup</code>,

<code>th</code> and <code>td</code>, and also <code>iframe</code> if it

has a <code>src</code>.

</p>

--# vim: et sw=4 sts=4

