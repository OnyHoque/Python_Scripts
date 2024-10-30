def library_ocd(lst):
    lst = lst.split('\n')
    new_lst = []
    for item in lst:
        if item not in new_lst and item != '' : new_lst.append(item)
    lst = new_lst
    flag = True
    while flag:
        flag = False
        for i in range(len(lst)-1):
            if len(lst[i]) > len(lst[i+1]) : lst[i], lst[i+1], flag = lst[i+1], lst[i], True
                
    for item in lst:
        print(item)