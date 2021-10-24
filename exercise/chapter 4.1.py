while True:
    def is_palindrom(word):
        if word[::-1] == word:
            return True
        return False
    spam = input('enter any palindrom word: ')
    print(is_palindrom(spam))
