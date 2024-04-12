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


find_and_print(messages, "Wanlong") # print Mary
print()
find_and_print(messages, "Songshan") # print Copper
print()
find_and_print(messages, "Qizhang") # print Leslie
print()
find_and_print(messages, "Ximen") # print Bob
print()
find_and_print(messages, "Xindian City Hall") # print Vivian