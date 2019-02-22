---
layout: page
title: Проблема совместимости с Firefox 47 решена
redirect_from: /news/177-firefox47-issue-resolved.html
date: 2016-06-30 07:48:27.000000000 +03:00
author: Алексей Баранцев
image:
  title: /images/news/firefox.jpg
  thumb: /images/news/firefox.jpg
teaser: "Вышла обновлённая версия браузера Firefox 47.0.1, в которой устранена
  проблема совместимости с Selenium WebDriver. Правда, обновлением одного только
  браузера дело не обошлось, на стороне Selenium тоже пришлось внести некоторые изменения."
category: Новости
---
<p><img src="images/news/firefox.jpg" border="0" width="500" /></p>
<p>Вышла обновлённая версия браузера Firefox 47.0.1, в которой устранена проблема совместимости с Selenium WebDriver.</p>
<p>Правда, обновлением одного только браузера дело не обошлось, на стороне Selenium тоже пришлось внести некоторые изменения.</p>
<p>Поэтому Selenium тоже надо обновить, необходимы <a href="http://selenium-release.storage.googleapis.com/index.html?path=2.53/">для Java версия 2.53.1</a> (центральный репозиторий Maven как всегда обновится с некоторой задержкой), <a href="https://www.nuget.org/packages/Selenium.WebDriver">для C# версия 2.53.1</a>, <a href="https://pypi.python.org/pypi/selenium">для Python версия 2.53.6</a>, <a href="https://rubygems.org/gems/selenium-webdriver">для Ruby версия 2.53.4</a>, <a href="https://www.npmjs.com/package/selenium-webdriver">для JavaScript версия 2.53.4</a>.</p>
