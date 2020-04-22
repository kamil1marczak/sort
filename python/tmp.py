

word = 'Wolnoxtariusz41!'

def split(word):
    return [char for char in word]

b={}

word_list = split(word)

for i in range(len(word)):
    b.update({i:word[i]})

print(b)