---
title: "nginx.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\新进群系统4.1.0-优化版\易支付\nginx.txt"
---

# nginx.txt 知识梳理

> 来源: `nginx.txt` | 字数: 332

## 内容全文

location / {

if (!-e $request_filename) {

rewrite ^/(.[a-zA-Z0-9\-\_]+).html$ /index.php?mod=$1 last;

}

rewrite ^/pay/(.*)$ /pay.php?s=$1 last;

rewrite ^/api/(.*)$ /api.php?s=$1 last;

rewrite ^/doc/(.[a-zA-Z0-9\-\_]+).html$ /index.php?doc=$1 last;

}

location ^~ /plugins {

deny all;

}

location ^~ /includes {

deny all;

}

