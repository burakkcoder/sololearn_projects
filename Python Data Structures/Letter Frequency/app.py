word = input()
letter = input()
count = word.count(letter)
print(int(count / len(word) * 100))