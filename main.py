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
  return sorted(args)

print(main(23,0,3,1,44,4))