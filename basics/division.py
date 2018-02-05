# try:
#   print(5/0)
# except ZeroDivisionError:
#   print('you can\'t divide by zero')

# while True:
#   name1 = input('被除数：')
#   if name1 == 'exit':
#     break
#   name2 = input('输入除数：')
#   try:
#     answer = int(name1) / int(name2)
#   except ZeroDivisionError:
#     print('错误')
#   else:
#       print(answer)

# try:
#   with open('ttt.txt') as q:
#     const = q.read()
# except FileNotFoundError:
#   print('文件找不到')

def getTxtWordNumber (fileName):
  try:
    with open(fileName) as f:
      f_details = f.read()
  except FileNotFoundError:
    print('找不到%s'%fileName)
  else:
    word = f_details.split()
    number = len(word)
    print('这本%s一共有单词%s'%(fileName, number))

txts = ['./txt/alice', './txt/aaa.txt' './txt/alice2', 'aa.txt', './txt/alicd3']

for item in txts:
  getTxtWordNumber(item)