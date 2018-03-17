---
layout: page
title: 'SWD.Starter: Быстрый старт автоматизации тестирования UI на C# + Selenium
  WebDriver + PageObjects'
joomla_id: 104
joomla_url: swd-starter-bystryj-start-avtomatizatsii-testirovaniya-ui-na-c-selenium-webdriver-pageobjects
date: 2014-01-13 11:05:18.000000000 +04:00
author: Super User
excerpt: |-
  <div><img src="http://habr.habrastorage.org/post_images/7d0/06e/13d/7d006e13d24b41a24b7d16b89f04060b.png" border="0" alt="WTF Logo" align="right" />Автор: <a href="http://blog.zhariy.com/" target="_blank">Дмитрий Жарий</a></div>
  <div><br /> Статья расскажет о том, как настроить фреймворк автоматизированного тестирования пользовательского интерфейса на языке C#, вместе с Selenium WebDriver и паттерном PageObjects. <br /> <br /> Стартовый набор с открытым исходным кодом – SWD.Starter – поможет написать и запустить ваш первый тест в течении 10 минут. Кроме этого, предлагая архитектуру фреймворка, основанную на хороших практиках автоматизации тестирования. <br /> Весь код SWD.Starter может быть полностью настроен под ваши задачи.</div>
category: Статьи
---
<div><img src="http://habr.habrastorage.org/post_images/7d0/06e/13d/7d006e13d24b41a24b7d16b89f04060b.png" border="0" alt="WTF Logo" align="right" />Автор: <a href="http://blog.zhariy.com/" target="_blank">Дмитрий Жарий</a></div>
<div><br /> Статья расскажет о том, как настроить фреймворк автоматизированного тестирования пользовательского интерфейса на языке C#, вместе с Selenium WebDriver и паттерном PageObjects. <br /> <br /> Стартовый набор с открытым исходным кодом – SWD.Starter – поможет написать и запустить ваш первый тест в течении 10 минут. Кроме этого, предлагая архитектуру фреймворка, основанную на хороших практиках автоматизации тестирования. <br /> Весь код SWD.Starter может быть полностью настроен под ваши задачи.</div><div>
<h2>Что такое SWD.Starter?</h2>
SWD.Starter – это стартовый набор для вашего фреймворка автоматизации тестирования. Весь исходный код доступен на GitHub: <a href="https://github.com/dzhariy/SWD.Starter">dzhariy/SWD.Starter</a>, а лицензия проекта (unlicense), позволяет вам использовать исходный код как угодно, хоть продавать. <br /> <br /> SWD.Starter – это уже настроенный проект, содержащий весь необходимый инфраструктурный код для начала создания и запуска тестов пользовательского интерфейса через Selenium WebDriver. <br /> <br /> SWD.Starter настойчиво рекомендует использование паттерна PageObjects. И в случае использования этого паттерна, вы сможете писать новый код авто-тестов действительно быстро, при этом, сохраняя красивую архитектуру и читабельность кода. <br />
<h2>Что необходимо для начала</h2>
Для запуска проекта, вам будет необходимо следующее программное обеспечение:<br /><ol>
<li>Visual Studio Express 2013 Desktop Edition (также, теоретически, поддерживаются VS2010 и VS2012)</li>
<li>Git для выкачки проекта из Github</li>
<li>Дополнительные драйвера браузеров Selenium WebDriver, которые можно <a href="http://docs.seleniumhq.org/download/">скачать с официальной страницы проекта</a></li>
</ol>Для быстрой и удобной установки ПО, я рекомендую использовать пакетный менеджер для Windows – <a href="http://chocolatey.org">Chocolatey</a>.<br /> Согласно инструкциям на главной странице, откройте cmd.exe, и в консольном окне, просто выполните следующий код:<br /> <br />
<pre xml:lang="dos">@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" &amp;&amp; SET PATH=%PATH%;%systemdrive%\chocolatey\bin</pre>
</div>
<div class="content html_format"> </div>
<div class="content html_format">А далее, в том же консольном окне, выполните следующие команды:<br />
<ul>
<li>cinst VisualStudioExpress2013WindowsDesktop</li>
<li>cinst git</li>
</ul>
Теперь, в консольном окне (например в cmd.exe или Far Manager), выберете папку, куда вы хотите клонировать SWD.Starter – и запустите команду:</div>
<div class="content html_format"><br />
<pre xml:lang="dos">git clone https://github.com/dzhariy/SWD.Starter.git</pre>
Это обязательный шаг, иначе проект не скомпилируется:<br /> Скопируйте <em>chromedriver.exe</em> и <em>IEDriverServer.exe</em> в папку <em>SWD.Starter\webdrivers</em><br /> <br /> А вот видео полной установки на чистую виртуалку (которую я скачал с <a href="http://modern.ie">modern.ie</a> )<br />
<div class="spoiler"><strong class="spoiler_title"> </strong></div>
<div class="spoiler"><strong class="spoiler_title">Следуй за розовым покемоном, Нео!</strong></div>
<iframe src="http://www.youtube.com/embed/8wigKFJ3WmY" frameborder="0" width="560" height="315"></iframe>
<div class="spoiler"><strong class="spoiler_title">На всякий случай замечу, на видео видно, что Windows на виртуальной машине требует активацию. <br /> Cогласно лицензионным условиям modern.ie я имею право использовать такие образы легально в тестовых целях. В пользовательском соглашении сказано, что я не должен активировать Windows в этом случае.</strong></div>
<div class="spoiler">
<div class="spoiler_text" style="display: none;"> </div>
<div class="spoiler_text" style="display: none;"> </div>
<div class="spoiler_text" style="display: none;"><iframe src="http://www.youtube.com/embed/8wigKFJ3WmY?wmode=opaque" frameborder="0" width="560" height="349"></iframe><br /> На всякий случай замечу, на видео видно, что Windows на виртуальной машине требует активацию. <br /> Cогласно лицензионным условиям modern.ie я имею право использовать такие образы легально в тестовых целях. В пользовательском соглашении сказано, что я не должен активировать Windows в этом случае.</div>
</div>
<br />
<h2>Что такое PageObjects и почему это настолько важно?</h2>
Если говорить просто, то подход в автоматизированном тестировании, с использованием PageObjects, заключается в том, что вы просто выносите весь код низкоуровневой работы со страницей (например, набор текста и нажатия мышкой по элементам) в отдельные классы. <br /> <br /> Теперь ваши тесты не работают со страницей напрямую, вызывая низкоуровневые методы WebDriver, а используют более высокоуровневые операции, специфичные для каждой страницы. <br /> <br /> Это сокращает количество строк кода в тестах, тем самым делая код более читабельным, понятным и надёжным. <br /> Подход PageObjects – это альтернатива бот-стилю – вызову методов WebDriver из тестов напрямую.<br /> В самом начале, бот-стиль кажется проще и понятнее чем использование PageObjects. Но, это огромное заблуждение, которое может привести ваш проект автоматизации к краху. <br /> <br /> Со временем, когда количество тестов будет расти, в случае использования бот-стиля, вы будете тратить все больше и больше времени на их поддержку. В итоге, поддержка фреймворка автоматизации будет экономически не выгодной и руководством проекта будет принято решение вернутся к ручному тестированию. А уже написанный код останется только выбросить, по причине того, что он уже не соответствует реальному тестируемому приложению. <br /> <br /> Тесты в бот-стиле подобны огромной не отсортированной куче книг. Когда ваша «куча» состоит всего из 10-ти книг, в ней можно разобраться без особых трудностей. <br /> Но, что вас ждёт, когда количество книг возрастёт до 100? Поверьте, я вам не завидую. Просто потому, что сам через это уже прошёл.<br /> <img src="http://habr.habrastorage.org/post_images/ca7/470/a71/ca7470a71888b02b819e1633c168a35c.png" border="0" alt="Heap of books" /><br /> <br /> С другой стороны, при использовании PageObjects, можно разложить все книги по полочкам. В книжных магазинах и на складах, содержится огромное количество книг. Тем не менее, продавцы могут быстро найти то, что вам нужно. <br /> PageObject-класс – это книжная полка, позволяющая удобно организовать код работы с веб-страницей. А популярные языки программирования и IDE предоставляют значительно больше возможностей при использовании объектно-ориентированного программирования. <br /> <br /> <img src="http://habr.habrastorage.org/post_images/5c1/56d/5e8/5c156d5e83e0d75308c877228e568888.png" border="0" alt="Book shelf" /><br /> <br />
<h3>Тесты в бот-стиле</h3>
Основное преимущество тестов в бот-стиле то, что вы можете их «записать даже не зная языка программирования», при помощи таких инструментов, как Selenium IDE и Selenium Builder. <br /> <br /> В результате, может получится нечто такое:</div>
<pre xml:lang="csharp">class BrittleTest
{
    [Test]
    public void Can_buy_an_Album_when_registered()
    {
        var driver = Host.Instance.Application.Browser;
        driver.Navigate().GoToUrl(driver.Url);
        driver.FindElement(By.LinkText("Admin")).Click();
        driver.FindElement(By.LinkText("Register")).Click();
        driver.FindElement(By.Id("UserName")).Clear();
        driver.FindElement(By.Id("UserName")).SendKeys("HJSimpson");
        driver.FindElement(By.Id("Password")).Clear();
        driver.FindElement(By.Id("Password")).SendKeys("!2345Qwert");
        driver.FindElement(By.Id("ConfirmPassword")).Clear();
        driver.FindElement(By.Id("ConfirmPassword")).SendKeys("!2345Qwert");
        driver.FindElement(By.CssSelector("input[type=\"submit\"]")).Click();
        driver.FindElement(By.LinkText("Disco")).Click();
        driver.FindElement(By.CssSelector("img[alt=\"Le Freak\"]")).Click();
        driver.FindElement(By.LinkText("Add to cart")).Click();
        driver.FindElement(By.LinkText("Checkout &gt;&gt;")).Click();
        driver.FindElement(By.Id("FirstName")).Clear();
        driver.FindElement(By.Id("FirstName")).SendKeys("Homer");
        driver.FindElement(By.Id("LastName")).Clear();
        driver.FindElement(By.Id("LastName")).SendKeys("Simpson");
        driver.FindElement(By.Id("Address")).Clear();
        driver.FindElement(By.Id("Address")).SendKeys("742 Evergreen Terrace");
        driver.FindElement(By.Id("City")).Clear();
        driver.FindElement(By.Id("City")).SendKeys("Springfield");
        driver.FindElement(By.Id("State")).Clear();
        driver.FindElement(By.Id("State")).SendKeys("Kentucky");
        driver.FindElement(By.Id("PostalCode")).Clear();
        driver.FindElement(By.Id("PostalCode")).SendKeys("123456");
        driver.FindElement(By.Id("Country")).Clear();
        driver.FindElement(By.Id("Country")).SendKeys("United States");
        driver.FindElement(By.Id("Phone")).Clear();
        driver.FindElement(By.Id("Phone")).SendKeys("2341231241");
        driver.FindElement(By.Id("Email")).Clear();
        driver.FindElement(By.Id("Email")).SendKeys("chunkylover53@aol.com");
        driver.FindElement(By.Id("PromoCode")).Clear(); 
        driver.FindElement(By.Id("PromoCode")).SendKeys("FREE");
        driver.FindElement(By.CssSelector("input[type=\"submit\"]")).Click();

        Assert.IsTrue(driver.PageSource.Contains("Checkout Complete"));
    }
}</pre>
<div class="content html_format"><br /> Такой подход может быть оправдан при выполнении одноразовых задач. Например, если вам необходимо создать 1000 пользователей через интерфейс приложения – достаточно записать создание одного, и с минимальными изменениями поместить код в цикл. <br /> Такой подход будет губительным, если вы надеетесь на автоматизацию тестирования в долгосрочной перспективе. <br /> Вот один небольшой пример: <br /> <br /> Предположим, доступ к одной странице продукта осуществляется из 30-ти тестов. В один прекрасный день, программисты принимают решение поменять вёрстку страницы: <br /> Теперь и элементы называются по другому, и «логика кликов» меняется. <br /> В этом случае, вам будет необходимо внести изменение в 30 тестов, вместо того, чтобы сделать это в одном классе. <br /> Как вы думаете, сколько времени эта интереснейшая работа займёт?<br /> <br /> <img src="http://habr.habrastorage.org/post_images/377/819/d30/377819d30b15cea6b645ac4c8d20d165.png" border="0" alt="Bot style" /><br /> <br />
<h3>Тесты с использованием PageObject-классов</h3>
Если просто вынести куски кода и организовать все виде нескольких PageObject-классов, то с кодом теста происходят чудесные превращения: он стает понятным, появляются действия, которые можно переиспользовать в других тестах, вместо того чтобы копи-пастить вызовы WebDriver. <br /> Обратите внимание, что в коде теста стало больше строк… Но, это ведь только за счёт комментариев и пояснений, которые важны для демонстрации в этой статье, но необязательны в вашем реальном коде. <br /> Уберите все комментарии и пустые строки – и код все равно останется читабельным и сократится по количеству строк.</div>
<div class="content html_format"><br />
<pre xml:lang="csharp">class PageObjectTest
{
    [Test]
    public void Can_buy_an_Album_when_registered()
    {
        // Обычно, конструкторы PageObject объектов не выполняют действий на странице. 
        // Они необходимы лишь для получения ссылки на объект.
        var registerUserPage = new RegisterUserPage();
        
        // Просто открывает страницу регистрации, при этом, 
        // кликая на все нужные ссылки по пути
        registerUserPage.Invoke();

        // Этот класс используется для передачи данных. 
        // Некоторые данные могут быть заполнены «по умолчанию», но об этом – позже        
        var newUserFromData = new UserFromDataData()
        {
            UserName = "HJSimpson",
            Password = "!2345Qwert",
        };

        // Момент заполнения и отправки формы
        registerUserPage.FillForm(newUserFromData);
        registerUserPage.Submit();
        
        // А следующий код выбирает товар из витрины, добавляет его в корзину 
        // и переходит на страницу оформления заказа. 
        var showCasePage = new ShowCasePage();
        showCasePage.Goto("Disco");
        showCasePage.SelectProduct("showCasePage");
        showCasePage.AddToCard();
        showCasePage.Checkout();

        var checkOutForm = new CheckOutForm();

        // .DefaultValues возвращает класс с уже заполненными данными по умолчанию. 
        // Если нас что-то не устраивает – всегда можно заменить. 
        var checkoutFromData = UserCheckoutFromData.DefaultValues;


        // Вот как раз это и не устраивает! А давайте заменим:
        checkoutFromData.Email = "funkylover53@aol.com";

        CheckoutCompletePage checkoutCompletePage = checkOutForm.Submit();

        Assert.IsTrue(checkoutCompletePage.GetPageTitle().Contains("Checkout Complete"));
    }
}</pre>
<br /> <br /> <br /> <img src="http://habr.habrastorage.org/post_images/c58/b1f/ab9/c58b1fab9dbfebeb4078d5544e6be762.png" border="0" alt="Page Object" /><br /> Ну что? Хотите создавать тесты, используя PageObject?</div>
<div class="content html_format"><br />
<h2>Первый Smoke-тест в SWD.Starter</h2>
Если вы задаётесь вопросом: с чего начать автоматизацию тестирования? То, у меня для вас есть очень простой ответ, который подойдёт в 99% случаев. <br /> Начните со смоук тестов для каждой страницы приложения. <br /> <br /> Рецепт: <br /><ol>
<li>Взять страницу любого уровня вложенности</li>
<li>Открыть страницу</li>
<li>Проверить, что все важные элементы – присутствуют на странице.</li>
</ol>И в результате мы получим легковесный тест, который в случае успешного прохода говорит:<br /> Что все важные элементы отдельной страницы до сих пор не изменились<br /> То, что наши PageObject классы по прежнему соответствуют актуальной странице<br /> То, что путь из точки А. (главная страница) в точку Б. (любая другая страница) – возможен для конечно пользователя приложения.<br /> И все это работает в разных браузерах.<br /> <br /> А теперь, давайте напишем первый тест для страницы регистрации нового пользователя Хабрахабр: <br /> <iframe src="http://www.youtube.com/embed/_se8MGhQrIs?wmode=opaque" frameborder="0" width="560" height="349"></iframe><br /> <br /> Покрыв все страницы приложения такими тестами – вы будете приятно удивлённы: метрики покрытия покажут покрытие больше 50%. Конечно же, мы понимаем, что метрика покрытия кода – не самая основная, но согласитесь, это – хороший результат. <br /> <br /> Кроме того, в <a href="https://github.com/dzhariy/SWD.Starter/blob/master/src/SWD.Core/WebDriver/SwdBrowser.cs">SwdBrowser.cs</a> есть метод HandleJavaScriptErrors(). В данной реализации, его нужно просто почаще вызывать, например, в каждом .Invoke(). И тогда, этот метод сможет отловить возможные неожиданные ошибки JavaScript. <br /> <br /> Я надеюсь, что в ходе просмотра видео, вы заметили несколько интересных вещей? <br /> Например, что в проекте уже готова инфраструктура для смоук-тестов PageObject-классов?.. <br /> И чтобы добавить тест – необходимо просто его записать, сгенерировать код… и следовать инструкциям в сгенерированном коде. <br /> А в самом начале, мы видим строку кода: <br /> <br />
<pre xml:lang="csharp">[TestMethod]
public void S01_First_Step_Run_WebDriver_with_Firefox()
{
    SwdBrowser.Driver.Url = "http://swd-tools.com";
}
</pre>
<br /> которая: открывает браузер, переходит по нужному URL… и закрывает браузер.<br /> Не много ли это для одной строки? <br /> И почему открылся именно FireFox, а что если я хочу Internet Explorer? <br /> Об этом и многом другом – ниже.</div>
<div class="content html_format"><br />
<h2>Хорошие практики в автоматизации тестирования</h2>
Вы знаете, опасно называть практики «лучшими», и поэтому, оставим просто «хорошими». <br /> Время от времени, я описываю такие практики в виде небольших заметок, которые иллюстрируют конкретное решение, но, к сожалению, не показывают общей картины. <br /> <br /> Для того, чтобы показать, как хорошие практики работают вместе, я и начал работу над SWD.Starter. <br /> Вот, например, по статье <a href="http://goo.gl/dYybUL">Автоматическое создание Браузера и инициализация PageObject</a> как раз и был реализован SwdBrowser. А PageObject классы, унаследованные от CorePage – умеют самостоятельно инициализировать веб-элементы. <br /> А в заметке <a href="http://goo.gl/kQdqbD">WebDriverWait и PageObject</a>, я рассказываю, как добавить «умные» методы ожидания элементов для PageObject, по типу WebDriverWait для обычных элементов. <br /> <br /> Все это уже вошло в SWD.Starter. И если вас интересует решение конкретной проблемы – просто посмотрите код, а я, со временем, сделаю так, чтобы в нем можно было легко разобраться. Уже сейчас, некоторые классы в достаточной мере документированы, например – <a href="http://swd-tools.com/swd-starter-api/class_swd_1_1_core_1_1_configuration_1_1_config.html">Swd.Core.Configuration.Config Class</a>. А комментарии для некоторых классов уже есть в коде, но пока ещё не мигрировали в Doxygen.</div>
<div class="content html_format"><br />
<h2>Структура проекта SWD.Starter</h2>
Ядро SWD.Starter – это Swd.Core. В нем содержатся такие интересные штуки как: <img src="http://habr.habrastorage.org/post_images/cab/f22/cc5/cabf22cc5b84bbfc0ef6288cffd4dedc.png" border="0" alt="Solution" align="right" /><br />
<ul>
<li>Класс Swd.Core.Configuration → Config, который читает настройки фреймворка из внешнего файла Config.config. Именно в этом файле можно выбрать запускаемый браузер, а также добавить свои настройки.</li>
<li>Класс Swd.Core.WebDriver → SwdBrowser – уже упоминался. Он управляет жизнью браузера. А рядом, в том же пространстве имен, находятся полезные методы и классы, упрощающие работу с браузером.</li>
<li>В пространстве имен Swd.Core.Pages, живут базовые классы для PageObject'ов.</li>
</ul>
В Swd.Core расположен только общий код, который, в дальнейшем, можно расширить в дочерних проектах по тестированию. <br /> <br /> Пример такого тестового проекта – DemoProject. <br /> Тестовый проект состоит из двух основных подпроектов: <br />
<ul>
<li>Demo.TestModel – содержит декларации PageObject-классов, кастомизированные базовые классы, необходимые данные, кусочки логики работы приложения, и другие библиотечные функции, специфичные для конкретного тестируемого приложения.<br /> Обычно, для отдельного тестируемого приложения должна быть лишь одна библиотека Модели.</li>
<li>Demo.TestProject – проект, содержащий наборы тестов. Таких тестовых проектов может быть несколько. Вот, например, Demo.Tutorial – это тоже проект с тестами, и он также как Demo.TestProject использует библиотеку Модели (Demo.TestModel ).</li>
<li>Demo.Tutorial – попытка создания руководства по работе с Swd.Starter. Пока ещё не совсем законченный, но уже сейчас, можно читать файл «Ch<em>00</em>Introduction.cs» и пробовать запускать тесты.</li>
</ul>
<h2>Обратная связь, лицензия и сотрудничество</h2>
Лицензия проекта позволяет вам производить любые действия с кодом проекта, которые может ограничить лишь ваша фантазия. (http://unlicense.org/)<br /> Код можно видоизменять, использовать в коммерческих целях, выкладывать на торренты и майнить биткоины, если хотите. <br /> <br /> Но, мне бы было очень полезно получить от вас обратную связь. Оставить комментарии можно как тут, так и на странице проекта на Github. <br /> А лучше всего, если вы отправите реальный чёткий пацанячий pull-request в репозиторий на github. <br /> Но, если это будет огромное изменение с перелапачиванием половины кода, то, неплохо было бы вначале его обсудить.<br /> <br /> Над чем можно работать? – Там поле почти не паханное: <br />
<ul>
<li>Документация</li>
<li>Туториал</li>
<li>Новый полезный код, решающий реальные проблемы</li>
<li>Новые демонстрационные проекты</li>
<li>Инструкции</li>
</ul>
И ещё. 28-го февраля 2014 в Киеве, я планирую выступать с докладом на конференции <a href="http://goo.gl/JHWbXZ">Selenium Camp 2014</a>. Доклад будет посвящён проекту SWD Page Recorder, но и проекту SWD.Starter будет посвящено не мало времени. А после, запись доклада появится в <a href="http://goo.gl/DB1SXh">разделе архива материалов</a>, через 3-4 месяца после конференции. <br /> Я буду доступен все два дня, и буду готов пообщаться «в живую» как после моего доклада, так и в течении всего времени конференции.</div>
<div class="content html_format"><br />
<h2>Полезные материалы</h2>
<ul>
<li><a href="http://swd-tools.com">SWD Tools</a> – страница проектов Page Recorder и Starter. Содержит (или будет содержать) все необходимые ссылки, касательно проектов</li>
<li><a href="https://github.com/dzhariy/SWD.Starter">GitHub SWD Starter</a></li>
<li><a href="https://github.com/dzhariy/swd-recorder/">GitHub SWD Page Recorder</a></li>
<li><a href="http://habrahabr.ru/post/191802/">SWD Page Recorder: Записывает PageObject-классы для Selenium WebDriver</a> – Обзор SWD Page Recorder на Хабрахабр</li>
<li><a href="http://habrahabr.ru/post/145848/">Вебинар: Основы использования паттерна Page Object вместе с Selenium WebDriver</a></li>
<li><a href="http://blog.zhariy.com/2013/12/atinfo.html">Подборка свежих заметок и статей по автоматизации тестирования</a> – если вам интересны советы по автоматизации тестирования</li>
<li><a href="http://blog.zhariy.com/2013/02/atdays-pageobject.html">Слайды/Видео к моему докладу на #atdays: За пределами PageObject</a></li>
<li><a href="http://net.tutsplus.com/tutorials/maintainable-automated-ui-tests/">Maintainable Automated UI Tests</a> – отличная статья, с современным взглядом на автоматизацию тестирования</li>
</ul>
Успешной вам автоматизации.<br /><hr /><br /> <em>P.S.: <strong>SWD</strong> расшифровывается как <strong>S</strong>elenium <strong>W</strong>eb<strong>D</strong>river</em></div>
