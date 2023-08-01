def deduplicate(input_list: list) -> list:
    """
    Remove duplicates from the input list while preserving their order of appearance.
    Args:
        input_list (list): The list containing elements with possible duplicates.
    Returns:
        list: A new list containing only the duplicate elements in the order of their appearance.
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    duplicated = []
    index_next = 1
    for item in input_list:
        if item in duplicated:
            index_next += 1
            continue
        for next_item in input_list[index_next:]:
            if item == next_item:
                duplicated.append(item)
                break
        index_next += 1
    return duplicated


# @profile
def deduplicate_new(input_list: list) -> list:
    seen = []
    duplicates = []
    for item in input_list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.append(item)
    return duplicates

# input = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]

# print(deduplitace(input))
# print(deduplicate_new(input))
# @profile
# def find_duplicates_set(input_list):
#     seen = set()
#     duplicates = set()
#     for item in input_list:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#     return list(duplicates)
