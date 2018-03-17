---
layout: page
title: Ожидание событий в Selenium RC, часть 2 -- AJAX
joomla_id: 11
joomla_url: selenium-waiting-events-2
date: 2010-08-18 10:06:00.000000000 +04:00
author: Алексей Баранцев
excerpt: |-
  <p>{tortags,11,1}</p>
  <p><strong>Автор: <a href="http://iso.software-testing.ru/about/authors/9-barancev">Алексей Баранцев</a></strong></p>
  <p>В <a href="articles/8-selenium-waiting-events-1">предыдущей заметке</a> мы сделали расширение Selenium RC, упрощающее операции, связанные с ожиданием загрузки страниц веб-приложения. Но те, кто занимается тестированием AJAX-приложений, с этими операциями сталкиваются редко, им приходится работать с другими событиями – появление и исчезновение элементов интерфейса, а также изменение их свойств (таких как, например, видимость или цвет). Поэтому сейчас мы добавим в наше расширение набор операций, предназначенных для ожидания таких событий.</p>
category: Статьи
---
<p>{tortags,11,1}</p>
<p><strong>Автор: <a href="http://iso.software-testing.ru/about/authors/9-barancev">Алексей Баранцев</a></strong></p>
<p>В <a href="articles/8-selenium-waiting-events-1">предыдущей заметке</a> мы сделали расширение Selenium RC, упрощающее операции, связанные с ожиданием загрузки страниц веб-приложения. Но те, кто занимается тестированием AJAX-приложений, с этими операциями сталкиваются редко, им приходится работать с другими событиями – появление и исчезновение элементов интерфейса, а также изменение их свойств (таких как, например, видимость или цвет). Поэтому сейчас мы добавим в наше расширение набор операций, предназначенных для ожидания таких событий.</p><p>Но сначала немного теории о том, как в целом устроена система команд в Selenium.</p>
<h3>Система команд в Selenium</h3>
<p>Все команды, которые есть в Selenium, разделяются на три класса:</p>
<ul>
<li>действия (actions)</li>
<li>получатели данных (accessors)</li>
<li>проверки (assertions)</li>
</ul>
<p><strong>Действия</strong> – это команды, которые управляют состоянием тестируемого приложения, такие как click, check, type, select, fireEvent и т.п.</p>
<p>Большая часть действий приводит к изменению состояния приложения – в результате выполнения такой команды либо отправляется запрос на сервер (например, проход по ссылке или отправка формы), либо происходят какие-то события в браузере (например, заполняются поля формы, устанавливаются cookies или отрабатывает javascript-функция).</p>
<p>Некоторые команды-действия сами ничего не делают, но управляют поведением других команд-действий, например setTimeout, answerOnNextPrompt, chooseCancelOnNextConfirmation.</p>
<p>Наконец, есть несколько команд, которые тоже почему-то относятся к действиям, но на самом деле это команды ожидания некоторого события. Это команды waitForCondition, waitForPageToLoad, waitForPopUp и waitForFrameToLoad, именно им была посящена предыдущая заметка (вообще-то команда waitForCondition может модифицировать состояние приложения, потому что в ней можно выполнить произвольный javascript-код, но теоретически она не должна иметь такого рода побочных эффектов).</p>
<p><strong>Получатели данных</strong> – это команды, предназначенные для получения информации о состоянии тестируемого приложения. В Selenium IDE все такие команды начинаются со слова “store” – storeTitle, storeText, storeElementPresent и т.д., они сохраняют полученную информацию о состоянии приложения в переменные, которые могут быть использованы в последующих командах.</p>
<p>В Selenium RC используется другая схема именования – имена получателей, возвращающих текстовое значение, начинаются со слова “get”, а имена получателей, возвращающих булевское значение (да/нет, true/false), начинаются со слова “is”. Например, getTitle, getText, getAttribute, но – isChecked, isElementPresent, isVisible.</p>
<p><strong>Проверки</strong> как самостоятельные команды существуют только в Selenium IDE. Они генерируются автоматически, для каждого получателя данных создается шесть проверок: прямая и обратная проверки в трёх режимах – assert, verify и waitFor. Например, для команды storeElementPresent создаются следующие проверки: assertElementPresent, assertElementNotPresent, verifyElementPresent, verifyElementNotPresent, waitForElementPresent, waitForElementNotPresent.</p>
<p>В Selenium RC проверки реализуются как комбинация получателя данных и подходящего метода из используемого фреймворка для разработки тестов.</p>
<p>Так, скажем, для фреймворка <a href="http://testng.org/">TestNG (Java)</a> проверки типа “assert” будут выглядеть примерно так:</p>
<pre xml:lang="java">assertEquals(getText("id=result"), "expected value");
assertFalse(isElementPresent("id=error"));</pre>
<p>А для фреймворка <a href="http://docs.python.org/library/unittest.html">Python unittest</a> аналогичные проверки будут такими:</p>
<pre xml:lang="python">self.assertEqual("expected value", sel.get_text("id=result"))
self.assertFalse(sel.is_element_present("id=error"))</pre>
<p>Чуть сложнее устроены проверки типа “verify”. Они отличаются от проверок типа “assert” тем, что не должны немедленно прерывать выполнение теста, вместо этого сообщение об ошибке вносится в специальный список. Этот способ используется для выполнения некритичных проверок, после которых можно продолжать выполнение даже если проверка дала отрицательный результат. При этом тест отрабатывает до конца, и если список ошибок непустой, он всё-таки помечается как завершившийся неуспешно.</p>
<p>Тестовые фреймворки как правило не имеют встроенной поддержки для проверок такого типа.</p>
<p>Для тех, кто разрабатывает тесты на языке Java, ситуация несколько лучше. В TestNG проверки типа “verify” реализованы во вспомогательном классе SeleneseTestNgHelper, о котором мы уже говорили в <a href="http://software-testing.ru/library/testing/functional-testing/1042-selenium-auto-screenshoots">предыдущих заметках</a>. Выглядеть это будет следующим образом:</p>
<pre xml:lang="java">verifyEquals(getText("id=result"), "expected value");
verifyFalse(isElementPresent("id=error"));</pre>
<p>Аналогичная поддержка проверок типа “verify” есть и в некоторых других фреймворках, в частности JUnit для Java и Groovy.</p>
<p>А вот для проверок типа “waitFor” нет поддержки ни в одном известном мне фреймворке или расширении для Selenium. Поэтому мы реализуем эту поддержку самостоятельно для TestNG (а если вы пользуетесь чем-нибудь другим – можете адаптировать это для своего фреймворка самостоятельно).</p>
<p>Но сначала ещё чуть-чуть поговорим о том, почему эти команды играют столь важную роль при тестировании AJAX-приложений</p>
<h4>AJAX и команды-проверки типа “waitFor”</h4>
<p>В “классических” веб-приложениях тесты устроены таким образом, что мы сначала выполняем некоторую последовательность действий, завершающуюся отправкой запроса на веб-сервер. Затем мы должны дождаться, пока браузер получит от сервера ответ, после чего приступить к его проверке. И для ожидания ответа обычно используется команда waitForPageToLoad.</p>
<p>Но для AJAX-приложений этот способ не годится, потому что обращения к серверу выполняются в “фоновом режиме”, после чего обновляются только отдельные части страницы, полностью страница не перегружается. Поэтому команда waitForPageToLoad оказывается совершенно бесполезной.</p>
<p>Вместо ожидания загрузки страницы в таких приложениях мы должны определить некоторые другие критерии завершения обработки запроса. Это может быть появление или исчезновение каких-либо элементов на странице, либо изменение их свойств – видимость, цвет, расположение и т.д. Соответственно, нам нужны команды для ожидания таких событий – а это и есть те самые команды-проверки типа “waitFor”, о которых шла речь выше.</p>
<p>Ну что ж, пришла пора заняться реализацией всех этих проверок.</p>
<h4>Реализация waitFor-проверок</h4>
<p>За основую релизации методов ожидания можно взять код, который генерирует Selenium IDE для проверок типа “waitFor”.</p>
<p>Вот что там предлагается, например, для команды waitForVisible:</p>
<pre xml:lang="java">for (int second = 0;; second++) {
    if (second &gt;= 60) fail("timeout");
    try {
        if (selenium.isVisible("id=result")) break;
    } catch (Exception e) {}
    Thread.sleep(1000);
}</pre>
<p>Идея вполне очевидна – в цикле раз в секунду проверять, виден ли нужный элемент. Если виден – ожидание прекращается. А если прошло уже достаточно много проверок (60) и все неуспешные – тогда можно завершить тест с сообщением о том, что время ожидания истекло.</p>
<p>Разумеется, невозможно каждый раз, когда требуется сделать такого рода проверку, вставлять столь громоздкий кусок кода. Давайте оформим его в виде вспомогательного метода, вот такого:</p>
<pre xml:lang="java">public void waitForVisible(String locator) {
    for (int second = 0;;  second++) {
        if (second &gt;= 60) {
            throw new  AssertionError("timeout");
        }
        try {
            if (selenium.isVisible(locator))  break;
        } catch (Exception e) {}
        
        try {
            Thread.sleep(1000);
        } catch  (InterruptedException e) {
            throw new AssertionError(e);
        }
    }
}</pre>
<p>Теперь посмотрим пристально, и попробуем понять, сколько времени будет ожидать этот метод, прежде чем сообщит о неудаче? Думаете, 60 секунд? Отнюдь! Например, на моём ноутбуке, где я пишу эту заметку, он работает примерно 140 секунд. Дело в том, что на самом деле в цикле считаются не секунды, а количество попыток. Между попытками проходит секунда, но сами попытки тоже требуют определённого времени, причём весьма существенного. То есть у меня 60 секунд ушло на ожидание, и ещё 80 секунд заняли обращения к Selenium.</p>
<p>Давайте исправим это так, чтобы метод на самом деле выполнял проверки в течение указанного <strong>времени</strong>:</p>
<pre xml:lang="java">public void waitForVisible(String locator) {
    long start = System.currentTimeMillis();
    while (System.currentTimeMillis() &lt; start  + 60000) {
        try {
            if (selenium.isVisible(locator)) return;
        } catch  (Exception e) {}

        try {
            Thread.sleep(1000);
        } catch  (InterruptedException e) {
            throw new AssertionError(e);
        }
    }
    throw  new AssertionError("timeout");
}</pre>
<p>Кроме того, хорошо бы сделать время ожидания параметром, а также дать возможность настраивать дефолтное время ожидания и промежуток между попытками:</p>
<pre xml:lang="java">public void waitForVisible(String locator) {
    waitForVisible(locator,  getDefaultTimeoutWaitFor());
}

