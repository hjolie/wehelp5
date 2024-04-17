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