---
title: "test_doctest.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\328.短剧 AI漫剧超暴力快速起号新技术\AI漫剧课程\Index-TTS2_ZZDH\Index-TTS2_ZZDH\venv\Lib\test\test_doctest.txt"
---

# test_doctest.txt 知识梳理

> 来源: `test_doctest.txt` | 字数: 300

## 内容全文

This is a sample doctest in a text file.

In this example, we'll rely on a global variable being set for us

already:

>>> favorite_color

'blue'

We can make this fail by disabling the blank-line feature.

>>> if 1:

...    print('a')

...    print()

...    print('b')

a

<BLANKLINE>

b

