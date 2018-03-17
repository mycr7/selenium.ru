---
layout: page
title: Больше cookies для Internet Explorer!
joomla_id: 147
joomla_url: ie-cookies
date: 2015-06-26 08:06:38.000000000 +03:00
author: Алексей Баранцев
excerpt: |-
  <p><img src="images/blog/browser-cookies.jpg" border="0" alt="" /></p>
  <p>На <span>фронте борьбы с Internet Explorer</span> <span>на </span><span>этой неделе</span><span> </span>случился небольшой технологический прорыв: <a href="https://github.com/SeleniumHQ/selenium/commit/43ec621c6abc239c2d1c1f7563d099970e2299da">Jim Evans переделал механизм получения cookies</a>, теперь Selenium умеет не только извлекать их через интерфейс браузера, но и загружать cookies из файлов, куда их сохраняет браузер.</p>
  <p>Это даёт возможность во-первых, получить доступ к тем cookies, у которых стоит флаг httpOnly, и которые раньше были недоступны в Internet Explorer. А во-вторых, таким способом удаётся получить больше информации про cookies, в частности, дату "протухания" (expiration date).</p>
  <p>Правда, некоторые ограничения всё равно остались -- браузер сохраняет в файлы только так называемые "персистентные" cookies, а ещё бывают "сессионные", их браузер не сохраняет в файлы или сохраняет частично, и надёжного способа получить сессионные cookies с флагом httpOnly, увы, пока не найдено.</p>
  <p><span style="color: #808080;">P.S. Картинка с печеньками утащена <a href="http://www.twistermc.com/41054/browser-sugar-cookies/"><span style="color: #808080;">отсюда</span></a>.</span></p>
category: Блог
---
<p><img src="images/blog/browser-cookies.jpg" border="0" alt="" /></p>
<p>На <span>фронте борьбы с Internet Explorer</span> <span>на </span><span>этой неделе</span><span> </span>случился небольшой технологический прорыв: <a href="https://github.com/SeleniumHQ/selenium/commit/43ec621c6abc239c2d1c1f7563d099970e2299da">Jim Evans переделал механизм получения cookies</a>, теперь Selenium умеет не только извлекать их через интерфейс браузера, но и загружать cookies из файлов, куда их сохраняет браузер.</p>
<p>Это даёт возможность во-первых, получить доступ к тем cookies, у которых стоит флаг httpOnly, и которые раньше были недоступны в Internet Explorer. А во-вторых, таким способом удаётся получить больше информации про cookies, в частности, дату "протухания" (expiration date).</p>
<p>Правда, некоторые ограничения всё равно остались -- браузер сохраняет в файлы только так называемые "персистентные" cookies, а ещё бывают "сессионные", их браузер не сохраняет в файлы или сохраняет частично, и надёжного способа получить сессионные cookies с флагом httpOnly, увы, пока не найдено.</p>
<p><span style="color: #808080;">P.S. Картинка с печеньками утащена <a href="http://www.twistermc.com/41054/browser-sugar-cookies/"><span style="color: #808080;">отсюда</span></a>.</span></p>
