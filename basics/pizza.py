def mak_pizze (size, *toppings):
  print('\n你的披萨要多大%s'%str(size))

  for item in toppings:
    print('-%s'%item)

def mak_pizze2 (size, *topings):
  print('\n你的吃的要多大呢%s'%size)
  for item in topings:
    print('-%s'% item)