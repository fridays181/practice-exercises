#Write a program to accept a string from the user and display characters that are present at an even index number.

x = input(": ")
xx = list(x)
for i in xx[1::2]:
    print(i)
