#正则表达式中的分割
# import re
#
# p = r'\d+'
# text = 'AB12CD34EF'
#
# clist = re.split(p,text)
# print(clist)
#
# clist = re.split(p, text, maxsplit=1)
# print(clist)
#
# clist = re.split(p, text, maxsplit=2)
# print(clist)


#文件操作



# f = open('test.txt','w+')
# f.write('World')
#
# f = open('test.txt','r+')
# f.write('Hello')
#
# f = open('test.txt','a')
# f.write(' ')
#
# fname=r'C:\Users\Dell\PycharmProjects\PYadvance\test.txt'
# f = open(fname,'a+')
# f.write('World')
#
#
# f_name = 'test.txt'
# try :
#     f = open (f_name)
# except OSError as e:
#     print('打开文件失败')
# else:
#     print('打开文件失败')
#     try:
#         content = f.read()
#         print(content)
#     except OSError as e:
#         print('处理OSError异常')
#     finally:
#         f.close()
#
# #使用with as自动资源管理
# with open(f_name,'r') as f:
#     content = f.read()
#     print(content)
#
#
# #文件的读写
# f_name = 'test.txt'
#
# with open(f_name, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     print(lines)
#     copy_f_name = 'copy.txt'
#     with open(copy_f_name, 'w', encoding='utf-8') as copy_f:
#         copy_f.writelines(lines)
#         print('文件复制成功')


