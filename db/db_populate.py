import os
import classes

path = os.getcwd()
ignores = classes.classes['ignore']
texts = os.listdir('./texts')
corpus = {}

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

class_list = removekey(classses.classes, 'ignores')

def parsetext(text_name):
    print('\n' + text_name + '\n')
    file = open(path + '/texts/' + text_name)
    loc = []
    while True:
        c = file.read(1)
        # If not a character, we've hit the end of the file
        if not c:
            break
        if (c in ignores):
            continue
        loc.append(c)
    file.close()
    return loc

for text in texts:
    corpus[text] = { 'chars' : parsetext(text) }

for key in corpus.keys():
    split = key.split('.')
    corpus[key]['id'] = split[len(split) - 2]

# def parseOneClass():
#    class_list...
