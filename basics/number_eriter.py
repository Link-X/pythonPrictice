# import json

# number = [1, 2, 3, 4, 5]

# filename = 'number.json'
# with open(filename, 'w') as f:
#   json.dump(number, f)

# with open(filename, 'r') as f:
#   numbers = json.load(f)
#   print(numbers)

import json

def getUserName ():
  fileNmae = 'number.json'
  try:
      with open(fileNmae) as f:
        userName = json.load(f)
  except:
      return None
  else:
      return userName

def setUser ():
  fileNmae = 'number.json'
  userNmae = input('请输入你的名字:')
  with open(fileNmae, 'w') as f:
    json.dump(userNmae, f)
  return userNmae


def greetUser ():
  userName = getUserName()
  if userName:
    print('hello%s'%userName)
  else:
    userName = setUser()
    print('欢迎加入:%s'%userName)

greetUser()