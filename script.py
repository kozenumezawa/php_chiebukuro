# -*- coding: utf-8 -*-

import lxml.html
import requests

def getDOM(target_url):
    target_html = requests.get(target_url).text
    dom = lxml.html.fromstring(target_html)
    return dom

f = open('url.txt')
url = f.read()
f.close()

top_dom = getDOM(url)
qalst = top_dom.get_element_by_id('qalst')

# search li tag
for li_tag in qalst:
    a_tag = li_tag[0][0][0]
    a_attrib = a_tag.attrib

    # access detail page
    detail_dom = getDOM(a_attrib['href'])
    div_question = detail_dom.xpath('//div[@class="ptsQes"]')
    p_question = div_question[0][0].text_content()
    print(p_question)
    # print(detail_dom.xpath('//p[@class="queTxt"]'))
    # print(detail_dom.xpath('//p[@class="ptsQes"]/text()'))
    # "ptsQes"
    # "queTxt"


#
# root = lxml.html.fromstring(target_html)
# print(root)
# root.cssselect('#news_body > p').text_content()
