---
layout: page
title: Баги не только в программах, но и в новостях
redirect_from: /blog/140-buggy-selenium-news.html
date: 2015-06-09 13:08:53.000000000 +03:00
author: Алексей Баранцев
teaser: "Новости надо читать с большой осторожностью, потому что там тоже есть баги. Иногда вроде бы уважаемая компания опубликует что-нибудь этакое..."
category: Блог
---
<p>Новости надо читать с большой осторожностью, потому что там тоже есть баги. Иногда вроде бы уважаемая компания опубликует что-нибудь этакое...</p>
<p>Наткнулся недавно на <a href="http://smartbear.com/all-resources/articles/what-s-new-in-selenium/">вот эту статью на сайте SmartBear</a>, и обнаружил там такую "новость":</p>
<p><em>"As of version 2.44, when you do something like window.click('button') in FireFox, you are actually causing the browser to fire a real click event. FireFox automation is more realistic than it has ever been."</em></p>
<p>Это должно означать, что начиная с версии 2.44 в Selenium якобы появились "нативные события", которые более лучше, чем синтезированные.</p>
<p><img src="images/blog/o-rly.png" border="0" style="border: 1px solid black;" /></p>
<p><strong>Разумеется, это неправда. Нативные события впервые появились в версии 2.5 (!) для браузера Firefox 7.</strong></p>
<p>Ирония в том, что версия 2.44 -- это последняя версия, в которой нативные события ещё обновлялись. Начиная с версии 2.45 мы фактически прекратили работу над ними и полностью сосредоточились на том, чтобы довести до ума синтезированные события. <a href="http://barancev.github.io/native-vs-synthesized/">Которые нисколько не хуже, а может быть даже лучше</a>.</p>
