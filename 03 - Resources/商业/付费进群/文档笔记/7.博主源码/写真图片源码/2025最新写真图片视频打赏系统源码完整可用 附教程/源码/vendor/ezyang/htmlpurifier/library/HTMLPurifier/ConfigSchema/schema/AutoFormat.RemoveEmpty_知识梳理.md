---
title: "AutoFormat.RemoveEmpty.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\写真图片源码\2025最新写真图片视频打赏系统源码完整可用 附教程\源码\vendor\ezyang\htmlpurifier\library\HTMLPurifier\ConfigSchema\schema\AutoFormat.RemoveEmpty.txt"
---

# AutoFormat.RemoveEmpty.txt 知识梳理

> 来源: `AutoFormat.RemoveEmpty.txt` | 字数: 1774

## 内容全文

AutoFormat.RemoveEmpty

TYPE: bool

VERSION: 3.2.0

DEFAULT: false

--DESCRIPTION--

<p>

When enabled, HTML Purifier will attempt to remove empty elements that

contribute no semantic information to the document. The following types

of nodes will be removed:

</p>

<ul><li>

Tags with no attributes and no content, and that are not empty

elements (remove <code>&lt;a&gt;&lt;/a&gt;</code> but not

<code>&lt;br /&gt;</code>), and

</li>

<li>

Tags with no content, except for:<ul>

<li>The <code>colgroup</code> element, or</li>

<li>

Elements with the <code>id</code> or <code>name</code> attribute,

when those attributes are permitted on those elements.

</li>

</ul></li>

</ul>

<p>

Please be very careful when using this functionality; while it may not

seem that empty elements contain useful information, they can alter the

layout of a document given appropriate styling. This directive is most

useful when you are processing machine-generated HTML, please avoid using

it on regular user HTML.

</p>

<p>

Elements that contain only whitespace will be treated as empty. Non-breaking

spaces, however, do not count as whitespace. See

%AutoFormat.RemoveEmpty.RemoveNbsp for alternate behavior.

</p>

<p>

This algorithm is not perfect; you may still notice some empty tags,

particularly if a node had elements, but those elements were later removed

because they were not permitted in that context, or tags that, after

being auto-closed by another tag, where empty. This is for safety reasons

to prevent clever code from breaking validation. The general rule of thumb:

if a tag looked empty on the way in, it will get removed; if HTML Purifier

made it empty, it will stay.

</p>

--# vim: et sw=4 sts=4

