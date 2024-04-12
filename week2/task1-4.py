# ------------------------- Task 1 ------------------------- #
messages={
"Leslie":"I'm at home near Xiaobitan station.", # 15.5 or 16.5
"Bob":"I'm at Ximen MRT station.", # 7
"Mary":"I have a drink near Jingmei MRT station.", # 14
"Copper":"I just saw a concert at Taipei Arena.", # 2
"Vivian":"I'm at Xindian station waiting for you." # 18
}

def find_and_print(messages, current_station):
    # Extract names and messages to two seperate lists
    name_list = [name for name, message in messages.items()]
    message_list = [message for name, message in messages.items()]

    green_line = {
    "Songshan": 0,
    "Nanjing Sanmin": 1,
    "Taipei Arena": 2,
    "Nanjing Fuxing": 3,
    "Songjiang Nanjing": 4,
    "Zhongshan": 5,
    "Beimen": 6,
    "Ximen": 7,
    "Xiaonanmen": 8,
    "Chiang Kai-Shek Memorial Hall": 9,
    "Guting": 10,
    "Taipower Building": 11,
    "Gongguan": 12,
    "Wanlong": 13,
    "Jingmei": 14,
    "Dapinglin": 15,
    "Qizhang": 16,
    "Xiaobitan": 15.5,
    "Xindian City Hall": 17,
    "Xindian": 18
    }

    # Extract stations to a list
    green_line_station_list = [station for station, num in green_line.items()]
    # Extract station values to a list
    green_line_num_list = [num for station, num in green_line.items()]
    
    # Find current station index from green line station list
    current_station_index = green_line_station_list.index(current_station)
    # Find current station value based on the current station index
    current_station_num = green_line_num_list[current_station_index]

    distance_list = []
    same_station = False

    for message in message_list:
        for station in green_line_station_list:
            if station in message:
                # Find which message and station (index)
                message_index = message_list.index(message)
                station_index = green_line_station_list.index(station)

                # Set different values for "Xiaobitan" based on the current station
                if station == "Xiaobitan" and current_station_num < 16:
                    station_num = 16.5
                elif station == "Xiaobitan" and current_station_num > 16:
                    station_num = 15.5
                else:
                    station_num = green_line_num_list[station_index]
                
                # Calculate distance
                if current_station_num == station_num:
                    same_station = True
                    friend_at_same_station = name_list[message_index]
                elif current_station_num > station_num:
                    distance = current_station_num - station_num
                    distance_list.append(distance)
                elif current_station_num < station_num:
                    distance = station_num - current_station_num
                    distance_list.append(distance)
    
    # Find the minimum distance and print the name
    if same_station == True:
        print(friend_at_same_station)
    else:
        min_distance = min(distance_list)
        min_distance_index = distance_list.index(min_distance)
        the_nearest_friend = name_list[min_distance_index]
        print(the_nearest_friend)


print("--------------------------- Task 1 ---------------------------")
print()
find_and_print(messages, "Wanlong") # print Mary
print()
find_and_print(messages, "Songshan") # print Copper
print()
find_and_print(messages, "Qizhang") # print Leslie
print()
find_and_print(messages, "Ximen") # print Bob
print()
find_and_print(messages, "Xindian City Hall") # print Vivian
print()
print("--------------------------- Task 2 ---------------------------")
print()

# ------------------------- Task 2 ------------------------- #

consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]

booked_times_by_price = {}
booked_times_by_rate = {}

