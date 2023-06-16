# Write a file

#create a variable of text to be added
text= 'City boiiiiiiii\nThis is some amazing stuff you doing here\nKeep on mate'

with open("File detection.txt",'w') as file:
    file.write(text)

#To append a file, we change to append mode 'a'

text='\nHave a nice day\nSee ya!'

with open("File detection.txt","a")as file:
    file.write(text)