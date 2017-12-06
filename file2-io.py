
with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

print(words[:10])


''' how many words end with an s? '''
count = 0
for w in words:
    if w[-1] == 's':
        count += 1

print(count)


''' how many words are 2 letters long? '''
count = 0
for w in words:
    count += len(w)

print(count)

count = 0
for w in words:
    if len(w) >= 7:
        count += 1

print(count)


''' how many words don't have an e? '''
count = 0
for w in words:
    if 'e' not in w:
        count += 1

print(count)

