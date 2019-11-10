---
layout: page
title: 'Selenium: ожидание завершения всех AJAX-запросов'
redirect_from: /articles/17-waiting-for-ajax.html
date: 2011-01-11 14:18:14.000000000 +03:00
author: Алексей Баранцев
teaser: В последнее время развелось очень много различных AJAX-приложений. По сути автоматизация тестирования такого приложения не отличается от автоматизации тестирования обычного WEB-приложения, но есть несколько тонкостей. Одна из тонкостей — это как раз ожидание завершения всех AJAX-запросов. Например, если отметка некого checkbox'а на странице вызывает обновление какого-нибудь select'a по AJAX-запросу, то тест, который сразу после отметки выбирает конкретный option, свалится, т.к. этого option'a там не будет. А всё потому, что сам тест выполняется намного быстрее чем AJAX-запрос на обновление списка. В данном случае у автоматизатора есть несколько выходов
category: Статьи
---
*Это гостевая статья, написанная Виталием Помазенковым*

В последнее время развелось очень много различных AJAX-приложений. По сути автоматизация тестирования такого приложения не отличается от автоматизации тестирования обычного WEB-приложения, но есть несколько тонкостей. Одна из тонкостей — это как раз ожидание завершения всех AJAX-запросов. Например, если отметка некого checkbox'а на странице вызывает обновление какого-нибудь select'a по AJAX-запросу, то тест, который сразу после отметки выбирает конкретный option, свалится, т.к. этого option'a там не будет. А всё потому, что сам тест выполняется намного быстрее чем AJAX-запрос на обновление списка.

В данном случае у автоматизатора есть несколько выходов.

**1. Поставить sleep после отметки checkbox'а.**

Это самое плохое и, к сожалению, чаще всего применяемое решение. Нам заранее не известно, сколько времени займёт выполнение AJAX-запроса, соответственно придётся задавать время ожидания исходя из минимально достаточного для большинства случаев. Например, 5 секунд. Когда таких ожиданий по 5 секунд наберётся достаточно много, наши тесты начнут выполняться очень долго, даже тогда, когда все AJAX-запросы выполняются быстро. Кроме того, иногда по разным причинам время выполнения AJAX-запроса может оказаться 5.2 секунды, в таких случаях мы будем получать ложные падения тестов, что тоже плохо.

