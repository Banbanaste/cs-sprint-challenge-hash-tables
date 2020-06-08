def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create dict of negative and positive pairs (actual values as keys)
    pairs_dict = {i: i * -1 for i in a}
    # create array from positive keys checking if there is a pair and if the key will return a positive integer
    result = [pairs_dict[pairs_dict[key]]
              for key in pairs_dict if key * -1 in pairs_dict and key > 0]
    # return list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
