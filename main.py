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
  for c in args:
    if type(c) == str:
      return "Неверный формат, ожидался Int, введен Str"
  return sorted(args)

if __name__ == '__main__':
  assert main(23,0,2,1,44,4) == [0,1,2,4,23,44],"Сортировка прошла не удачно"
  assert main(1,0,2,3,4,5) == [0,1,2,3,4,5],"Сортировка прошла не удачно"
  assert main(10,0,20,30,50,40) == [0,10,20,30,40,50],"Сортировка прошла не удачно"
print(main(23,0,2,1,44,4))