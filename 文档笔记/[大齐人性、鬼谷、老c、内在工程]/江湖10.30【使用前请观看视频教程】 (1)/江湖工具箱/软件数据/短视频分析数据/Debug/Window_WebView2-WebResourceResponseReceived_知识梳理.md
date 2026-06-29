---
title: "Window_WebView2-WebResourceResponseReceived.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "D:\转录\[大齐人性、鬼谷、老c、内在工程]\江湖10.30【使用前请观看视频教程】 (1)\江湖工具箱\软件数据\短视频分析数据\Debug\Window_WebView2-WebResourceResponseReceived.txt"
---

# Window_WebView2-WebResourceResponseReceived.txt 知识梳理

> 来源: `Window_WebView2-WebResourceResponseReceived.txt` | 字数: 1682

## 内容全文

﻿异常链接：https://www.ixigua.com/ttwid/union/register/callback/?aid=1768&ticket=1Rro-ekkQN-K6KPfuV6hOgTuWAoa2lsRvihaOtkBfUbRI4bqwdaia9lsmNf7fmBdV

异常位置：0.4

异常头部：accept   application/json, text/plain, */*

accept-encoding   gzip, deflate, br

accept-language   zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6

cookie   msToken=iLUPCkunJvEcPRo7sju5r7MNpa3vgdpd0Sds3iVhv0UPjFMnrbJtwH_DVGLYWj0Grse99G6jWvXV6TQf9dSclkzbj_ppqu6vM0Kk1236; csrf_session_id=7fd2f47cf09bfd153fbe39a69cd869b8

referer   https://www.ixigua.com/7204145419507630629?id=7289652742623232570&logTag=58b0d1a0590898363569

sec-ch-ua   "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108", "Microsoft Edge WebView2";v="108"

sec-ch-ua-mobile   ?0

sec-ch-ua-platform   "Windows"

sec-fetch-dest   empty

sec-fetch-mode   cors

sec-fetch-site   same-origin

user-agent   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54

x-secsdk-csrf-token   0001000000018dc8e054dbe160adcdc7a39eb7ea3b43fbe94821dadeedeee740078ca52809e517bcf7ad0975fc35

异常标题：异常来自 HRESULT:0xFFFF8300

异常内容：System.Runtime.InteropServices.COMException (0xFFFF8300): 异常来自 HRESULT:0xFFFF8300

在 System.Runtime.InteropServices.Marshal.ThrowExceptionForHRInternal(Int32 errorCode, IntPtr errorInfo)

在 Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponseView.<GetContentAsync>d__13.MoveNext()

--- 引发异常的上一位置中堆栈跟踪的末尾 ---

在 System.Runtime.CompilerServices.TaskAwaiter.ThrowForNonSuccess(Task task)

在 System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)

在 LJHDemo.Window_WebView2.<WebResourceResponseReceived>d__12._01.82()

