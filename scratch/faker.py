import random
ccs = ['cc0','cc1','cc2','cc3','cc4','cc5','cc6','cc7','cc8','cc9','cc10','cc11','cc12','cc13','cc14','cc15','cc16','cc17','cc18','cc19']
genres = ['history','pizza','arrows','milk']
for i in range(1,97):
    j = str(i)
    print("'text_" + j + "' : { ")
    print("'id' : 't" + j + "',")
    print("'genre' : '" + genres[random.randint(0,4) + "',"]
    print("'date' : " + str(random.randint(-100,1500)) + ",")
    print("'chars' : " + "['a','b','c','d'],")
