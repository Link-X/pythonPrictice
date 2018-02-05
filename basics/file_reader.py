# with open('pi_dig.txt') as f:
#   lines = f.readlines()
#   pi_string = ''
#   for line in lines:
#     pi_string += line.strip()
#   print(pi_string)
#   print(len(pi_string))

# with open('text_file/Anih.txt') as q:
#   lines = q.readlines()
#   for line in lines:
#     print(line.rstrip())

# with open('text_file/pai.txt', 'r') as e:
#   lines = e.readlines()
#   pi_string = ''
#   for line in lines:
#     pi_string += line
  
#   birthad = input('输入你的生日:')
#   if birthad in pi_string:
#     print('你的生日在圆周率里呦')
#   else:
#       print('你的生日不在圆周率里')

# mes = 'i really like dogs'
# print(mes.replace('dog', 'car'))
# print(mes)

filename = 'test.txt'
# with open(filename, 'w') as q:
#   q.write('i lover programming.\n')
#   q.write('i lover creating new games.\n')

# with open(filename, 'a') as q:
#   q.write('i like javaScript\n')
#   q.write('i link python\n')

with open(filename, 'a') as q:
  while True:
    name = input(' 输入你喜欢的语言吧:')
    q.write('\n%s'%name)
    if name == 'over':
      print('感谢调查')
      break