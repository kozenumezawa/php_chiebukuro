# -*- coding: utf-8 -*-

import lxml.html
import requests
import codecs

def getDOM(target_url):
    target_html = requests.get(target_url).text
    dom = lxml.html.fromstring(target_html)
    return dom

f_question = codecs.open('love_question.txt', 'w', 'utf-8')
f_answer = codecs.open('love_answer.txt', 'w', 'utf-8')

f = open('url.txt')
url = f.read()
f.close()

for i in range(10):
    open_url = url + str(i)

    top_dom = getDOM(open_url)
    qalst = top_dom.get_element_by_id('qalst')

    # search li tag
    for li_tag in qalst:
        a_tag = li_tag[0][0][0]
        a_attrib = a_tag.attrib

        # access detail page
        detail_dom = getDOM(a_attrib['href'])

        # get question
        div_question = detail_dom.xpath('//div[@class="ptsQes"]')
        p_question_1 = div_question[0][0].text_content()
        p_question_2 = div_question[0][1].text_content()
        question = p_question_1.strip() + p_question_2.strip()
        f_question.write(question)

        # get a best answer
        best_answer = div_question[0].text_content()
        best_answer = div_question[1][0].text_content()
        best_answer = best_answer.strip()
        f_answer.write(best_answer)
f_question.close()
f_answer.close()
