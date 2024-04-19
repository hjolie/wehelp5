import urllib.request as request
import bs4, csv

result_list = []

def get_data(url):
    request_headers = request.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })

    with request.urlopen(request_headers) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")

    titles = root.find_all("div", class_="title")

    likes = root.find_all("div", class_="nrec")

    for i in range(len(titles)):
        if titles[i].a != None:
            article_title = titles[i].a.string
            article_link = "https://www.ptt.cc" + titles[i].find("a")["href"]
            publish_time = get_time(article_link)
            if likes[i].span != None:
                like_count = likes[i].span.string
            else:
                like_count = "0"
            result_list.append([article_title, like_count, publish_time])

    next_link = root.find("a", string="‹ 上頁")
    return next_link["href"]

def get_time(article_url):
    request_headers = request.Request(article_url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })

    with request.urlopen(request_headers) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")

    times = root.find_all("span", class_="article-meta-value")

    if times != []:
        time = times[3].string
        return time
    else:
        return ""

page_url = "https://www.ptt.cc/bbs/Lottery/index.html"
page_count = 0
while page_count < 3:
    page_url = "https://www.ptt.cc" + get_data(page_url)
    page_count += 1

with open("article.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(result_list)