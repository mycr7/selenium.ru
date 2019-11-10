---
layout: page
title: Быстрое создание Maven-проекта для Selenium-тестов
redirect_from: /articles/117-maven-selenium-archetypes.html
date: 2014-07-15 14:26:44.000000000 +04:00
author: Алексей Баранцев
teaser: Создание Maven-проекта с нуля вручную -- занятие довольно утомительное. Надо написать POM-файл, добавить в него все нужные зависимости, создать структуру директорий. Всего этого можно избежать, если взять уже готовый шаблон проекта, распаковать его и слегка подправить -- дать проекту уникальное имя, указать номер версии. К счастью, такая возможность создания проектов из готовых шаблонов уже есть в Maven. Но ведь нужен ещё шаблон, в котором уже настроены все нужные зависимости от Selenium и от тестовых фреймворков. Есть такие шаблоны! Две штуки -- один для создания проектов, в которых используется TestNG, и второй для проектов, где используется JUnit.
category: Статьи
---
Создание Maven-проекта с нуля вручную -- занятие довольно утомительное. Надо написать POM-файл, добавить в него все нужные зависимости, создать структуру директорий. Всего этого можно избежать, если взять уже готовый шаблон проекта, распаковать его и слегка подправить -- дать проекту уникальное имя, указать номер версии.

К счастью, такая возможность создания проектов из готовых шаблонов уже есть в Maven. Называются такие заготовки "архетипами", и для создания проекта из архетипа нужно использовать команду `mvn archetype:generate`, подробнее про неё можно почитать [на официальной странице плагина maven-archetype-plugin](http://maven.apache.org/archetype/maven-archetype-plugin/usage.html)

Но ведь нужен ещё шаблон, в котором уже настроены все нужные зависимости от Selenium и от тестовых фреймворков.

Есть такие шаблоны! Две штуки -- один [для создания проектов, в которых используется TestNG](http://search.maven.org/#search%7Cga%7C1%7Cwebdriver-testng-archetype) , и второй [для проектов, где используется JUnit](http://search.maven.org/#search%7Cga%7C1%7Cwebdriver-junit-archetype).

Чтобы сгенерировать проект для TestNG, надо запустить консоль, перейти в директорию, где должен быть создан проект, и выполнить вот такую команду (**в консоли надо всё вводить в одну строчку**):

{% highlight bash %}
mvn archetype:generate -DarchetypeGroupId=ru.stqa.selenium
-DarchetypeArtifactId=webdriver-testng-archetype -DarchetypeVersion=2.0
-DgroupId=com.example -DartifactId=my_example_project
{% endhighlight %}

Разумеется, вместо `com.example` и `my_example_project` нужно указать ваши собственные значения, и желательно использовать последнюю доступную версию архетипа.

Аналогично создаётся проект, в котором предполагается использовать JUnit, надо лишь заменить параметр `archetypeArtifactId`:

{% highlight bash %}
mvn archetype:generate -DarchetypeGroupId=ru.stqa.selenium
-DarchetypeArtifactId=webdriver-junit-archetype -DarchetypeVersion=2.0
-DgroupId=com.example -DartifactId=my_example_project
{% endhighlight %}

Ну и для любителей -- исходный код архетипов можно найти [здесь](https://github.com/barancev/webdriver-testng-archetype) и [здесь](https://github.com/barancev/webdriver-junit-archetype).

