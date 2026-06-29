---
title: "URI.SafeIframeRegexp.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.SafeIframeRegexp.txt"
---

# URI.SafeIframeRegexp.txt 知识梳理

> 来源: `URI.SafeIframeRegexp.txt` | 字数: 897

## 内容全文

URI.SafeIframeRegexp

TYPE: string/null

VERSION: 4.4.0

DEFAULT: NULL

--DESCRIPTION--

<p>

A PCRE regular expression that will be matched against an iframe URI.  This is

a relatively inflexible scheme, but works well enough for the most common

use-case of iframes: embedded video.  This directive only has an effect if

%HTML.SafeIframe is enabled.  Here are some example values:

</p>

<ul>

<li><code>%^http://www.youtube.com/embed/%</code> - Allow YouTube videos</li>

<li><code>%^http://player.vimeo.com/video/%</code> - Allow Vimeo videos</li>

<li><code>%^http://(www.youtube.com/embed/|player.vimeo.com/video/)%</code> - Allow both</li>

</ul>

<p>

Note that this directive does not give you enough granularity to, say, disable

all <code>autoplay</code> videos.  Pipe up on the HTML Purifier forums if this

is a capability you want.

</p>

--# vim: et sw=4 sts=4