public void waitForVisible(String  locator, long timeout) {
    long pause = getAttemptsInterval();
    long  start = System.currentTimeMillis();

    while (System.currentTimeMillis()  &lt; start + timeout) {
        try {
            if (selenium.isVisible(locator)) return;
        } catch (Exception e) {}

        try {
            Thread.sleep(pause);
        } catch  (InterruptedException e) {
            throw new AssertionError(e);
        }
    }
    throw  new AssertionError("timeout");
}</pre>
<p>Далее мы должны были бы создать аналогичные методы для всех команд получения данных, но это не очень хорошо, потому что у нас получится множество методов, похожих как близнецы-братья.</p>
<p>Более правильный способ состоит в том, чтобы отделить “логику ожидания” от “логики проверки”, создать один унивесальный метод ожидания, который может проверять разные условия. Именно так, кстати, реализованы проверки типа “assert” и “verify” – в них комбинируется единый универсальный метод проверки с семейством специализированных методов получения данных.</p>
<p>Мы сделаем такую реализацию, в которой проверка-ожидание будет выглядеть следующим образом:</p>
<pre xml:lang="java">boolean res = selenium.waitFor(Visible("id=result"));</pre>
<p>То есть у нас будет унивесальный метод waitFor (а также waitForNot) и семейство методов, реализующих логику проверки, по одному для каждой операции получения данных.</p>
<p>Кроме того, мы сделаем так, чтобы при неуспешном завершении он не прерывал выполнение теста, а просто возвращал false (а при успешном завершении, соответственно, true). Это даст возможность разработчику тестов самостоятельно принять решение о том, что делать в той или иной ситуации. Если он решит, что тест должен прерываться, можно добиться этого эффекта путём комбинирования с методом assertTrue:</p>
<pre xml:lang="java">assertTrue(selenium.waitFor(Visible("id=result")));</pre>
<p>Итак, вот как устроен универсальный метод ожидания, который мы поместим в класс WaitingSelenium:</p>
<pre xml:lang="java">public boolean waitFor(Condition condition) {
    return  waitFor(condition, getDefaultTimeoutWaitFor());
}

