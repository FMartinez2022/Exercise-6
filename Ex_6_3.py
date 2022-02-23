def count(word, letter) :
    count = 0
    for character in word:
        if character == letter:
            count = count + 1
    print(count)


input_word = input('Enter word')
input_letter = input('Enter letter you want counted')
count(input_word, input_letter)
