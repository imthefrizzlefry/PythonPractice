


def index_all(source_list, search_term):
    result_indexes = []

    for index, val in enumerate(source_list):
        if type(val) is list:
            for sub_val in index_all(val, search_term):
                result_indexes.append([index] + sub_val)
        else:
            if val == search_term:
                result_indexes.append([index])

    return result_indexes





if __name__ == "__main__":
    inputs = [
        (([[[1,2,3],2,[1,3]],[1,2,3]],2), [[0,0,1], [0,1],[1,1]])
    ]

    for pair in inputs:
        value = pair[0]
        expected_result = pair[1]

        actual_result = index_all(value[0], value[1])

        print("{} => {}".format(value, actual_result))
        assert actual_result == expected_result
