---
layout: page
title: Ожидание событий в Selenium RC, часть 1
joomla_id: 8
joomla_url: selenium-waiting-events-1
date: 2010-08-11 07:56:00.000000000 +04:00
author: Алексей Баранцев
excerpt: |-
  <p>{tortags,8,1}</p>
  <p><strong>Автор: <a href="http://software-testing.ru/about/authors/9-barancev">Алексей Баранцев</a></strong></p>
  <p>Оставим на время в стороне тему <a href="articles/9-selenium-remote-screenshots">снятия скриншотов в Selenium</a>, поговорим об ожидании тех или иных событий, то есть о методах, название которых содержит слово wait. В этой заметке мы сделаем расширение стандартного класса DefaultSelenium, которое облегчит работу с классическими (не-AJAX) приложениями, сократив количество рутинного кода, предназначенного для ожидания загрузки страниц.</p>
category: Статьи
---
<p>{tortags,8,1}</p>
<p><strong>Автор: <a href="http://software-testing.ru/about/authors/9-barancev">Алексей Баранцев</a></strong></p>
<p>Оставим на время в стороне тему <a href="articles/9-selenium-remote-screenshots">снятия скриншотов в Selenium</a>, поговорим об ожидании тех или иных событий, то есть о методах, название которых содержит слово wait. В этой заметке мы сделаем расширение стандартного класса DefaultSelenium, которое облегчит работу с классическими (не-AJAX) приложениями, сократив количество рутинного кода, предназначенного для ожидания загрузки страниц.</p><h3>Подготовка расширения</h3>
<p>Расширять возможности Selenium RC на этот раз мы будем достаточно простым способом, без добавления новых команд в ядро, только при помощи методов-обёрток для уже существующих команд на клиентской стороне. Всё будет демонстрироваться на примере языка Java, для других языков расширение выполняется аналогично.</p>
<p>Для начала мы сделаем новый класс WaitingSelenium, унаследованный от DefaultSelenium, именно туда, в этот новый класс мы будем добавлять новые методы:</p>
<pre xml:lang="java">public class WaitingSelenium extends DefaultSelenium {
    public  WaitingSelenium(String serverHost, int serverPort, String browserStartCommand,  String browserURL) {
        super(serverHost, serverPort,  browserStartCommand, browserURL);
    }
}</pre>
<p>Затем мы немного модифицируем класс SeleneseTestNgHelper, чтобы вместо стандартной реализации DefaultSelenium инициализировалась наша, расширенная. Если вы не используете TestNG, нужно будет внести аналогичные изменения туда, где создается клиент Selenium RC. Там должна появиться вот такая строчка:</p>
<pre xml:lang="java">selenium = new WaitingSelenium(server, port, browserString, url);</pre>
<p>Теперь можно перейти к делу – начинаем добавлять новые методы в класс WaitingSelenium.</p>
<h3>waitForPageToLoad</h3>
<p>Если вы тестируете не-AJAX приложение, наверняка у вас в коде часто встречается команда waitForPageToLoad – после каждого действия, приводящего к отправке браузером запроса на сервер, нужно дожидаться, пока браузер получит ответ и отрисует страницу. Сейчас мы немного поработаем над повышением удобства использования этой команды.</p>
<p>Думаю, что у каждого, кто начинал работать с Selenium RC, возникал закономерный вопрос – почему метод waitForPageToLoad принимает параметр типа String, хотя по смыслу туда передаётся число (время ожидания в миллисекундах):</p>
<pre xml:lang="java">selenium.waitForPageToLoad("30000");</pre>
<p>Давайте исправим это недоразумение, сделаем дополнительный метод, который принимает числовой параметр, и сам преобразует его в строку:</p>
<pre xml:lang="java">public void waitForPageToLoad(int timeout) {
    waitForPageToLoad("" +  timeout);
}</pre>
<p>Теперь обращение к этому методу будет выглядеть более осмысленно:</p>
<pre xml:lang="java">selenium.waitForPageToLoad(30000);</pre>
<p>Аналогичные методы-преобразователи можно сделать для других команд ожидания: waitForFrameToLoad, waitForPopUp и waitForCondition.</p>
<p>Второе неудобство с использованием этой команды заключается в том, что в неё обязательно нужно передавать параметр. Сейчас мы сделаем модификацию без параметров, которая будет ожидать в течение некоторого времени “по умолчанию”, а также методы для установки этого “дефолтного” таймаута:</p>
<pre xml:lang="java">private int defaultTimeoutWaitForPageToLoad = 30000;

public int getDefaultTimeoutWaitForPageToLoad() {
    return  defaultTimeoutWaitForPageToLoad;
}

public void setDefaultTimeoutWaitForPageToLoad(int timeout) {
    this.defaultTimeoutWaitForPageToLoad = timeout;
}

public void waitForPageToLoad() {
    waitForPageToLoad(getDefaultTimeoutWaitForPageToLoad());
}</pre>
<p>И теперь больше не нужно указывать время ожидания при каждом обращении, достаточно настроить его один раз где-нибудь в начале теста (а если устраивает дефолтное значение, то и вообще ничего настраивать не надо):</p>
<pre xml:lang="java">selenium.waitForPageToLoad();</pre>
<p>Впрочем, достаточно возиться с этим методом waitForPageToLoad, давайте лучше спрячем его совсем.</p>
<h3>clickAndWait</h3>
<p>Если вы пользовались Selenium IDE, вы могли заметить, что там есть две похожие команды – click и clickAndWait. На самом деле такая <a href="http://seleniumhq.org/docs/04_selenese_commands.html#the-andwait-commands" target="_blank">парная команда с ожиданием</a> имеется для всех команд-действий (actions), кроме команды open, которая ждёт автоматически.</p>
<p>А вот в Selenium RC таких парных команд почему-то нет. Не сделали. Ну и что? Давайте добавим их сами, причём сделаем даже в двух вариантах – с параметром, задающим время ожидания, и без параметра, чтобы использовался таймаут “по умолчанию”.</p>
<pre xml:lang="java">public void clickAndWait(String locator, int timeout) {
    click(locator);
    waitForPageToLoad(timeout);
}

public void clickAndWait(String locator) {
    click(locator);
    waitForPageToLoad();
}</pre>
<p>Ну и конечно аналогичные методы можно реализовать для всех команд-действий, которые вы используете в своих тестах.</p>
<p>На этом пока всё. А в следующей заметке мы постараемся расширить возможности для работы с приложениями, использующими AJAX, ибо таких возможностей в Selenium RC явно недостаточно.</p>
<p>В приложении находится проект Eclipse, содержащий исходный код расширения WaitingSelenium и модифицированный класс SeleneseTestNgHelper, использующий это расширение: <a href="http://software-testing.ru/files/library/barancev/waiting_selenium/WaitingSelenium.zip">WaitingSelenium.zip</a></p>
<h4 style="text-align: center;"><a href="http://software-testing.ru/forum/topic/17496/">Обсудить в форуме</a></h4>
