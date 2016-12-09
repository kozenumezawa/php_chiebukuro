# -*- coding: utf-8 -*-

import lxml.html
import requests
import codecs

def getDOM(target_url):
    target_html = requests.get(target_url).text
    dom = lxml.html.fromstring(target_html)
    return dom

def deleteSpace(lines):
    text = ""
    for line in lines:
        text += line.rstrip('\r\n')
    return text
f_question = codecs.open('love_question.txt', 'w', 'utf-8')
f_answer = codecs.open('love_answer.txt', 'w', 'utf-8')

f = open('url.txt')
url = f.read()
f.close()

for i in range(50):
    print(i)
    open_url = url.strip() + str(i+1)
    top_dom = getDOM(open_url)
    qalst = top_dom.get_element_by_id('qalst')

    # scraping from each question page
    for li_tag in qalst:
        a_tag = li_tag[0][0][0]
        a_attrib = a_tag.attrib

        # access detail page
        detail_dom = getDOM(a_attrib['href'])

        # get question
        div_question = detail_dom.xpath('//div[@class="ptsQes"]')
        p_question_1 = div_question[0][0].text_content()
        question = p_question_1.strip()

        question_attr = div_question[0][0].attrib
        if not question_attr.has_key('class'):
            p_question_2 = div_question[0][1].text_content()
            question += p_question_2.strip()

        # f_question.write(question.strip())  # delete \n
        f_question.write(deleteSpace(question))
        f_question.write('\n')

        # get a best answer
        best_answer = div_question[1][0].text_content()
        f_answer.write(deleteSpace(best_answer))  # delete \n
        f_answer.write('\n')

f_question.close()
f_answer.close()
