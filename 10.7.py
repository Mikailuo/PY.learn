# def calculate_fun(opr):
#     if opr =='+':
#         return lambda a,b:(a+b)
#     else:
#         return lambda a,b:(a-b)
#
# f1=calculate_fun('+')
# f2=calculate_fun('-')
#
# print("10+5={0}".format(f1(10,5)))
# print("10-5={0}".format(f2(10,5)))     #函数式编程

# users=['tony','tom','ben','alex']
# users_filter=filter(lambda u:u.startswith('t'),users)
#
# print(list(users_filter))              #lambda表达式+filter过滤操作


from functools import reduce
a=(1,2,3,4)
a_reduce=reduce(lambda c,i:c+i,a)
print(a_reduce)


