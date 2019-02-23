# -*- coding: utf-8 -*-
import requests
from lxml import etree, html

results = []

response = requests.get("http://software-testing.ru/edu/", headers = {'User-agent': 'Mozilla/5.0'})
page = html.fromstring(response.text)
trainings = page.cssselect("div.c-course")
for training in trainings:
    tutor = training.cssselect("div.c-course__attributes a")[0].text
    if (tutor == "Алексей Баранцев"):
        link = training.cssselect("h4.c-course__title a")[0]
        title = link.text
        url = link.get("href")
        date = training.cssselect("div.c-course-aside_attribute")[0].text_content().strip()
        results.append({"title": title, "url": url, "date": date})

with open('_data/trainings.yml', 'w', encoding="utf-8") as file:
    for training in results:
        file.write('- title: "%s"\n  url: http://software-testing.ru%s\n  date: %s\n\n' % (training['title'], training['url'], training['date']))
