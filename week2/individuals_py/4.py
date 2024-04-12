
# 0, 4, 8,
# 7, 11, 15,
# 14, 18, 22,
# 21, 25, ...

# 0               + 4 + 4
# 0 + 7           + 4 + 4
# 0 + 7 + 7       + 4 + 4


def get_number(index):
    # your code here
    num_list = []

    for i in range(index*4):
        if i % 7 == 0:
            num_list.append(i)
            num_list.append(i + 4)
            num_list.append(i + 8)
    
    print(num_list[index])


get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70