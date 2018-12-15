# Sessions 11&12
# No homework
# Excercises:
# Determine the longest word in a text file

x = open('words','r')
l = x.readlines()
listofwords = l[0]
listsplit = listofwords.split()

d = []
for i in listsplit:
   d.append(len(i))
   longest = max(d)

for j in listsplit:
   if len(j) == longest:
       print (j, "-", len(j),"- letters long")

# Print out only the words that appear more than 2 times in a file

f = []
b=[]
def repeated_words():
   for j in listsplit:
       f.append(str(j))

   f.sort()
   print(f)

   for r in f:
       if f.count(r) == 2:
           print(r)


