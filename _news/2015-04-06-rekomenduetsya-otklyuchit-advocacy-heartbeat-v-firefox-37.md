---
layout: page
title: Рекомендуется отключить Advocacy/heartbeat в Firefox 37
joomla_id: 131
joomla_url: rekomenduetsya-otklyuchit-advocacy-heartbeat-v-firefox-37
date: 2015-04-06 14:27:11.000000000 +03:00
author: Super User
excerpt: |-
  <p><a href="https://www.facebook.com/groups/selenium.ru/" target="_blank">Оригинальная публикация в группе в Facebook</a></p>
  <p>FYI: В версии Firefox 37 появилась новая "фича", которая может помешать выполнению автотестов: <a href="https://wiki.mozilla.org/Advocacy/heartbeat" target="_blank" rel="nofollow">https://wiki.mozilla.org/Advocacy/heartbeat</a></p>
  <p>Каждый день некоторое количество случайно выбранных пользователей при запуске браузера видят перед собой панельку, где предлагается оценить качество браузера по пятибалльной шкале.</p>
  <p>Если у вас достаточно большой тестовый стенд и браузеры запускаются часто -- вы в зоне риска, время от времени тесты будут натыкаться на эту панельку и сбоить.</p>
  <div class="text_exposed_show">
  <p>Поэтому до выхода следующей версии Selenium рекомендуется при запуске FirefoxDriver передавать в качестве параметра профиль, в котором указана пустая строка в качестве значения настройки "browser.selfsupport.url".</p>
  </div>
category: Новости
---
<p><a href="https://www.facebook.com/groups/selenium.ru/" target="_blank">Оригинальная публикация в группе в Facebook</a></p>
<p>FYI: В версии Firefox 37 появилась новая "фича", которая может помешать выполнению автотестов: <a href="https://wiki.mozilla.org/Advocacy/heartbeat" target="_blank" rel="nofollow">https://wiki.mozilla.org/Advocacy/heartbeat</a></p>
<p>Каждый день некоторое количество случайно выбранных пользователей при запуске браузера видят перед собой панельку, где предлагается оценить качество браузера по пятибалльной шкале.</p>
<p>Если у вас достаточно большой тестовый стенд и браузеры запускаются часто -- вы в зоне риска, время от времени тесты будут натыкаться на эту панельку и сбоить.</p>
<div class="text_exposed_show">
<p>Поэтому до выхода следующей версии Selenium рекомендуется при запуске FirefoxDriver передавать в качестве параметра профиль, в котором указана пустая строка в качестве значения настройки "browser.selfsupport.url".</p>
</div>
