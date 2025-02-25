# a=30
# b=10

# print("the multiply the two number",a*b)
# a=int(input("types an integer:"))
# b=int(input("types an interger"))
# if((a*b)<1000):
#     print(a*b)
# else:
#     print(a+b)
# price=int(input("types an integer:"))
# if price>100:
#     print("price is greate then 100")
# elif price == 100:
#     print("price is 100")
# elif price < 100:
#     print("price is less than 100")

# if price==100:
#     print("price is equal")

# if price < 100:
#     print("price is less")
for i in range(11):
    print(i)
previous_num  =0
for i in range(1,10):
    x_sum = previous_num + i
    print("current Number",i,"previous Number",previous_num,"sum",x_sum)
    previous_num=i