**2. Воспользоваться классом [Wait](http://release.seleniumhq.org/selenium-remote-control/0.9.2/doc/java/com/thoughtworks/selenium/Wait.html) и ждать пока [Selenium#isElementPresent](http://release.seleniumhq.org/selenium-remote-control/0.9.2/doc/java/com/thoughtworks/selenium/Selenium.html#isElementPresent%28java.lang.String%29) не вернёт true для нужного option'а.**

Этот способ уже лучше, но всё равно не должен применяться, в будущем напишу подробно почему. Лучше вместо класса Wait использовать метод Selenium#waitForCondition, в котором и ждать появления требуемого элемента.

**3. Каким-то образом после отметки checkbox'а дождаться завершения всех AJAX-запросов и только после этого выбирать option.**

Этот способ рассмотрим более подробно, т.к. он является достаточно универсальным и простым с точки зрения автоматизатора.

В большинстве WEB-приложений для работы с AJAX используются специализированные библиотеки (jQuery, Prototype, Dojo и т.д.), предоставляющие разработчику более высокий уровень абстракции, чем стандартное API, а соответственно и большую гибкость.

Для того, чтобы в Selenium-тесте дождаться завершения всех AJAX-запросов, необходимо научиться следить за этими запросами глобально. В стандартном API нет возможности установки глобальных перехватчиков, но зато практически в каждой из сторонних библиотек такая возможность есть, хотя везде это делается по-своему. Вот пример, как можно дождаться завершения всех AJAX-запросов при использовании библиотеки jQuery:

{% highlight javascript %}
/**
 * Waits for all active jQuery AJAX requests to finish.
 *
 * @param timeout Timeout in milliseconds.
 * @throws SeleniumError If timeout is reached.
 */
Selenium.prototype.doWaitForJqueryAjaxRequests = function(timeout) {
  return Selenium.decorateFunctionWithTimeout(function() {
    return selenium.browserbot.getUserWindow().jQuery.active == 0;
  }, timeout);
};
{% endhighlight %}

Здесь мы просто оборачиваем необходимое нам условие (количество активных AJAX-запросов равно нулю) в метод Selenium#decorateFunctionWithTimeout, который будет ожидать выполнения данного условия в течение указанного в timeout времени, и если дождётся, то метод будет успешно завершён, иначе будет выкинуто исключение SeleniumError.

Если описать на мета-языке то, что нам требуется для создания универсального метода ожидания, то получится примерно следующее:

* Определить, какие библиотеки используются для работы с AJAX.
* Подождать завершения всех AJAX-запросов для каждой из используемых библиотек.

Всё просто, осталось реализовать это на JavaScript и подключить в качестве расширения к Selenium RC либо к Selenium IDE, кому как нравится. При использовании Selenium RC для большей универсальности можно подгружать код расширения с помощью метода DefaultSelenium#setExtensionJs.

Вот готовая реализация (поддержаны jQuery, Prototype и Dojo):

{% highlight javascript %}
/**
 * Waits for all active AJAX requests to finish during specified timeout.
 * Works only for AJAX requests which are instantiated using one of the following frameworks:
 * jQuery, Prototype, Dojo. Don't work (immediately returns without any errors)
 * if standard AJAX API or one of other frameworks is used to send XML HTTP request.
 *
 * @param timeout Timeout in milliseconds.
 * @throws SeleniumError If timeout is reached.
 */
Selenium.prototype.doWaitForAjaxRequests = function(timeout) {
    return Selenium.decorateFunctionWithTimeout(function() {

        var userWindow = selenium.browserbot.getUserWindow();
        var isJqueryComplete = typeof(userWindow.jQuery) != 'function'
            || userWindow.jQuery.active == 0;
        var isPrototypeComplete = typeof(userWindow.Ajax) != 'function'
            || userWindow.Ajax.activeRequestCount == 0;
        var isDojoComplete = typeof(userWindow.dojo) != 'function'
            || userWindow.dojo.io.XMLHTTPTransport.inFlight.length == 0;
        return isJqueryComplete &amp;&amp; isPrototypeComplete && isDojoComplete;
    }, timeout);
};
{% endhighlight %}

Если для написания тестов используется не [Selenese](http://seleniumhq.org/docs/04_selenese_commands.html), а нормальный язык программирования, то для того, чтобы можно было воспользоваться новым методом, необходимо расширить используемый драйвер, добавив в него этот метод.

Теперь мы можем легко заменить такой вот код теста:

{% highlight java %}
...
selenium.check("name=enableBender");
sleep(5000);
selenium.select("name=mode", "label=Kill all humans");
...
{% endhighlight %}

На такой:

{% highlight java %}
...
selenium.check("name=enableBender");
selenium.waitForAjaxRequests(60000);
selenium.select("name=mode", "label=Kill all humans");
...
{% endhighlight %}

И тесты будут выполняться со скоростью, равной скорости ответа сервера, т.е. без лишних задержек.

Для некоторых проектов, где AJAX-запросы начинают выполняться сразу после загрузки страницы (да, бывают и такие), рекомендую перегрузить методы waitForPageToLoad, waitForFrameToLoad и waitForPopUp, добавив в них последним вызовом waitForAjaxRequests, чтобы не дергать его постоянно в тестах.

Напоследок ещё раз повторюсь, что в стандартном API нет возможности установки глобальных перехватчиков AJAX-запросов, поэтому данный метод не будет работать, если разработчики используют стандартный API напрямую. Благо, что в более-менее серьёзных проектах так не поступают. Но вполне возможно, что в каком-нибудь проекте применяется собственная обёртка вокруг стандартного API, в таком случае надо будет просто поддержать эту обёртку в user-extensions.js.
