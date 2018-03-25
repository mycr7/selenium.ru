---
layout: page
#header:
#  image_fullwidth: you-can-delete-me-header.png
permalink: /index.html
---
**Selenium -- это инструмент для автоматизированного управления браузерами.**

Наиболее популярной областью применения Selenium является автоматизация тестирования веб-приложений. Однако при помощи Selenium можно (и даже нужно!) автоматизировать любые другие рутинные действия, выполняемые через браузер.

Разработка Selenium поддерживается производителями популярных браузеров. Они адаптируют браузеры для более тесной интеграции с Selenium, а иногда даже реализуют встроенную поддержку Selenium в браузере.

Selenium позволяет разрабатывать сценарии автоматизации практически на любом языке программирования. Он является ключевым компонентом целого ряда как открытых, так и проприетарных инструментов автоматизации. С помощью Selenium можно организовывать распределённые стенды, состоящие из сотен машин с разными операционными системами и браузерами, и даже выполнять сценарии в облаках.

_Selenium -- это настоящее и будущее автоматизированного управления браузерами. Если Вы хотите считаться профессионалом в области автоматизации тестирования веб-приложений -- Вы обязательно должны владеть этим инструментом._

## Какая часть Selenium нужна Вам?

<div class="medium-4 columns frontpage-widget">
	{% capture widget_url %}{% if include.widget.url contains 'http' %}{{ include.widget.url }}{% else %}{{ site.url }}{{ site.baseurl }}{{ include.widget.url }}{% endif %}{% endcapture %}
	<a href="{{ widget_url }}">
		{% if include.widget.image %}
			{%comment%}TODO lazy loading{%endcomment%}
			{%comment%}<img class="lazy" data-src="{% if include.widget.image contains='http://' %}{{ include.widget.image }}{% else %}{{ site.urlimg }}{{ include.widget.image }}{% endif %}" width="100%" alt="" />{%endcomment%}
			{%comment%}<noscript>{%endcomment%}
			{% capture widget_image %}{% if include.widget.image contains 'http' %}{{ include.widget.image }}{% else %}{{ site.url }}{{ site.baseurl }}{{ include.widget.image }}{% endif %}{% endcapture %}
			<img src="{{widget_image}}" width="100%" alt="" />
			{%comment%}</noscript>{%endcomment%}
		{% endif %}
		{% if include.widget.video %}{{ include.widget.video }}{% endif %}
	</a>
	<h2 class="font-size-h3 t10">{{ include.widget.title }}</h2>
	<p>{{ include.widget.text }}</p>
	<p><a class="button tiny radius" href="{% if include.widget.url contains 'http' %}{{ include.widget.url }}{% else %}{{ site.url }}{{ site.baseurl }}{{ include.widget.url }}{% endif %}">{{ site.data.language.more }}</a></p>
</div>
