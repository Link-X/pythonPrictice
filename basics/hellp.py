# dicts = {
#     'a': 1,
#     'b': 2
# }
# dicts.pop('a')

# s = set([1, 2, 3, 4])
# s.add(2)
# s.add(6)
# print(dicts['a'])
# print('c' in dicts, 'a' in dicts)
# print(dicts.get('c', 2))
# print(dicts)

# print(s)

# print(abs(-11), abs(100))
# print(max(1, 2, 3, 4, 5, 8, 10, 5, 2))
# print(int('123'))
# print(float('123.1'))
# print(str(123))
# print(bool(12))

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('类型错误')
#     if x >= 0:
#         return x, -x
#     else:
#         return -x, x
# print(my_abs(-111))

# def power(x):
#     return x * x
# print(power(12))

# def power(x = 1, n = 2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# print(power(2, 5))

# def add_end(l = None):
#     if l is None:
#         l = []
#     l.append('END')
#     return l
# print(add_end(), add_end(), add_end([1, 2, 3]))

# def cale (numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# print(cale([1, 2, 3, 4, 5]))

# def cale2 (*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# # print(cale(1, 2, 3, 4, 5))
# num = [1, 2, 3]
# print(cale2(*num))
# ext = {
#     'city': '江西',
#     'set': '男'
# }
# def person (name, age, **kew):
#     print('name:', name, 'age:', age, 'kew:', kew)

# person('许','18', **ext)


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# print(fact(500))

# l = ['xu', 'dao', 'bin']
# l = list(range(100))
# print(l[:10:2])

# d = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
# for key in d.values():
#     print(key)

# for ch in 'abc':
#     print(ch)
# from collections import Iterable

# print(isinstance('abc', Iterable))

# print(isinstance([1, 2, 3], Iterable))

# print(isinstance(123, Iterable))

# for i, value in enumerate(['a', 'b', 'c']):
#     print(i, value)

# for x, (y, j) in enumerate([(1, 2), (2, 4), (3, 9)]):
#     print(x, y, j)

# l = [1, 2, 3, 4, 5]

# def isMax(l):
#     maxs = float()
#     for v in l:
#         if v > maxs:
#             maxs = v
#     return maxs

# print(isMax(l))

# l = []
# for x in range(1, 11):
#     l.append(x * x)

# print(l)

# print([x * x for x in range(1, 11)])

# print([x * x for x in range(1, 11) if x % 2 == 0])

# print([m + n for m in 'ABC' for n in 'XYZ'])

# import os
# print([d for d in os.listdir('.')])

# d = {'x': 1, 'y': 2, 'z': 3}

# for x, v in d.items():
#     print('%s=%f'%(x, v))

# l = ['Hello', 'World', 18, 'Apple', None]

# print([s.lower() for s in l if isinstance(s, str)])

# l = [x * x for x in range(10)]

# g = (x * x for x in l)
# # l[1] = 2
# # print(g, l)

# for x in g:
#     print(x)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while x < max:
#         # yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# g = fib(10)
# for i in g:
#     print(i)
# print([x for x in g])

# abs = 10
# abs(-10)
# def add(x, y, f):
#     return f(x) + f(y)

# print(add(1,-12, abs))

# def f(x):
#     return x * x
# r = map(f, range(1, 9))
# print(r, list(r))

# from functools import reduce
# def add(x, y):
#     return x + y
# def fn(x, y):
#     return x * 10 + y
# r1 = reduce(fn, [x for x in range(1, 10) if x % 2 != 0])
# print(r1)
# r = reduce(add, range(1, 9))

# print(r)

# l = range(1, 10)
# print(sum(l))

# from functools import reduce

# def fn(x, y):
#     return x * 10 + y
# def char2num(s):
#     digits = {'0': 0, '1': 1, '3': 3, '5': 5, '7': 7, '9': 9}
#     return digits[s]

# print(reduce(fn, map(char2num, '13579')))


# L1 = ['adam', 'LISA', 'barT']

# def normalize(name):
#     name = name[:1].upper()+name[1:].lower()
#     return name

# print(list(map(normalize, L1)))

# from functools import reduce

# def prod(l):
#     def add(x, y):
#         return x + x
#     return reduce(add, l)

# print(prod([x for x in range(1, 5)]))

# def isOdd(n):
#     return n % 2 == 1
# print(list(filter(isOdd, [1, 2, 4, 5, 6, 9, 10 ,15])))

# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty, ['a', '', 'b', '', 'c', ''])))


# print(sorted([35, 5, 11, -10, 2, 5], key = abs))

# def lazy_sum (*args):
#     def sums ():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sums

