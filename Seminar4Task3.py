def for_task3():
    print(f"Случайная последовательность цифр:")
    new_list = [rand_num(1, 10) for i in range(1, 20)]
    print(new_list)
    result = list(filter(lambda n: new_list.count(n) == 1, new_list))

    # for i in range(len(new_list)):
    #     cnt = new_list.count(new_list[i])
    #     if cnt == 1:
    #         result.append(new_list[i])
    #     else:
    #         continue
    print(f"\nНеповторяющиеся элементы:")
    print(result)