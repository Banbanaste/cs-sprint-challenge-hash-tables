def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create dictionary of indecies and values needed to equal the limit
    weights_dict = {i: limit - weights[i] for i in range(0, length)}
    # return None if no tuple is created
    answer = None
    # loop through dictionary and compare if value is in original weights list
    for j in weights_dict:
        if weights_dict[j] in weights:
            # if value is in weights list save both indecese to tuple
            # could save just the dict key and construct the tuple outside of this for loop as well
            answer = (j, weights.index(weights_dict[j]))
    # return tuple or None
    return answer
