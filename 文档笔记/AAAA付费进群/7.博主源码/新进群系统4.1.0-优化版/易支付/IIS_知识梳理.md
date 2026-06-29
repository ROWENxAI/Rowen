---
title: "IIS.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\AAAA付费进群\7.博主源码\新进群系统4.1.0-优化版\易支付\IIS.txt"
---

# IIS.txt 知识梳理

> 来源: `IIS.txt` | 字数: 1408

## 内容全文

<rule name="payrule1_rewrite" stopProcessing="true">

<match url="^(.[a-zA-Z0-9-_]+).html"/>

<conditions logicalGrouping="MatchAll">

<add input="{REQUEST_FILENAME}" matchType="IsFile" negate="true"/>

<add input="{REQUEST_FILENAME}" matchType="IsDirectory" negate="true"/>

</conditions>

<action type="Rewrite" url="index.php?mod={R:1}"/>

</rule>

<rule name="payrule2_rewrite" stopProcessing="true">

<match url="^pay/(.*)"/>

<conditions logicalGrouping="MatchAll">

<add input="{REQUEST_FILENAME}" matchType="IsFile" negate="true"/>

<add input="{REQUEST_FILENAME}" matchType="IsDirectory" negate="true"/>

</conditions>

<action type="Rewrite" url="pay.php?s={R:1}"/>

</rule>

<rule name="payrule3_rewrite" stopProcessing="true">

<match url="^api/(.*)"/>

<conditions logicalGrouping="MatchAll">

<add input="{REQUEST_FILENAME}" matchType="IsFile" negate="true"/>

<add input="{REQUEST_FILENAME}" matchType="IsDirectory" negate="true"/>

</conditions>

<action type="Rewrite" url="api.php?s={R:1}"/>

</rule>

<rule name="payrule4_rewrite" stopProcessing="true">

<match url="^doc/(.[a-zA-Z0-9-_]+).html"/>

<conditions logicalGrouping="MatchAll">

<add input="{REQUEST_FILENAME}" matchType="IsFile" negate="true"/>

<add input="{REQUEST_FILENAME}" matchType="IsDirectory" negate="true"/>

</conditions>

<action type="Rewrite" url="index.php?doc={R:1}"/>

</rule>

