---
title: "PatternGrammar.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\328.短剧 AI漫剧超暴力快速起号新技术\AI漫剧课程\Index-TTS2_ZZDH\Index-TTS2_ZZDH\venv\Lib\lib2to3\PatternGrammar.txt"
---

# PatternGrammar.txt 知识梳理

> 来源: `PatternGrammar.txt` | 字数: 793

## 内容全文

# Copyright 2006 Google, Inc. All Rights Reserved.

# Licensed to PSF under a Contributor Agreement.

# A grammar to describe tree matching patterns.

# Not shown here:

# - 'TOKEN' stands for any token (leaf node)

# - 'any' stands for any node (leaf or interior)

# With 'any' we can still specify the sub-structure.

# The start symbol is 'Matcher'.

Matcher: Alternatives ENDMARKER

Alternatives: Alternative ('|' Alternative)*

Alternative: (Unit | NegatedUnit)+

Unit: [NAME '='] ( STRING [Repeater]

| NAME [Details] [Repeater]

| '(' Alternatives ')' [Repeater]

| '[' Alternatives ']'

)

NegatedUnit: 'not' (STRING | NAME [Details] | '(' Alternatives ')')

Repeater: '*' | '+' | '{' NUMBER [',' NUMBER] '}'

Details: '<' Alternatives '>'

