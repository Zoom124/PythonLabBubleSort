'''
print("Введите количество символов = ", end = '')
n = int(input());
array = list(range(n))
print("Введите символы:")
i = 0
while (i < n):
  print('array['+ str(i) +'] = ', end='')
  array[i] = input()
  i += 1;

j = 0
while j < n-1:
  i = 0
  while (i < n-1):
    if array[i] > array[i+1]:
      temp = array[i+1]
      array[i+1] = array[i]
      array[i] = temp
    i+=1
  j+=1
print(array)
'''
def main(*args):
  l = list(args)
  i = 0
  for c in l:
    #print('l[{}] = {}'.format(i,type(c)))
    if type(c) == str:
      if (not c.isdigit() and not c.isalpha()) or c.isalpha():
        return "Ошибка! Неверный формат ввода {}".format(c)
      elif c.isdigit():
        l[i] = int(c)
      else:
        l[i] = int(ord(c))
    i+=1
  return sorted(l)

if __name__ == '__main__':
  assert main(23,0,2,1,44,4) == [0,1,2,4,23,44],"Сортировка прошла не удачно"
  assert main(1,0,2,3,4,5) == [0,1,2,3,4,5],"Сортировка прошла не удачно"
  assert main(10,0,20,30,50,40) == [0,10,20,30,40,50],"Сортировка прошла не удачно"

print(main(23,'dasga',0.5,True,False))