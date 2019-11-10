---
layout: page
title: Ожидание событий в Selenium RC, часть 1
redirect_from: /articles/8-selenium-waiting-events-1.html
date: 2010-08-11 07:56:00.000000000 +04:00
author: Алексей Баранцев
teaser: Оставим на время в стороне тему снятия скриншотов в Selenium, поговорим об ожидании тех или иных событий, то есть о методах, название которых содержит слово wait. В этой заметке мы сделаем расширение стандартного класса DefaultSelenium, которое облегчит работу с классическими (не-AJAX) приложениями, сократив количество рутинного кода, предназначенного для ожидания загрузки страниц
category: Статьи
---
Оставим на время в стороне тему [снятия скриншотов в Selenium](/articles/9-selenium-remote-screenshots), поговорим об ожидании тех или иных событий, то есть о методах, название которых содержит слово wait. В этой заметке мы сделаем расширение стандартного класса DefaultSelenium, которое облегчит работу с классическими (не-AJAX) приложениями, сократив количество рутинного кода, предназначенного для ожидания загрузки страниц.

## Подготовка расширения

Расширять возможности Selenium RC на этот раз мы будем достаточно простым способом, без добавления новых команд в ядро, только при помощи методов-обёрток для уже существующих команд на клиентской стороне. Всё будет демонстрироваться на примере языка Java, для других языков расширение выполняется аналогично.

Для начала мы сделаем новый класс `WaitingSelenium`, унаследованный от `DefaultSelenium`, именно туда, в этот новый класс мы будем добавлять новые методы:

{% highlight java %}
public class WaitingSelenium extends DefaultSelenium {
  public  WaitingSelenium(
    String serverHost, int serverPort, String browserStartCommand,  String browserURL)
  {
    super(serverHost, serverPort,  browserStartCommand, browserURL);
  }
}
{% endhighlight %}

Затем мы немного модифицируем класс `SeleneseTestNgHelper`, чтобы вместо стандартной реализации `DefaultSelenium` инициализировалась наша, расширенная. Если вы не используете TestNG, нужно будет внести аналогичные изменения туда, где создается клиент Selenium RC. Там должна появиться вот такая строчка:

{% highlight java %}
selenium = new WaitingSelenium(server, port, browserString, url);
{% endhighlight %}

Теперь можно перейти к делу – начинаем добавлять новые методы в класс `WaitingSelenium`.

## waitForPageToLoad
 
Если вы тестируете не-AJAX приложение, наверняка у вас в коде часто встречается команда `waitForPageToLoad` – после каждого действия, приводящего к отправке браузером запроса на сервер, нужно дожидаться, пока браузер получит ответ и отрисует страницу. Сейчас мы немного поработаем над повышением удобства использования этой команды.

Думаю, что у каждого, кто начинал работать с Selenium RC, возникал закономерный вопрос – почему метод `waitForPageToLoad` принимает параметр типа String, хотя по смыслу туда передаётся число (время ожидания в миллисекундах):

{% highlight java %}
selenium.waitForPageToLoad("30000");
{% endhighlight %}

Давайте исправим это недоразумение, сделаем дополнительный метод, который принимает числовой параметр, и сам преобразует его в строку:

{% highlight java %}
public void waitForPageToLoad(int timeout) {
  waitForPageToLoad("" +  timeout);
}
{% endhighlight %}

Теперь обращение к этому методу будет выглядеть более осмысленно:

{% highlight java %}
selenium.waitForPageToLoad(30000);
{% endhighlight %}

Аналогичные методы-преобразователи можно сделать для других команд ожидания: `waitForFrameToLoad`, `waitForPopUp` и `waitForCondition`.

Второе неудобство с использованием этой команды заключается в том, что в неё обязательно нужно передавать параметр. Сейчас мы сделаем модификацию без параметров, которая будет ожидать в течение некоторого времени “по умолчанию”, а также методы для установки этого “дефолтного” таймаута:

{% highlight java %}
private int defaultTimeoutWaitForPageToLoad = 30000;

public int getDefaultTimeoutWaitForPageToLoad() {
  return  defaultTimeoutWaitForPageToLoad;
}

public void setDefaultTimeoutWaitForPageToLoad(int timeout) {
  this.defaultTimeoutWaitForPageToLoad = timeout;
}

public void waitForPageToLoad() {
  waitForPageToLoad(getDefaultTimeoutWaitForPageToLoad());
}
{% endhighlight %}

И теперь больше не нужно указывать время ожидания при каждом обращении, достаточно настроить его один раз где-нибудь в начале теста (а если устраивает дефолтное значение, то и вообще ничего настраивать не надо):

{% highlight java %}
selenium.waitForPageToLoad();
{% endhighlight %}

Впрочем, достаточно возиться с этим методом `waitForPageToLoad`, давайте лучше спрячем его совсем.


## clickAndWait
 
Если вы пользовались Selenium IDE, вы могли заметить, что там есть две похожие команды – `click` и `clickAndWait`. На самом деле такая [парная команда с ожиданием](http://seleniumhq.org/docs/04_selenese_commands.html#the-andwait-commands) имеется для всех команд-действий (actions), кроме команды open, которая ждёт автоматически.

А вот в Selenium RC таких парных команд почему-то нет. Не сделали. Ну и что? Давайте добавим их сами, причём сделаем даже в двух вариантах – с параметром, задающим время ожидания, и без параметра, чтобы использовался таймаут “по умолчанию”.

{% highlight java %}
public void clickAndWait(String locator, int timeout) {
  click(locator);
  waitForPageToLoad(timeout);
}

public void clickAndWait(String locator) {
  click(locator);
  waitForPageToLoad();
}
{% endhighlight %}

Ну и конечно аналогичные методы можно реализовать для всех команд-действий, которые вы используете в своих тестах.

На этом пока всё. А в следующей заметке мы постараемся расширить возможности для работы с приложениями, использующими AJAX, ибо таких возможностей в Selenium RC явно недостаточно.

В приложении находится проект Eclipse, содержащий исходный код расширения `WaitingSelenium` и модифицированный класс `SeleneseTestNgHelper`, использующий это расширение: [WaitingSelenium.zip](http://software-testing.ru/files/library/barancev/waiting_selenium/WaitingSelenium.zip)
