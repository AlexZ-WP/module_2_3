my_list = [42, 69, 322,13, 0, 99, -5, 9, 8, 7, -6, 5]
while 0 in my_list:
    my_list.remove(0)
a = 0
while my_list[a] > 0 and a < len(my_list):
    print(my_list[a])
    a += 1