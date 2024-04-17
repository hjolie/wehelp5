# ======================== Task 1 ======================== #
import urllib.request as request
import json, re, csv

url1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

with request.urlopen(url1) as response1:
    data1 = json.load(response1)
with request.urlopen(url2) as response2:
    data2 = json.load(response2)

spot_list = data1["data"]["results"]
mrt_list = data2["data"]

with open("spot.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for spot in spot_list:
        for mrt in mrt_list:
            if mrt["SERIAL_NO"] == spot["SERIAL_NO"]:
                district = mrt["address"].replace(" ", "")[3:6]
                pattern = r"https://[^\s]+?\.(jpg|jpeg|JPG|JPEG)"
                match = re.search(pattern, spot["filelist"])
                if match:
                    # Extract the first url from the match object
                    url = match.group(0)
                writer.writerow([spot["stitle"], district, spot["longitude"], spot["latitude"], url])

# --------------------------------------------

# Create a dict to store spots associated with mrt stations
# key: mrt stn, value: [spot1, spot2...]
dic = {}
for mrt in mrt_list:
    # Create a new key with empty list if not existing
    if mrt["MRT"] not in dic:
        dic[mrt["MRT"]] = []
    for spot in spot_list:
        if mrt["SERIAL_NO"] == spot["SERIAL_NO"]:
                dic[mrt["MRT"]].append(spot["stitle"])

with open("mrt.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    # Store stations and spots in two separate lists
    # and combine each station and associated spots to same rows
    # based on the index i
    rows = []
    spots_list = []
    
    for station, spots in dic.items():
        rows.append([station])
        spots_list.append(spots)
    
    for i in range(len(rows)):
        rows[i].extend(spots_list[i])
    
    writer.writerows(rows)

# ======================== Task 2 ======================== #
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
            pushlish_time = get_time(article_link)
            if likes[i].span != None:
                like_count = likes[i].span.string
            else:
                like_count = "0"
            result_list.append([article_title, like_count, pushlish_time])

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