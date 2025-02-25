'''def greet(name):
    print ("hello,"+ name +".Good Morning!")
greet("Sugam")'''

'''def absolute_value(num):
    if num>=0:
        return num
    else:
        return -num
print(absolute_value(2))
print(absolute_value(-4))
print(absolute_value(0))'''

'''def greet ( name ,msg='good morning'):
    print("hello "+name+','+msg)


greet("ram bahadur")
greet("shayam bahadur","how do you do?")'''
"""""
def greet(*names):
    for name in names:
        print("hello,hi",name)
greet("gita")
greet("Ram", "shyam","hari","sita")"""""

"""""
def calc_function(x):
    if x==1:
        return 1
    else:
        return(x*calc_function(x-1))
num=4
print("the factorial of",num,"is",calc_function(num))"""

#lambda function'''
'''''
double=lambda x:x*2
square= lambda y:y**2

print(double(5))'''''
'''''
my_list=[1,5,6,8,11,3,12]

odd_list=list(filter(lambda))'''''
'''''
x = "global"
def foo():
    global x
    y='local'
    x= x*2
    print(x)
    print(y)
foo()
print(x)

x=5
def hel():
    global x
    x=10
    print("local x:",x)
hel()
print(x)'''''

def foo():
    x=20
    def bar():
        global x
        x=25
    print("before",x)
    print("calling bar")
    bar()
    print("after",x)
foo()
print("x in main",x)
 