# f = lazy_sum(1, 2, 3)
# print(f())

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f
#     return fs

# f1, f2, f3 = count()
# print(f3())

# def count():
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs
# f1, f2, f3 = count()
# print(f3())

# print(list(map(lambda x: x * x, range(1, 10))))

# f = lambda x: x * x
# print(f(5))


# print(list(filter(lambda x: x % 2 == 1, range(1, 20))))

# def now():
#     print('2015-3-25')

# f = now
# f()
# print(f.__name__)

# import functools
# int2 = functools.partial(int, base = 2)
# print(int2('10000'))

# print(max(2, 3, 4, 5))
# import sys
# PATH = sys.path
# print(PATH)

# class Student(object):
#   def __init__(self, name, score):
#     self.__name = name
#     self.__score = score
  
#   def print_score(self):
#     print('%s: %s'%(self.__name, self.__score))

#   def get_name (self):
#     return self.__name

#   def get_score (self):
#     return self.__score

#   def get_grade (self):
#     if self.__score >= 90:
#       return 'A'
#     elif self.__score >= 60:
#       return 'B'
#     else:
#       return 'C'
  
#   def set_name (self, name):
#     self.__name = name

#   def set_score (self, score):
#     self.__score = score
        

# xu = Student('xuDaoBin', 18)
# lisa = Student('lisa Simpson', 16)
# print(xu.get_grade())
# print(xu.get_name(), xu.get_score())
# xu.set_score(19)
# print(xu.get_score())
# print(xu._Student__name)
# xu.print_score()
# lisa.print_score()

# import sys
# print(sys.path)

# class Student2 (object):
#   def __init__ (self, name, gender):
#     self.__name = name
#     self.__gender = gender
  
#   def get_name (self):
#     return self.__name
#   def get_gender (self):
#     return self.__gender

#   def set_name (self, name):
#     self.__name = name
#   def set_gender (self, gender):
#     self.__gender = gender

# xu2 = Student2('许道斌', '男')

# print(xu2.get_name(), xu2.get_gender())
# xu2.set_name('许道')
# print(xu2.get_name(), xu2.get_gender())

# class Animal (object):
#   def run (self):
#     print('Aminal is running...')

# class Dog (Animal):
#   def run (self):
#     print('Dog is runing...')

# class eat (Animal):
#   def run (self):
#     print('eat is runing..')

# dog = Dog()
# dog.run()

# print(isinstance(dog, Animal))
# print(isinstance(dog, Dog))

# print(type(123), type('s'), type(None))
# print(type(Animal), type(dog))

# print(dir([]))

# class MyDog (object):
#   def __len__ (self):
#     return 100

# dog = MyDog()
# print(len(dog))

# class myObject (object):
#   def __init__ (self):
#     self.x = 9
#   def power (self):
#     return self.x * self.x

# obj = myObject()

# setattr(obj, 'y', 19)
# print(hasattr(obj, 'x'), hasattr(obj, 'y'))

# print(dir(obj))

# print(getattr(obj, 'y'))

# print(getattr(obj, 'z', '没有该属性'))

# class Student (object):
#   name = 'student'

# s = Student()
# s.name = 'Ms'
# print(s.name, Student.name)

# del s.name
# print(s.name)

# class Student (object):
#   __slots__ = ('name', 'age')

# s = Student()
# s.name = 'xu'
# s.age = 18

# # s.score = 19

# class gerStu (Student):
#   pass

# g = gerStu()
# g.score = 19

# class Studen(object):
#   pass

# s = Studen()
# s.name = 'xu'

# print(s.name)
# def set_age (self, age):
#   self.age = age

# from types import MethodType

# s.set_age = MethodType(set_age, s)

# s.set_age(18)

# print(getattr(s, 'age'))

# class obj (object):
#   def __init__ (self, score):
#     self.__score = score
  
#   def get_score (self):
#     return self.__score
#   def set_score (self, value):
#     if not isinstance(value, int):
#       return ValueError('类型错误')
#     if value < 0 or value > 100:
#       return ValueError('不许设置1-100之间')
#     self.__score = value

# s = obj(0)
# s.set_score(60)
# print(s.get_score())

# class Studen (object):
#   def __init__ (self, name):
#     self.name = name
#   def __str__ (self):
#     return 'Studen obj (name: %s)' % self.name

# print(Studen('xu'))

# f = open('C:/Users/Administrator/Desktop/Anih.txt', 'r')
# print(f)
# print(f.read())
# f.close()

# with open('C:/Users/Administrator/Desktop/Anih.txt', 'r') as f:
#   for line in f.readlines():
#     print(line.strip())

# with open('C:/Users/Administrator/Desktop/home.png', 'w') as e:
#   e.write('123')

