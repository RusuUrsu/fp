def read(filname):
    file = open(filname,'r')
    text = file.read()

    words = text.split()

    file.close()
    return words

def show(text):
    print(' '.join(text))


def replace(text, word_to_remove, word_to_add):
    stats = []
    replaced = 0
    for i in range(len(text)):
        if text[i] == word_to_remove:
            replaced+=1
            text[i] = word_to_add
    stats.append(text)
    stats.append(replaced)
    return stats

def write(filename,text):
    file = open(filename,'w')
    file.write(' '.join(text))
    file.flush()
    file.close()

def main():
    text = read('replace.txt')
    show(text)

    word1 = input("Word to replace: ")
    word2 = input(f'Replace {word1} with: ')

    stats = replace(text,word1,word2)
    text = stats[0]
    if stats[1] > 0:
        print(f'Replaced {word1} with {word2} {stats[1]} times')
    else:
        print(f'{word1} has not been found')
    #show(text)

    write('replace.txt',text)


main()