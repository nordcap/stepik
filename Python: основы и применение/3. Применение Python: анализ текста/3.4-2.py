"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на
которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением
случаев с относительными ссылками вида
<a href="../some_path/index.html">﻿.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""

# ==================================================================================
# text = "<a href=\"http://stepic.org/courses\">"
# text = "<a href='https://stepic.org'>"
# text = "<a href='http://neerc.ifmo.ru:1345'>"
# text = "<a href=\"ftp://mail.ru/distib\">"
# text = "<a href=\"ya.ru\">"
# text = "<a target=\"_blank\" name=\"namelink\" href=\"www.ya.ru\">"
# text = "<a href=\"../skip_relative_links\">"

import requests, re, sys

for line in sys.stdin:
    line = line.strip()
    #request = requests.get(line)
    #text = request.text


    text = """<a href="http://www.liveinternet.ru/click" target=_blank><img src="http://pics.rbc.ru/img/ver99/counter_liveinternet.gif" border=0 width=31 height=31 title="liveinternet.ru"></a>
            <a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turist.ru/goods/"><img width=150 height=100 alt="turbo.ru" src="http://turbo.ru/turbo_pics/uniora/90/240/350/a839c3fac974f93478606906dda54e77_150x100.jpg"></a><br>';
            <li><a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.nissan-avtogrand.ru/news/news.php?id=40">Суперусловия по покупке автомобилей Nissan 2008 г.в.</a></li>
            <li><a href='http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459494' >В Сеуле дебютирует седан KIA VG</a></li><li><a href='http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459452' >Российский завод Toyota остановил производство на неделю</a></li><li><a href='http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459434' >Сегодня Путин проведет совещание на АвтоВАЗе</a></li>"""
    all_body_link = re.findall(r"<a\s+([\w*|\s*|=|\'|\"|\.|:|//|-]*)", text)

    arr_link = []
    for one_link in all_body_link:
        link = re.findall(r"href=(?:\"|\')(?:https://|http://|ftp://)?(?!\.{2}/)(?P<domen>[\w\d\.-]+)(?:\"|\'|/|:)",
                          one_link)
        if len(link) > 0:
            arr_link.append(link[0])

    list_link = list(set(arr_link))
    list_link.sort()
    for link in list_link:
        print(link)
