---
layout: page
title: Что такое Selenium?
permalink: /kb/
---
#### Selenium – это инструмент для автоматизированного управления браузерами.

Чаще всего Selenium используется для автоматизации тестирования веб-приложений. Однако при помощи Selenium можно автоматизировать любые рутинные действия, выполняемые через браузер.

Разработку Selenium поддерживают производители браузеров. Они адаптируют браузеры для более тесной интеграции с Selenium, а иногда даже реализуют в браузере встроенную поддержку Selenium.

Selenium позволяет писать сценарии практически на любом языке программирования. Он является ключевым компонентом множества открытых и проприетарных инструментов автоматизации. Selenium позволяет управлять браузером удаленно, благодаря чему можно создавать распределённые стенды, состоящие из множества машин с разными операционными системами и браузерами, и даже запускать браузеры в облаках.

### Полный список статей в базе знаний
{% for post in site.kb limit:1000 %}
<dl class="accordion" data-accordion>
  <dd class="accordion-navigation">
    <a href="#panel{{ counter }}"><span class="iconfont"></span> {% if post.subheadline %}{{ post.subheadline }} › {% endif %}<strong>{{ post.title }}</strong></a>
    <div id="panel{{ counter }}" class="content">
      {% if post.meta_description %}{{ post.meta_description | strip_html | escape }}{% elsif post.teaser %}{{ post.teaser | strip_html | escape }}{% endif %}
      <a href="{{ site.url }}{{ post.url }}" title="Read {{ post.title | escape_once }}"><strong>{{ site.data.language.read_more }}</strong></a><br><br>
    </div>
  </dd>
</dl>
{% endfor %}
