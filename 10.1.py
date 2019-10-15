# def mianji(height,width):
#     result = width*height
#     return result
#
# result_a=mianji(4,5)
# print("this square's area is {0:.2f}".format(result_a))



# def sum(*numbers,multiple=1):
#     total=0.0
#     for number in numbers:
#         total+=number
#     return total*multiple
# print(sum(30.0,80.0))


def show_info(sep=':',**info):
    print('----info----')
    for key,value in info.items():
        print('{0}  {2}  {1}'.format(key,value,sep))
    return None
# print(show_info('->',name='tony',age=18,sex='ture'))
s=show_info('->',name='tony',age=18,sex= 'ture')
print(s)
# def show_info(sep=':',**info):
#     print('----info----')
#     for key,value in info.items():
#         print('{0}  {2}  {1}'.format(key,value,sep))
# print(show_info('->',**{'name':'tony','age':18,'sex':'ture'}))