# #构建实例变量
#  class Animal(object):
#      """定义动物类"""
#      def __init__(self,age,sex,weight):
#          self.age=age
#          self.sex=sex
#          self.weight=weight
#
#  animal = Animal(2, 1, 10.0)
#
#  print('age:{0}'.format(animal.age))
#  print('sex:{0}'.format('male' if animal.sex==0 else'female'))
#  print('weight:{0}'.format(animal.weight))


#构建类变量
# class Account:
#     """定义银行账户"""
#
#     interest_rate=0.0668    #类变量利率
#
#     def __init__(self,owner,amount):
#         self.owner=owner
#         self.amount=amount
#
#
# account1=Account('tony',1_800_000.0)
# account2=Account('miku',200_000_000.0)
#
# print('账户名：{0}'.format(account1.owner))
# print('账户金额：{0}'.format(account1.amount))
# print('利率：{0}'.format(account1.interest_rate))
#
# print('账户名：{0}'.format(account2.owner))
# print('账户金额：{0}'.format(account2.amount))
# print('利率：{0}'.format(Account.interest_rate))


# def soft(a):                                   #函数式编程
#      print("账户为：{0}".format(a[0]))
#      print("账户金额：{0}".format(a[1]))
#      return ' '
#
#  print(soft(('tony',1_800_000.0)))
#  print(soft(('miku',200_000_000.0)))


# class Animal(object):
#     """定义动物类"""
#
#     def __init__(self, age, sex=1, weight=0.0):
#         self.age = age
#         self.sex = sex
#         self.weight = weight
#
#     def eat(self):
#         self.weight+=0.05
#         print('eat...')
#
#     def run(self):
#         self.weight-=0.01
#         print('run...')
#
# a1=Animal(2, 0, 10.0)
#
# print('a1体重：{0:0.2f}'.format(a1.weight))
# a1.eat()
# print('a1体重：{0:0.2f}'.format(a1.weight))
# a1.run()
# print('a1体重：{0:0.2f}'.format(a1.weight))


# class Account:
#     """定义银行账户类"""
#
#     interest_rate = 0.0668       #类变量利率
#
#     def __init__(self,owner,amount):
#         self.owner=owner         #实例变量
#         self.amount=amount
#
#     #类方法
#     @classmethod
#     def interest_by(cls,amt):
#         return cls.interest_rate*amt
#
#     @staticmethod
#     def interest_with(amt):
#         return Account.interest_by(amt)
#
#
# interest1 = Account.interest_by(12_000.0)
# print('计算利息：{0:.4f}'.format(interest1))
# interest2 = Account.interest_with(12_000.0)
# print('计算利息: {0:.4f}'.format(interest2))


# weight=999
# class Animal(object):
#     """定义动物类"""
#     def __init__(self, age, sex=1, weight=0.0):
#         self.age = age
#         self.sex = sex
#         self.__weight= weight               #定义了体重实例变量（私有的）
#
#     def eat(self):
#         self.__weight += 0.05
#         print('eat...={0:.2f}'.format(self.__weight))    #内部调用？
#
#     def run(self):
#         self.__weight -= 0.01
#         print('run...')
#
# a1=Animal(2, 0, 10.0)
#
# print('ai的体重: {0:0.2f}'.format(a1.weight))
# a1.eat()
# a1.run()


#继承性
class Person:
     def __init__(self,name,age):
         self.name = name                      #name
         self.age = age                        #age

     def info(self):
         template = 'Person [name={0}, age={1}]'
         s = template.format(self.name, self.age)
         return s


# print('{0}'.format(li.info()))     #different way



#继承性
class Student(Person):

    def __init__(self, name, age, school):
        super().__init__(name, age)
        # self.name=name
        # self.age=age
        self.school=school               #所在学校


    def info(self):
        template = 'School [name={0}, age={1}, school={2}]'
        s = template.format(self.name, self.age, self.school)
        return s

li=Person("李四", 19)
ha=Student("Puppy", 3, "郧阳中学")
print(li.info())
print(ha.info())
