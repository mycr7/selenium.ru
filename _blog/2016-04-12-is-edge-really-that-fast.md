---
layout: page
title: '"Is Edge really that fast?"'
joomla_id: 174
joomla_url: is-edge-really-that-fast
date: 2016-04-12 09:25:37.000000000 +03:00
author: Алексей Баранцев
excerpt: |-
  <p> <img src="images/blog/microsoft-edge-extensions.jpg" border="0" alt="" /></p>
  <p>Официальные внешние интерфейсы для интеграции приложений с браузерами не очень хорошо приспособлены для "тонкого" управления браузерами. Они главным образом рассчитаны на то, что движок браузера будет встроен в приложение и в нём будут просто открываться странички. Однако Selenium требует более тесной интеграции. И кто может реализовать это лучше, чем сам производитель браузера?</p>
  <p>Все, кто использует Selenium, уже привыкли к тому, что браузер Internet Explorer самый медлительный из всех. Но распространяется ли это правило на браузер Edge, драйвер для которого делает <span>непосредственно </span>компания Microsoft?</p>
  <p>Посмотрите, например, на эти <a href="http://jperala.fi/2016/04/11/webdriver-locator-performance/">результаты сравнения скорости работы различных локаторов в Edge, Chrome и Firefox</a>.</p>
  <p>Вот итоговая таблица с результатами (указано время выполнения 100 запросов различного типа к одной и той же странице):</p>
  <table class="table table-hover">
  <tbody>
  <tr>
  <td><span>Locator</span></td>
  <td><span>Firefox</span></td>
  <td><span>Chrome</span></td>
  <td><span>Edge</span></td>
  </tr>
  <tr>
  <td><span>name</span></td>
  <td>1377 ms</td>
  <td>929 ms</td>
  <td>204 ms</td>
  </tr>
  <tr>
  <td><span>className</span></td>
  <td>1795 ms</td>
  <td>902 ms</td>
  <td>199 ms</td>
  </tr>
  <tr>
  <td><span>id</span></td>
  <td>1600 ms</td>
  <td>851 ms</td>
  <td><span>262 ms</span></td>
  </tr>
  <tr>
  <td><span>linkText</span></td>
  <td><span>9056 ms</span></td>
  <td><span>1522 ms</span></td>
  <td>238 ms</td>
  </tr>
  <tr>
  <td><span>xpath</span></td>
  <td>2229 ms</td>
  <td>919 ms</td>
  <td>247 ms</td>
  </tr>
  <tr>
  <td><span>cssSelector</span></td>
  <td>1280 ms</td>
  <td>809 ms</td>
  <td>219 ms</td>
  </tr>
  </tbody>
  </table>
  <p>Edge обгоняет конкурентов минимум в 3 раза по всем типам локаторов!</p>
  <p>Ну а если он и на других типах операций окажется быстрее других браузеров... Вам не кажется, что начинается новый виток войны браузеров, сложившееся равновесие нарушено?</p>
category: Блог
---
<p> <img src="images/blog/microsoft-edge-extensions.jpg" border="0" alt="" /></p>
<p>Официальные внешние интерфейсы для интеграции приложений с браузерами не очень хорошо приспособлены для "тонкого" управления браузерами. Они главным образом рассчитаны на то, что движок браузера будет встроен в приложение и в нём будут просто открываться странички. Однако Selenium требует более тесной интеграции. И кто может реализовать это лучше, чем сам производитель браузера?</p>
<p>Все, кто использует Selenium, уже привыкли к тому, что браузер Internet Explorer самый медлительный из всех. Но распространяется ли это правило на браузер Edge, драйвер для которого делает <span>непосредственно </span>компания Microsoft?</p>
<p>Посмотрите, например, на эти <a href="http://jperala.fi/2016/04/11/webdriver-locator-performance/">результаты сравнения скорости работы различных локаторов в Edge, Chrome и Firefox</a>.</p>
<p>Вот итоговая таблица с результатами (указано время выполнения 100 запросов различного типа к одной и той же странице):</p>
<table class="table table-hover">
<tbody>
<tr>
<td><span>Locator</span></td>
<td><span>Firefox</span></td>
<td><span>Chrome</span></td>
<td><span>Edge</span></td>
</tr>
<tr>
<td><span>name</span></td>
<td>1377 ms</td>
<td>929 ms</td>
<td>204 ms</td>
</tr>
<tr>
<td><span>className</span></td>
<td>1795 ms</td>
<td>902 ms</td>
<td>199 ms</td>
</tr>
<tr>
<td><span>id</span></td>
<td>1600 ms</td>
<td>851 ms</td>
<td><span>262 ms</span></td>
</tr>
<tr>
<td><span>linkText</span></td>
<td><span>9056 ms</span></td>
<td><span>1522 ms</span></td>
<td>238 ms</td>
</tr>
<tr>
<td><span>xpath</span></td>
<td>2229 ms</td>
<td>919 ms</td>
<td>247 ms</td>
</tr>
<tr>
<td><span>cssSelector</span></td>
<td>1280 ms</td>
<td>809 ms</td>
<td>219 ms</td>
</tr>
</tbody>
</table>
<p>Edge обгоняет конкурентов минимум в 3 раза по всем типам локаторов!</p>
<p>Ну а если он и на других типах операций окажется быстрее других браузеров... Вам не кажется, что начинается новый виток войны браузеров, сложившееся равновесие нарушено?</p>
