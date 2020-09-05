def test():
    import sys
    num_name = input()
    name_list = []
    for _ in range(int(num_name)):
        name_list.append(input())
        true_name = 0
        for a in range(len(name_list)):
            if len(name_list[a]) <=10 and name_list[a].isalnum():
                true_name+=1
    return true_name
