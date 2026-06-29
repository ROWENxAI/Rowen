---
title: "exception_hierarchy.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\328.短剧 AI漫剧超暴力快速起号新技术\AI漫剧课程\Index-TTS2_ZZDH\Index-TTS2_ZZDH\venv\Lib\test\exception_hierarchy.txt"
---

# exception_hierarchy.txt 知识梳理

> 来源: `exception_hierarchy.txt` | 字数: 1853

## 内容全文

BaseException

+-- SystemExit

+-- KeyboardInterrupt

+-- GeneratorExit

+-- Exception

+-- StopIteration

+-- StopAsyncIteration

+-- ArithmeticError

|    +-- FloatingPointError

|    +-- OverflowError

|    +-- ZeroDivisionError

+-- AssertionError

+-- AttributeError

+-- BufferError

+-- EOFError

+-- ImportError

|    +-- ModuleNotFoundError

+-- LookupError

|    +-- IndexError

|    +-- KeyError

+-- MemoryError

+-- NameError

|    +-- UnboundLocalError

+-- OSError

|    +-- BlockingIOError

|    +-- ChildProcessError

|    +-- ConnectionError

|    |    +-- BrokenPipeError

|    |    +-- ConnectionAbortedError

|    |    +-- ConnectionRefusedError

|    |    +-- ConnectionResetError

|    +-- FileExistsError

|    +-- FileNotFoundError

|    +-- InterruptedError

|    +-- IsADirectoryError

|    +-- NotADirectoryError

|    +-- PermissionError

|    +-- ProcessLookupError

|    +-- TimeoutError

+-- ReferenceError

+-- RuntimeError

|    +-- NotImplementedError

|    +-- RecursionError

+-- SyntaxError

|    +-- IndentationError

|         +-- TabError

+-- SystemError

+-- TypeError

+-- ValueError

|    +-- UnicodeError

|         +-- UnicodeDecodeError

|         +-- UnicodeEncodeError

|         +-- UnicodeTranslateError

+-- Warning

+-- DeprecationWarning

+-- PendingDeprecationWarning

+-- RuntimeWarning

+-- SyntaxWarning

+-- UserWarning

+-- FutureWarning

+-- ImportWarning

+-- UnicodeWarning

+-- BytesWarning

+-- EncodingWarning

+-- ResourceWarning

