---
layout: page
title: 'Selenium: как отключить same origin policy в браузере Google Chrome'
redirect_from: /articles/13-selenium-google-chrome-same-origin-policy.html
date: 2011-01-18 11:10:00.000000000 +03:00
author: Алексей Баранцев
teaser: Недавно ученики моего курса Программирование для тестировщиков пришли ко мне с жалобой – тесты, которые у них успешно выполнялись в браузерах FireFox и Internet Explorer по непонятной причине падали в браузере Google Chrome. Когда я посмотрел, что происходит, мне показалось, что я вернулся лет на пять в прошлое – налицо были все симптомы проявления same origin policy, с которым давно уже все научились бороться при использовании браузеров Internet Explorer и FireFox
category: Статьи
---
Недавно ученики моего курса [Программирование для тестировщиков](https://software-testing.ru/edu/schedule/1) пришли ко мне с жалобой – тесты, которые у них успешно выполнялись в браузерах FireFox и Internetr Explorer по непонятной причине падали в браузере Google Chrome. Когда я посмотрел, что происходит, мне показалось, что я вернулся лет на пять в прошлое – налицо были все симптомы проявления same origin policy, с которым давно уже все научились бороться при использовании браузеров Internet Explorer и FireFox.

Страшные слова [same origin policy](http://www.w3.org/Security/wiki/Same_Origin_Policy) знакомы практически каждому тестировщику, который начал использовать Selenium достаточно давно, когда ещё не было режимов запуска `*iehta` и `*chrome`. Производители браузеров, заботясь о защищенности пользователей, изобретают различные средства борьбы с уязвимостями в веб-приложениях. И как одно из средств защиты от [XSS-уязвимостей](http://en.wikipedia.org/wiki/Cross-site_scripting), был придуман запрет в JavaScript-коде получать данные с любых сайтов, за исключением того, с которого был первоначально загружен этот самый JavaScript-код. Вот он-то и называется same origin policy.

Мы не будем здесь обсуждать, [насколько этот запрет эффективен как средство защиты](http://www.simplecoding.org/xss-i-same-origin-policy.html). Важно то, что его наличие [вызывает проблемы](http://seleniumhq.org/docs/05_selenium_rc.html#the-same-origin-policy) при выполнении тестов при помощи Selenium. Дело в том, что ядро Selenium реализовано на языке JavaScript. При запуске теста ядро загружается в браузер, и всё работает хорошо до тех пор, пока в процессе выполнения теста не возникает необходимость перейти на другой сайт – браузер немедленно замечает это "опасное" действие и блокирует его.

Чтобы обойти это ограничение, были реализованы специальные режимы запуска браузеров с отключеной защитой, это режим `*chrome` для браузера FireFox и режим `*iehta` для браузера Internet Explorer.

А вот для браузера Google Chrome существует только один единственный режим запуска `*googlechrome`, и в этом режиме он запускается с включенными средствами защиты.

Но всё-таки способ отключения защиты существует, решение удалось найти, и я хочу поделиться с вами этой информацией. Ключ к решению заключается в [использовании опции --disable-web-security](http://blog.mfabrik.com/2010/11/29/disabling-cross-domain-security-check-for-ajax-development-in-google-chrome/). Вопрос лишь в том, как заставить Selenium запустить браузер с этой опцией.

Если вы пишете на языке Java и наследуете свой класс от `SeleneseTestCase` или `SeleneseTestBase`, инициализация браузера скорее всего выполняется обращением к методу `setUp`:

{% highlight java %}
setUp("http://www.example.com/", "*googlechrome");
{% endhighlight %}

Но для запуска с отключенной защитой такой способ не годится, необходимо сделать свой собственный метод инициализации браузера. Конечно же за основу можно взять тот самый стандартный метод `setUp`, который выглядит следующим образом (это вариант с наибольшим набором параметров):

{% highlight java %}
public void setUp(String url, String browserString, int port) {
  if  (url == null) {
    url = "http://localhost:" + port;
  }
  selenium = new DefaultSelenium("localhost", port, browserString, url);
  selenium.start();
}
{% endhighlight %}

Как несложно видеть, здесь у объекта `selenium` вызывается метод `start` без параметров. А нам нужно вместо этого вызвать другой метод `start`, принимающий на вход строковый параметр, через который можно передать указания, пользуясь которыми Selenium Server построит полную строку запуска, включая опции браузера.

Указание отключить защиту в Google Chrome можно передать двумя способами, либо так:

{% highlight java %}
selenium.start("commandLineFlags=--disable-web-security");
{% endhighlight %}

либо вот так:

{% highlight java %}
selenium.start("mode=disableSecurity")
{% endhighlight %}

При этом разработчики в комментариях неявно намекают на то, что второй способ предпочтительнее, но я рекомендую использовать первый способ. Причина в том, что второй способ конфликтует с браузером Safari при запуске в режиме `*safari` (если честно, чисто теоретически я бы ожидал с большей вероятностью возникновения конфликтов при первом способе, но практика показывает обратное).

Итак, создаём свой собственный метод и везде, где нужно, используем его вместо стандартного метода `setUp`:

{% highlight java %}
public void setUpWithDisabledSecurity(String url, String browserString, int  port) {
    if (url == null) {
        url = "http://localhost:" +  port;
    }
    selenium = new DefaultSelenium("localhost", port,  browserString, url);
    selenium.start("commandLineFlags=--disable-web-security");
}
{% endhighlight %}

Вот и всё, same origin policy повержен!
