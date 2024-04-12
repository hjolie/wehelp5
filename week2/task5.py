def find(spaces, stat, n):
    # Extract car indices of 1 to a list
    available_car_index_list = [index for index, car in enumerate(stat) if car == 1]

    # Extract available spaces to a list based on car indices
    available_spaces_list = []
    for space_index, space in enumerate(spaces):
        for car_index in available_car_index_list:
            if space_index == car_index:
                available_spaces_list.append(space)

    # Find the most fitted car
    stat_of_found = ""
    space_difference_list = []
    for spaces in available_spaces_list:
        if spaces == n:
            stat_of_found = "Found Exact Spaces"
            index = available_spaces_list.index(spaces)
            the_most_fitted_car_index = available_car_index_list[index]
            break
        elif spaces > n:
            difference = spaces - n
            space_difference_list.append(difference)
            stat_of_found = "Found"
        elif spaces < n:
            stat_of_found = "Not Found"
    
    # Print car index based on stat of found
    if stat_of_found == "Found Exact Spaces":
        print(the_most_fitted_car_index)
    elif stat_of_found == "Found":
        min_space_difference = min(space_difference_list)
        index = space_difference_list.index(min_space_difference)
        the_most_fitted_car_index = available_car_index_list[index]
        print(the_most_fitted_car_index)
    elif stat_of_found == "Not Found":
        print(-1)


find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
print()
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
print()
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2