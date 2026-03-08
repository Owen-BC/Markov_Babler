from main import word_dict 

def main():

    test = word_dict('there')
    test.update_word('hello', 'friend')
    test.update_word('hello', 'friend')
    test.update_word('hello', 'stranger')
    print(test.get_random_child(None))


if __name__ == "__main__":
    main()