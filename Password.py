import random
import string
import easygui as ea
from easygui.boxes.choice_box import choicebox


answer=ea.choicebox(msg="Password Numbers",title="Select",choices=["6","8","10"])

if answer == "6":
    a=random.randint(100000,999999)
    b=random.randint(100000,999999)
    c=random.randint(100000,999999)
    d=random.randint(100000,999999)
    e=random.randint(100000,999999)
    f=random.randint(100000,999999)
    g=random.randint(100000,999999)
    h=random.randint(100000,999999)
    i=random.randint(100000,999999)
    j=random.randint(100000,999999)
elif answer == '8':
    a=random.randint(100000,99999999)
    b=random.randint(100000,99999999)
    c=random.randint(100000,99999999)
    d=random.randint(100000,99999999)
    e=random.randint(100000,99999999)
    f=random.randint(100000,99999999)
    g=random.randint(100000,99999999)
    h=random.randint(100000,99999999)
    i=random.randint(100000,99999999)
    j=random.randint(100000,99999999)
else:
    a=random.randint(100000,9999999999)
    b=random.randint(100000,9999999999)
    c=random.randint(100000,9999999999)
    d=random.randint(100000,9999999999)
    e=random.randint(100000,9999999999)
    f=random.randint(100000,9999999999)
    g=random.randint(100000,9999999999)
    h=random.randint(100000,9999999999)
    i=random.randint(100000,9999999999)
    j=random.randint(100000,9999999999)
ab=string.ascii_lowercase
abc=random.choice(ab)
abs=string.ascii_lowercase
abcs=random.choice(abs)
abd=string.ascii_lowercase
abcd=random.choice(abd)

result = abc + abcs + abcd + str((a+b+c+d+e+f+g+h+i+j)/10)


print (result)