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

letter=ea.choicebox(msg='Password letter',title="Select",choices=["2",'3','4'])
letter1=string.ascii_lowercase
l1=random.choice(letter1)
letter2=string.ascii_lowercase
l2=random.choice(letter2)
letter3=string.ascii_lowercase
l3=random.choice(letter3)
letter4=string.ascii_lowercase
l4=random.choice(letter4)
if letter == '2':
    result= l1 + l2 + str((a+b+c+d+e+f+g+h+i+j)/10)
elif letter == '3':
    result= l1 + l2 + l3 + str((a+b+c+d+e+f+g+h+i+j)/10)
else:
    result= l1 + l2 + l3 + l4 + str((a+b+c+d+e+f+g+h+i+j)/10)




ea.msgbox(result,title='result')
