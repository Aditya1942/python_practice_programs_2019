def word_count(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    print(count)
word_count("aditya parmar")