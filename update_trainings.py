# -*- coding: utf-8 -*-
import requests
from lxml import etree, html

results = []

response = requests.get("http://software-testing.ru/edu/")
page = html.fromstring(response.text)
trainings = page.cssselect("div.c-course")
for training in trainings:
    tutor = training.cssselect("td.c-course__attributes a").text
    if (tutor == "Алексей Баранцев"):
        link = training.cssselect("h4.c-course__title a")
        title = link.text
        url = link.get("href")
        date = training.cssselect("i.c-course-icon_calendar").text
        results.append({"title": title, "url": url, "date": date})

print(results)