def book(consultants, hour, duration, criteria):
    # Re-arrange the consultants based on price (lowest --> highest)
    prices = [consultant["price"] for consultant in consultants]
    sorted_prices = sorted(prices)
    sorted_consultants_by_price = [consultant for price in sorted_prices for consultant in consultants if consultant["price"] == price]

    # Extract the names from sorted consultants by price
    names_by_price = [consultant["name"] for consultant in sorted_consultants_by_price]

    # Create a dic for storing booked times (if not done yet)
    # based on the order of sorted consultants by price
    # key: name, value: list of booked times (hours)
    if booked_times_by_price == {}:
        for i in range(len(sorted_consultants_by_price)):
            booked_times_by_price[names_by_price[i]] = []

    #Re-arrange the consultants based on rate (highest --> lowest)
    rates = [consultant["rate"] for consultant in consultants]
    sorted_rates = sorted(rates, reverse=True)
    sorted_consultants_by_rate = [consultant for rate in sorted_rates for consultant in consultants if consultant["rate"] == rate]

    # Extract the names from sorted consultants by rate
    names_by_rate = [consultant["name"] for consultant in sorted_consultants_by_rate]

    # Create a dic for storing booked times (if not done yet)
    # based on the order of sorted consultants by rate
    # key: name, value: list of booked times (hours)
    if booked_times_by_rate == {}:
        for i in range(len(sorted_consultants_by_rate)):
            booked_times_by_rate[names_by_rate[i]] = []

    # Store requested times in a list based on hour & duration
    requested_times = []
    time = hour
    requested_times.append(time)
    if duration > 1:
        for i in range(duration - 1):
            time += 1
            requested_times.append(time)
    
    # Check if the requested time slot is available based on price or rate
    if criteria == "price":
        availability = True
        for key, value in booked_times_by_price.items():
            # Check if there is common elements between booked times and requested times
            booked_times_set = set(value)
            requested_times_set = set(requested_times)
            if booked_times_set.intersection(requested_times_set) == set():
                availability = True
                available_consultant = key
                break
            else:
                availability = False
        if availability == False:
            print("No Service")
        else:
            print(available_consultant)
            value.extend(requested_times)
            booked_times_by_rate[available_consultant].extend(requested_times)
    else:
        availability = True
        for key, value in booked_times_by_rate.items():
            # Check if there is common elements between booked times and requested times
            booked_times_set = set(value)
            requested_times_set = set(requested_times)
            if booked_times_set.intersection(requested_times_set) == set():
                availability = True
                available_consultant = key
                break
            else:
                availability = False
        if availability == False:
            print("No Service")
        else:
            print(available_consultant)
            value.extend(requested_times)
            booked_times_by_price[available_consultant].extend(requested_times)


book(consultants, 15, 1, "price") # Jenny: 15, 16
print()
book(consultants, 11, 2, "price") # Jenny: 11, 12, 13
print()
book(consultants, 10, 2, "price") # John: 10, 11, 12
print()
book(consultants, 20, 2, "rate") # John: 20, 21, 22
print()
book(consultants, 11, 1, "rate") # Bob: 11, 12
print()
book(consultants, 11, 2, "rate") # No Service 11, 12, 13
print()
book(consultants, 14, 3, "price") # John: 14, 15, 16, 17
print()
print("--------------------------- Task 3 ---------------------------")
print()

# ------------------------- Task 3 ------------------------- #

from collections import Counter

def func(*data):
    # Extract each middle name out to a list
    middle_name_list = []
    for fullname in data:
        if len(fullname) == 2 or len(fullname) == 3:
            middle_name = fullname[1]
        elif len(fullname) == 4 or len(fullname) == 5:
            middle_name = fullname[2]
        middle_name_list.append(middle_name)

    # Find the unique middle name from the list above
    unique_middle_name = find_unique_middle_name(middle_name_list)

    # Print the fullname with unique middle name
    if unique_middle_name != "":
        index = middle_name_list.index(unique_middle_name)
        print(data[index])
    else:
        print("沒有")

def find_unique_middle_name(my_list):
    # Concatenate all the middle names into one (string)
    middle_names = "".join(my_list)

    # Count the occurrences of each middle name
    middle_name_counts = Counter(middle_names)

    # Filter out the middle name that appear only once
    unique_middle_name = ""
    for name, count in middle_name_counts.items():
        if count == 1:
            unique_middle_name = name

    return unique_middle_name


func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
print()
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
print()
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
print()
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
print()
print("--------------------------- Task 4 ---------------------------")
print()

# ------------------------- Task 4 ------------------------- #

def get_number(index):
    num_list = []

    for i in range(index*4):
        if i % 7 == 0:
            num_list.append(i)
            num_list.append(i + 4)
            num_list.append(i + 8)
    
    print(num_list[index])


get_number(1) # print 4
print()
get_number(5) # print 15
print()
get_number(10) # print 25
print()
get_number(30) # print 70
print()