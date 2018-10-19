def unique_funk(lst):
    if type(lst) == list:
        flag = 0
        resultLs = []
        resultLs.append(lst[0])
        for l in lst:
            i = 0
            while i < len(resultLs):
                if resultLs[i] == l:
                    flag = 1
                i += 1;
            if (flag == 0):
                resultLs.append(l)
            flag = 0
        return resultLs
    else:
        return "Ошибка! Неверный формат ввода {}".format(type(lst))


print(unique_funk([4,4,4,1,4,2,3,5,3,3]))

if __name__ == '__main__':
    assert unique_funk([1,2,3,3,3]) == [1,2,3], "Функция возвращает не верные значения"
    assert unique_funk([1,1,1,2,3,3,3]) == [1,2,3], "Функция возвращает не верные значения"
    assert unique_funk([1,2,2,2,2,3,3,3]) == [1,2,3], "Функция возвращает не верные значения"