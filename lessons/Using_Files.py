text_filev = open("textfile.txt","r") 
print(text_filev.readline())
#print(text_filev.read())

for t in text_filev.readlines():
    print (t)

text_filev.close()

text_filev = open("textfile.txt","a") 
text_filev.write("\nHaha")
text_filev.close()

text_filev = open("textfile.txt","w") 
text_filev.write("Hello")
text_filev.close()