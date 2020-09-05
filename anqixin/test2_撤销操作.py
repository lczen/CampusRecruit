words = 'hello undo hello undo redo world'
word_list = list(words.split())

stack = []
undo_count = 0
redo_count = 0
for item in word_list:
    stack.append(item)

word_reverse = []
while stack:
    word = stack.pop()
    if word == 'redo':
        redo_count += 1
        stack.pop()
    elif word == 'undo':
        if redo_count > 0:
            redo_count -= 1
        else:
            stack.pop()
        stack.pop()

    else:
        word_reverse.append(word)
word_reverse.reverse()
print(word_reverse)