---
title: "URI.MungeSecretKey.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\URI.MungeSecretKey.txt"
---

# URI.MungeSecretKey.txt 知识梳理

> 来源: `URI.MungeSecretKey.txt` | 字数: 978

## 内容全文

URI.MungeSecretKey

TYPE: string/null

VERSION: 3.1.1

DEFAULT: NULL

--DESCRIPTION--

<p>

This directive enables secure checksum generation along with %URI.Munge.

It should be set to a secure key that is not shared with anyone else.

The checksum can be placed in the URI using %t. Use of this checksum

affords an additional level of protection by allowing a redirector

to check if a URI has passed through HTML Purifier with this line:

</p>

<pre>$checksum === hash_hmac("sha256", $url, $secret_key)</pre>

<p>

If the output is TRUE, the redirector script should accept the URI.

</p>

<p>

Please note that it would still be possible for an attacker to procure

secure hashes en-mass by abusing your website's Preview feature or the

like, but this service affords an additional level of protection

that should be combined with website blacklisting.

</p>

<p>

Remember this has no effect if %URI.Munge is not on.

</p>

--# vim: et sw=4 sts=4

