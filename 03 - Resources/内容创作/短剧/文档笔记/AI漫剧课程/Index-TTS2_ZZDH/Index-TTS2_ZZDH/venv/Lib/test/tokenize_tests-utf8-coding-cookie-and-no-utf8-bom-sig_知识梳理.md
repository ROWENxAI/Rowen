---
title: "tokenize_tests-utf8-coding-cookie-and-no-utf8-bom-sig.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\328.短剧 AI漫剧超暴力快速起号新技术\AI漫剧课程\Index-TTS2_ZZDH\Index-TTS2_ZZDH\venv\Lib\test\tokenize_tests-utf8-coding-cookie-and-no-utf8-bom-sig.txt"
---

# tokenize_tests-utf8-coding-cookie-and-no-utf8-bom-sig.txt 知识梳理

> 来源: `tokenize_tests-utf8-coding-cookie-and-no-utf8-bom-sig.txt` | 字数: 411

## 内容全文

# -*- coding: utf-8 -*-

# IMPORTANT: unlike the other test_tokenize-*.txt files, this file

# does NOT have the utf-8 BOM signature '\xef\xbb\xbf' at the start

# of it.  Make sure this is not added inadvertently by your editor

# if any changes are made to this file!

# Arbitrary encoded utf-8 text (stolen from test_doctest2.py).

x = 'ЉЊЈЁЂ'

def y():

"""

And again in a comment.  ЉЊЈЁЂ

"""

pass

