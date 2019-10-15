# def position(dt,speed):
#     posx=speed[0]*dt
#     posy=speed[1]*dt
#     return(posx,posy)
#
# move=position(60.0,(10,-5))
# print("physics displacement:({0},{1})".format(move[0],move[1]))

# def square(num):
#     list_n=[]
#     for i in range(1,num+1):
#         list_n.append(i*i)
#     # print(list_n)
#     return list_n
#
# for i in square(5):
#     print(i  ,end=' ')



def f1():
    for i in range(10):
        print(i)
        i +=1
        yield i
        # return i
f=f1()
next(f)
next(f)
next(f)

