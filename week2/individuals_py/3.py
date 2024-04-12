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
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
