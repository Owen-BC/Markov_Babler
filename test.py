from main import word_dict 

def main():
    word_dict_add_words_test()

def word_dict_add_words_test():
    test = word_dict('there')
    test_parent_array = ['hello','hello','hello','get']
    test_child_array = ['friend','friend','stranger', 'now']
    for parent, child in zip(test_parent_array, test_child_array):
        test.update_word(parent, child)

    children, weights = test.get_all_child(None)
    print(children, weights)
    assert(children == ['friend', 'stranger', 'now'])
    assert(weights == [2, 1, 1])
    print("Passed test with none parent")


    children, weights = test.get_all_child('hello')
    print(children, weights)
    assert(children == ['now'])
    assert(weights == [1])
    print("Passed test with hello parent")

    children, weights = test.get_all_child('get')
    print(children, weights)
    assert(children == ['friend', 'stranger'])
    assert(weights == [2, 1])
    print("Passed test with get parent")

if __name__ == "__main__":
    main()