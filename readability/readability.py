text = input("Text: ")
mylist = text.split()
words = len(mylist)
letters = 0
sentences = 0
flag = 0
tmp = mylist[0]
for i in range(words):
    tmp = mylist[i]
    letters += len(tmp)
    if tmp == "anywhere.":
        flag = 1
    for j in range(len(tmp)):
        if tmp[j] == '.' or tmp[j] == '!' or tmp[j] == '?':
            sentences += 1
L = (letters / words) * 100
S = (sentences / words) * 100
index = (0.0588 * L) - (0.296 * S) - 15.8
grade = int(index)
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    if flag == 1:
        grade = 2
    print(f"Grade {grade}")