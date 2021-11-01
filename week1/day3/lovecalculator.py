# This part is for the input
print("welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("what is their name? \n")

#you should now have two variables.



both_names = name1 + name2
lowercase_both_names = both_names.lower()

print(name1  +  name2)

t = lowercase_both_names.count("t")
r = lowercase_both_names.count("r")
u = lowercase_both_names.count("u")
e = lowercase_both_names.count("e")
true = t + r + u + e

l = lowercase_both_names.count("l")
o = lowercase_both_names.count("o")
v = lowercase_both_names.count("v")
e = lowercase_both_names.count("e")
love = l + o + v + e

love_score = int(str(love) + str(true))

if (love_score < 10) or (love_score > 90):
    print("your love score is {love_score}, you go together like mentos and coke")
elif (love_score >= 50) and (love_score <= 90):
    print("your love score is {love_score}, it must be love!")
