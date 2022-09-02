def create_diff(one_lns, two_lns):
    removed = []
    created = []
    one_full = {}
    two_full = {}
    for one_ln in one_lns:
        aut_num = int(one_ln.split(' ')[0])
        one_full[aut_num] = one_ln
        if one_ln not in two_lns:
            removed.append(aut_num)
    for two_ln in two_lns:
        aut_num = int(two_ln.split(' ')[0])
        two_full[aut_num] = two_ln
        if two_ln not in one_lns:
            created.append(aut_num)
    for create in created:
        if create in removed:
            removed.remove(create)
            formatted_a = one_full[create].replace('\n', '')
            formatted_b = two_full[create].replace('\n', '')
            print(f"CHANGE \"{formatted_a}\" TO \"{formatted_b}\"")
        else:
            formatted = two_full[create].replace('\n', '')
            print(f"CREATE \"{formatted}\"")
    for remove in removed:
        formatted = one_full[remove].replace('\n', '')
        print(f"REMOVE \"{formatted}\"")

a = open('./in_one.txt')
b = open('./in_two.txt')
diff_a = a.readlines()
diff_b = b.readlines()
a.close()
b.close()

create_diff(diff_a, diff_b)