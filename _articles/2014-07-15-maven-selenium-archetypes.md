---
layout: page
title: Быстрое создание Maven-проекта для Selenium-тестов
redirect_from: /articles/117-maven-selenium-archetypes.html
date: 2014-07-15 14:26:44.000000000 +04:00
author: Super User
teaser: Создание Maven-проекта с нуля вручную -- занятие довольно утомительное. Надо написать POM-файл, добавить в него все нужные зависимости, создать структуру директорий. Всего этого можно избежать, если взять уже готовый шаблон проекта, распаковать его и слегка подправить -- дать проекту уникальное имя, указать номер версии. К счастью, такая возможность создания проектов из готовых шаблонов уже есть в Maven. Но ведь нужен ещё шаблон, в котором уже настроены все нужные зависимости от Selenium и от тестовых фреймворков. Есть такие шаблоны! Две штуки -- один для создания проектов, в которых используется TestNG, и второй для проектов, где используется JUnit.
category: Статьи
---
<p>Создание Maven-проекта с нуля вручную -- занятие довольно утомительное. Надо написать POM-файл, добавить в него все нужные зависимости, создать структуру директорий. Всего этого можно избежать, если взять уже готовый шаблон проекта, распаковать его и слегка подправить -- дать проекту уникальное имя, указать номер версии.</p>
<p>К счастью, такая возможность создания проектов из готовых шаблонов уже есть в Maven. Называются такие заготовки "архетипами", и для создания проекта из архетипа нужно использовать команду 'mvn archetype:generate', подробнее про неё можно почитать <a href="http://maven.apache.org/archetype/maven-archetype-plugin/usage.html">на официальной странице плагина maven-archetype-plugin</a></p>
<p>Но ведь нужен ещё шаблон, в котором уже настроены все нужные зависимости от Selenium и от тестовых фреймворков.</p>
<p>Есть такие шаблоны! Две штуки -- один <a href="http://search.maven.org/#search%7Cga%7C1%7Cwebdriver-testng-archetype">для создания проектов, в которых используется TestNG</a> , и второй <a href="http://search.maven.org/#search%7Cga%7C1%7Cwebdriver-junit-archetype">для проектов, где используется JUnit</a>.</p><p><span style="line-height: 1.3em;">Чтобы сгенерировать проект для TestNG, надо запустить консоль, перейти в директорию, где должен быть создан проект, и выполнить вот такую команду (<strong>в консоли надо всё вводить в одну строчку</strong>):</span></p>
<pre>mvn archetype:generate -DarchetypeGroupId=ru.stqa.selenium<br /><span style="line-height: 1.3em;">-DarchetypeArtifactId=webdriver-testng-archetype -DarchetypeVersion=2.0<br />-DgroupId=com.example -DartifactId=my_example_project</span></pre>
<p>Разумеется, вместо com.example и my_example_project нужно указать ваши собственные значения, и желательно использовать последнюю доступную версию архетипа.</p>
<p>Аналогично создаётся проект, в котором предполагается использовать JUnit, надо лишь заменить параметр archetypeArtifactId:</p>
<pre>mvn archetype:generate -DarchetypeGroupId=ru.stqa.selenium<br />-DarchetypeArtifactId=webdriver-junit-archetype -DarchetypeVersion=2.0<br />-DgroupId=com.example -DartifactId=my_example_project</pre>
<p>Ну и для любителей -- исходный код архетипов можно найти <a href="https://github.com/barancev/webdriver-testng-archetype">здесь</a> и <a href="https://github.com/barancev/webdriver-junit-archetype">здесь</a>.</p>