public boolean waitFor(Condition condition, long timeout) {
    long pause =  getAttemptsInterval();
    long start = System.currentTimeMillis();

    while (System.currentTimeMillis() &lt; start + timeout) {
        try {
            if (condition.checkConditionWith(this)) return true;
        } catch (Exception e) {}

        try {
            Thread.sleep(pause);
        } catch (InterruptedException e) {
            return false;
        }
    }
    return false;
}</pre>
<p>На вход он получает параметр типа Condition, это интерфейс, в котором имеется всего один метод:</p>
<pre xml:lang="java">public interface Condition {
    boolean checkConditionWith(Selenium selenium);
}</pre>
<p>А вот метод Visible, который реализует проверку того, виден или нет элемент с заданным локатором:</p>
<pre xml:lang="java">public static Condition Visible(final String locator) {
    return new Condition() {
        public boolean checkConditionWith(Selenium selenium)  {
            return selenium.isVisible(locator);
        }
    };
}</pre>
<p>Вот и всё. Теперь надо наделать много методов, аналогичных Visible – для всех команд получения данных, и можно пользоваться. Впрочем, всё это уже есть в приложенном архиве, содержащем код – в класс WaitingSelenium добавлены два универсальных метода ожидания, а в классе SeleneseTestNgHelper появилась целая серия методов, создающих проверки для практически всех команд-получателей данных. Пропущены команды getAllButtons, getAllFields, getAllLinks, getAllWindowIds, getAllWindowNames и getAllWindowTitles, для которых проверки типа waitFor не имеют особого смысла, но про которые мы ещё поговорим в будущем. Кроме того, нет проверок для команды storeLogMessages, которая просто заглушка без реализации, и для команд WhetherThisFrameMatchFrameExpression и WhetherThisWindowMatchFrameExpression, которые предназначены для сугубо служебных целей.</p>
<p>И напоследок ещё одно замечание – условия для проверки можно делать сколь угодно сложными, они не обязательно должны состоять только из одной команды Selenium.</p>
<p>А в следущей заметке серии мы реализуем ещё два метода ожидания, которых в Selenium нет вообще, но которые тоже бывают полезны при тестировании AJAX-приложений – waitForChange и waitForStopChanges.</p>
<p>В приложении находится проект Eclipse, содержащий исходный код расширения WaitingSelenium и модифицированный класс SeleneseTestNgHelper, в которых реализованы проверки-ожидания: <a href="http://software-testing.ru/files/library/barancev/waiting_selenium/WaitingSelenium2.zip">WaitingSelenium2.zip</a></p>
<h4 style="text-align: center;"><a href="http://software-testing.ru/forum/topic/17512/">Обсудить в форуме</a></h4>