# with open('C:/Users/Administrator/Desktop/home.png', 'rb') as q:
#   for line in q.readlines():
#     print(line.strip())

# from io import StringIO
# f= StringIO('hello!\nHi!\ngoodbye')

# f.write('hello')
# print(f.getvalue())

# while True:
#   s = f.readline()
#   if s == '':
#     break
#   print(s.strip())

# from io import BytesIO

# f = BytesIO()
# f.write('中文'.encode('utf-8'))

# print(f.getvalue())

# f = BytesIO('xu\ndao\nbin'.encode('utf-8'))

# print(f.read())

# import os
# print(os.name)
# print(os.environ.get('PATH'))
# paths = os.path.abspath('.')
# print(paths)
# os.path.join(paths + '/testdir')

# os.mkdir(paths + '/testdir')
# os.rmdir(paths + '/testdir')

# print(os.path.splitext('C:/Users/Administrator/Desktop/python/hellp.py'))
# print(os.path.split('C:/Users/Administrator/Desktop/python/hellp.py'))


# os.rename('/test.txt', 'test.py')

# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print(os.listdir('.'))
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# d = dict(name = 'bob', age = 20, score = 88)
# print(d)


# import pickle
# d = dict(name = 'bob', age = 20, score = 88)

# with open('dump.txt', 'wb') as f:
#   pickle.dump(d, f)

# with open('dump.txt', 'rb') as f:
#   d = pickle.load(f)
#   print(d)


# import json

# d = dict(name = 'xu', age = 18, score = 99)

# jsonStr = json.dumps(d)

# print(json.loads(jsonStr))

# class Studen(object):
#   def __init__ (self, name, age, score):
#     self.name = name
#     self.age = age
#     self.score = score

# def stud2dict(std):
#   return {
#     'name': std.name,
#     'age': std.age,
#     'score': std.score
#   }
# s = Studen('xu', 19, 100)
# jsonstr = json.dumps(s, default=stud2dict)
  
# print(json.loads(jsonstr))

# obj = dict(name = '小明', age = 18)

# s = json.dumps(obj, ensure_ascii=True)
# print(s)

# from multiprocessing import Process
# import os, time, random
# def run_proc (name):
#   print('Run child process %s (%s)..' %(name, os.getpid()))

# if __name__ == '__main__':
#   print('Parent process %s' %os.getpid())
#   p = Process(target = run_proc, args = ('test',))
#   print('Child process will start')
#   p.start()
#   p.join()
#   print('Child process end')


# from multiprocessing import Pool
# import os, time, random
# def long_time_task(name):
#   print('Run task %s (%s)...' % (name, os.getpid()))
#   start = time.time()
#   time.sleep(random.random() * 3)
#   end = time.time()
#   print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__ == '__main__':
#   print('parent process %s' % os.getpid())
#   p = Pool(8)
#   for i in range(8):
#     p.apply_async(long_time_task, args=(i,))
#   print('Waiting for all subprocesses done...')
#   p.close()
#   p.join()
#   print('All subprocesses done.')

# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])

# print('exit code', r)


# from multiprocessing import Process, Queue
# import os, time, random

# def write(q):
#   print('process to write: %s' % os.getpid())
#   for value in ['a', 'b', 'c']:
#     print('put %s to queue..' %value)
#     q.put(value)
#     time.sleep(random.random())

# def read (q):
#   print('process to read: %s' % os.getpid())
#   while True:
#     value = q.get(True)
#     print('get %s from queue.' % value)

# if __name__ == '__main__':
#   q = Queue()
#   pw = Process(target = write, args = (q,))
#   pr = Process(target = read, args = (q,))
#   pw.start()
#   pr.start()
#   pw.join()
#   pr.terminate()


# import time, threading

# import hashlib

# md5 = hashlib.md5()
# md5.update('how to use mdt in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(('www.sina.com.cn', 80))

# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# s.bind('127.0.0.1', 9999)

# s.listen(5)
# print('waiting for connection..')

# def tcplink (sock, addr):
#   print('Accept new connection from %s:%s' % addr)
#   sock.send(b'welcome!')
#   while True:
#     data = sock.recv(1024)
#     time.sleep(1)
#     if not data or data.decode('utf-8') == 'exit':
#       break
#     sock.close()
#     sock.send(('hello, %s' % data.decode('utf-8').encode('utf-8')))

# while True:
#   sock, addr = s.accept()
#   t = threading.Thread(target = tcplink, args=(sock, addr))
#   t.start()

# from email.mime.text import MIMEText

# msg = MIMEText('hello, send by python', 'plain', 'utf-8')
