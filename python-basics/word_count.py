sentence = input("Enter a sentence: ")
count = {}

for word in sentence.split():
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

print(count)
