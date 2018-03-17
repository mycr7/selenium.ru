---
layout: page
title: 'Selenium: как отключить same origin policy в браузере Google Chrome'
joomla_id: 13
joomla_url: selenium-google-chrome-same-origin-policy
date: 2011-01-18 11:10:00.000000000 +03:00
author: Алексей Баранцев
excerpt: |-
  <p>{tortags,13,1}</p>
  <p><strong>Автор: <a href="http://software-testing.ru/about/authors/9-barancev">Алексей Баранцев</a></strong></p>
  <div class="warning">Внимание: Эта статья относится к версиям Selenium меньше 2.12, в последних версиях опция --disable-web-security для браузера Chrome установлена по умолчанию.</div>
  <p>Недавно ученики моего курса <a href="http://software-testing.ru/trainings/schedule?&amp;task=3&amp;cid=1">Программирование для тестировщиков</a> пришли ко мне с жалобой – тесты, которые у них успешно выполнялись в браузерах FireFox и Internetr Explorer по непонятной причине падали в браузере Google Chrome. Когда я посмотрел, что происходит, мне показалось, что я вернулся лет на пять в прошлое – налицо были все симптомы проявления same origin policy, с которым давно уже все научились бороться при использовании браузеров Internet Explorer и FireFox.</p>
category: Статьи
---
<p>{tortags,13,1}</p>
<p><strong>Автор: <a href="http://software-testing.ru/about/authors/9-barancev">Алексей Баранцев</a></strong></p>
<div class="warning">Внимание: Эта статья относится к версиям Selenium меньше 2.12, в последних версиях опция --disable-web-security для браузера Chrome установлена по умолчанию.</div>
<p>Недавно ученики моего курса <a href="http://software-testing.ru/trainings/schedule?&amp;task=3&amp;cid=1">Программирование для тестировщиков</a> пришли ко мне с жалобой – тесты, которые у них успешно выполнялись в браузерах FireFox и Internetr Explorer по непонятной причине падали в браузере Google Chrome. Когда я посмотрел, что происходит, мне показалось, что я вернулся лет на пять в прошлое – налицо были все симптомы проявления same origin policy, с которым давно уже все научились бороться при использовании браузеров Internet Explorer и FireFox.</p><p>Страшные слова <a href="http://www.w3.org/Security/wiki/Same_Origin_Policy" target="_blank">same origin policy</a> знакомы практически каждому тестировщику, который начал использовать Selenium достаточно давно, когда ещё не было режимов запуска *iehta и *chrome. Производители браузеров, заботясь о защищенности пользователей, изобретают различные средства борьбы с уязвимостями в веб-приложениях. И как одно из средств защиты от <a href="http://en.wikipedia.org/wiki/Cross-site_scripting" target="_blank">XSS-уязвимостей</a>, был придуман запрет в JavaScript-коде получать данные с любых сайтов, за исключением того, с которого был первоначально загружен этот самый JavaScript-код. Вот он-то и называется same origin policy.</p>
<p>Мы не будем здесь обсуждать, <a href="http://www.simplecoding.org/xss-i-same-origin-policy.html" target="_blank">насколько этот запрет эффективен как средство защиты</a>. Важно то, что его наличие <a href="http://seleniumhq.org/docs/05_selenium_rc.html#the-same-origin-policy" target="_blank">вызывает проблемы при выполнении тестов при помощи Selenium</a>. Дело в том, что ядро Selenium реализовано на языке JavaScript. При запуске теста ядро загружается в браузер, и всё работает хорошо до тех пор, пока в процессе выполнения теста не возникает необходимость перейти на другой сайт – браузер немедленно замечает это "опасное" действие и блокирует его.</p>
<p>Чтобы обойти это ограничение, были реализованы специальные режимы запуска браузеров с отключеной защитой, это режим *chrome для браузера FireFox и режим *iehta для браузера Internet Explorer.</p>
<p>А вот для браузера Google Chrome существует только один единственный режим запуска *googlechrome, и в этом режиме он запускается с включенными средствами защиты.</p>
<p>Но всё-таки способ отключения защиты существует, решение удалось найти, и я хочу поделиться с вами этой информацией. Ключ к решению заключается в <a href="http://blog.mfabrik.com/2010/11/29/disabling-cross-domain-security-check-for-ajax-development-in-google-chrome/" target="_blank">использовании опции --disable-web-security</a>. Вопрос лишь в том, как заставить Selenium запустить браузер с этой опцией.</p>
<p>Если вы пишете на языке Java и наследуете свой класс от SeleneseTestCase или SeleneseTestBase, инициализация браузера скорее всего выполняется обращением к методу setUp:</p>
<pre xml:lang="java">setUp("http://www.example.com/", "*googlechrome");</pre>
<p>Но для запуска с отключенной защитой такой способ не годится, необходимо сделать свой собственный метод инициализации браузера. Конечно же за основу можно взять тот самый стандартный метод setUp, который выглядит следующим образом (это вариант с наибольшим набором параметров):</p>
<pre xml:lang="java">public void setUp(String url, String browserString, int port) {
    if  (url == null) {
        url = "http://localhost:" + port;
    }
    selenium = new DefaultSelenium("localhost", port, browserString, url);
    selenium.start();
}</pre>
<p>Как несложно видеть, здесь у объекта selenium вызывается метод start без параметров. А нам нужно вместо этого вызвать другой метод start, принимающий на вход строковый параметр, через который можно передать указания, пользуясь которыми Selenium Server построит полную строку запуска, включая опции браузера.</p>
<p>Указание отключить защиту в Google Chrome можно передать двумя способами, либо так:</p>
<pre xml:lang="java">selenium.start("commandLineFlags=--disable-web-security");</pre>
<p>либо вот так:</p>
<pre xml:lang="java">selenium.start("mode=disableSecurity")</pre>
<p>При этом разработчики в комментариях неявно намекают на то, что второй способ предпочтительнее, но я рекомендую использовать первый способ. Причина в том, что второй способ конфликтует с браузером Safari при запуске в режиме *safari (если честно, чисто теоретически я бы ожидал с большей вероятностью возникновения конфликтов при первом способе, но практика показывает обратное).</p>
<p>Итак, создаём свой собственный метод и везде, где нужно, используем его вместо стандартного метода setUp:</p>
<pre xml:lang="java">public void setUpWithDisabledSecurity(String url, String browserString, int  port) {
    if (url == null) {
        url = "http://localhost:" +  port;
    }
    selenium = new DefaultSelenium("localhost", port,  browserString, url);
    selenium.start("commandLineFlags=--disable-web-security");
}</pre>
<p>Вот и всё, same origin policy повержен!</p>
<h4 style="text-align: center;"><a href="http://software-testing.ru/forum/topic/18440/">Обсудить в форуме</a></h4>
