---
layout: page
title: Баги не только в программах, но и в новостях
image:
  title: /images/blog/o-rly.png
  thumb: /images/blog/o-rly.png
redirect_from: /blog/140-buggy-selenium-news.html
date: 2015-06-09 13:08:53.000000000 +03:00
author: Алексей Баранцев
teaser: Новости надо читать с большой осторожностью, потому что там тоже есть баги. Иногда вроде бы уважаемая компания опубликует что-нибудь этакое
category: Блог
---
Новости надо читать с большой осторожностью, потому что там тоже есть баги. Иногда вроде бы уважаемая компания опубликует что-нибудь этакое...

Наткнулся недавно на [вот эту статью на сайте SmartBear](http://smartbear.com/all-resources/articles/what-s-new-in-selenium/), и обнаружил там такую "новость":

*"As of version 2.44, when you do something like window.click('button') in FireFox, you are actually causing the browser to fire a real click event. FireFox automation is more realistic than it has ever been."*

Это должно означать, что начиная с версии 2.44 в Selenium якобы появились "нативные события", которые более лучше, чем синтезированные.

**Разумеется, это неправда. Нативные события впервые появились в версии 2.5 (!) для браузера Firefox 7.**

Ирония в том, что версия 2.44 -- это последняя версия, в которой нативные события ещё обновлялись. Начиная с версии 2.45 мы фактически прекратили работу над ними и полностью сосредоточились на том, чтобы довести до ума синтезированные события. [Которые нисколько не хуже, а может быть даже лучше](http://barancev.github.io/native-vs-synthesized/).
