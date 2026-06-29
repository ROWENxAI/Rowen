---
title: "HTML.AllowedCommentsRegexp.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\HTML.AllowedCommentsRegexp.txt"
---

# HTML.AllowedCommentsRegexp.txt 知识梳理

> 来源: `HTML.AllowedCommentsRegexp.txt` | 字数: 711

## 内容全文

HTML.AllowedCommentsRegexp

TYPE: string/null

VERSION: 4.4.0

DEFAULT: NULL

--DESCRIPTION--

A regexp, which if it matches the body of a comment, indicates that

it should be allowed. Trailing and leading spaces are removed prior

to running this regular expression.

<strong>Warning:</strong> Make sure you specify

correct anchor metacharacters <code>^regex$</code>, otherwise you may accept

comments that you did not mean to! In particular, the regex <code>/foo|bar/</code>

is probably not sufficiently strict, since it also allows <code>foobar</code>.

See also %HTML.AllowedComments (these directives are union'ed together,

so a comment is considered valid if any directive deems it valid.)

--# vim: et sw=4 sts=4

