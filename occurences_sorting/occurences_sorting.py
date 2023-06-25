def resolve(input: list[int] = []) -> list[int]:
    result = []

    occurences_set = set(input)
    count_map: dict[str, list[int]] = {}
    for num in occurences_set:
        count = input.count(num)
        if not count_map.get(count):
            count_map.setdefault(count, [num])
        else:
            count_map[count].append(num)

    count_list = [*count_map.keys()]
    count_list.sort()

    for count in count_list:
        nums = count_map[count]*count
        nums.sort(reverse=True)
        result += nums

    return result

print(resolve([1, 1, 3, 4, 2, 2, 2, -2, -2]))
