def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # init empty list to add converted lists
    dicts_list = []
    # loop appending created dicts from original lists
    for i in arrays:
        dicts_list.append({j: 0 for j in i})
    # init result dict
    result = dicts_list.pop()
    # loop comparing dicts_list dicts w/ result dict and leaving only the intersection keys
    for j in dicts_list:
        result = result & j.keys()
    # convert dict to list
    return list(result)


if __name__ == "__main__":
    arrays = []

    arrays.append([1, 2, 3, 4, 5])
    arrays.append([12, 7, 2, 9, 1])
    arrays.append([99, 2, 7, 1, ])

    print(intersection(arrays))
