# name = 'ada lovelace'
# print(name.title())

# age = 18

# message = 'happy' + str(age) + 'rd bithabyp'
# print(message)

# lists = ['xu', 'bin']

# lists.insert(1, 'dao')

# for i, v in enumerate(lists):
#   print(i, v)

# del lists[2]
# print(lists)

# print(sum(range(1000000)))
# print([x for x in range(3,30) if x % 3 == 0])

# players = ['charles', 'martina', 'michael', 'florence', 'eli', [1]]
# print(players[-3:])
# for x in players[:3]:
#   print(x.title())
# players[5][0] = 3
# players2 = players[:]
# players2[5][0] = 2
# print(players2, players)

# dimis = (200, 50)
# print(dimis)

# car = "AduI"
# print(car.lower())
# req = [1, 2, 3, 4]
# print(1 in req)
# print(1 not in req)
# print('a' not in req)

# lists = []
# print(not lists)
# for x in lists:
#   print(x)


# dicts = {'name': 1, 'age': 18, 'name': 2}
# print(dicts)
# print('aaAd'.lower())

# favorite_languages = {
#   'jen': 'python',
#   'sarah': 'c',
#   'edward': 'ruby',
#   'phil': 'python',
# }

# for name in sorted(favorite_languages.keys()):
#   print(name.title())

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# print(aliens)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#   message = input(prompt)
#   if message == 'quit':
#      active = False
#   else:
#       print(message)

# while True:
#   city = input(prompt)
  
#   if city == 'quit':
#     break
#   else:
#       print("I'd love to go to " + city.title() + "!")


# uncon = ['alce', 'brian', 'candace']

# confired = []

# while uncon:
#   confired.append(uncon.pop())


# for item in sorted(confired):
#   print(item.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# print(pets)
# while 'cat' in pets:
#   pets.remove('cat')

# print(pets)

# res = {}

# active = True
# def isC(name):
#   for item in res:
#     if name == item:
#       return False
#   return True

# while active:
#   name = input('请输入你的名字: ')
  # while 循环版
  # while name in res:
  #   print('名字重复，请重新输入.')

  # 自写函数continue版本
#   if not isC(name):
#     print('名字重复，请重新输入.')
#     continue
#   response = input('请输入你的建议: ')
#   res[name] = response
#   rep = input('是否是否还有人继续接受调查 y/n')

#   if rep == 'no':
#     active = False

# for key, val in res.items():
#   print('%s   提出了   %s\n'%(key, val))

# def make_pizza(*toppings):
#   print(toppings)


# make_pizza(1, 2, 3, 3, 4, 5, 6)

# import pizza

# pizza.mak_pizze(200, '贵的', '便宜的', '中等的', '好吃的')

# from pizza import mak_pizze, mak_pizze2

# mak_pizze(100, '榴莲', '蒜蓉', '火腿肠')

# mak_pizze2(200, *['中等的', '不好吃的', '好吃的'])

# from pizza import mak_pizze as mp

# mp(16, '123')

# import pizza as p
# p.mak_pizze(1223, '大的')

# from pizza import *

# mak_pizze(123, '大大大')

# mak_pizze2(100, *{'小小小': '小小小'})

class Dog():
  def __init__ (self, name, age):
    self.name = name
    self.age = age
  
  def sit (self):
    print(self.name.title() + '蹲下')
  
  def roll_ove (self):
    print(self.name.title() + '打滚')

dodo = Dog('小花猫', 18)

dodo.sit()
dodo.roll_ove()

print('你的小狗名字叫%s, 年龄%s' % (dodo.name, dodo.age))