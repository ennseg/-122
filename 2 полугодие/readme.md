### Подготовка к ЕГЭ
# 2 задача.
## 1. Сгенерировать все возможные сочетания переменных. много вложенных циклов
## 2. Проверить логическую функцию на условие, проверить её на лож.
# 3 задача.
## 1. Фильтруй все столбци таблици.
# 4 задача.
## 1. Построить бинарное дерево с известными данными.
## 2. Определить количесвтво нужных символов для кодировк.
## 3. Начать кодировку с минимального набора с минимального кода.
## 4. Берем минимальный код и смотрим оставшихся вариантов хватает, чтобы закрыть все симолы, ели их не хваитет для кодирования символа, то увеличиваем длину кода.
# 5 задача.
## 1. Перебор чиселс с нуля до нужного из условия
## 2. Превод в двоичную систему (bin(i)[:] / f'{N:b}')
## 3. Проверка строки по условию, осуществляем допись и замену
## 4. Перевод в десятичную систему, проверка по условию и выходиз цикла
    for N in range(516):
        b = f'{N:b}' # bin(N)
        if N%2 == 0:
            b+='10'
        else:
            b = '1'+b+'10'
        
        if int(b,2) >516:
            print(b)
            break;
# 6 задача.
## 1. вспомнить команды черепашки
## 2. реалтзовать алгаритм задачи
## 3. посчитать количество точек с учетом масштаба
    from turtle import *
    left(90)
    for i in range(7):
        forward(300)
        right(120)
    pu()
    for x in range(1,9):
        for y in range(1,10):
            goto(x*30,y*30)
            dot(5)
    done()
# 8 задача.
## 1. Создаем все возможные варианты искомой величины (через циклы for)
## 2. Проверяем есть ли в последовательности выполнение условия
## 3. Вывод счетчика искомых значений
    from itertools import product
    nums=product('01234567',repeat=5)
    k=0
    n='16 36 56 76 61 63 65 67'
    nn=n.split()
    for n in nums:
        numb=''.join(n)
        sp=[]
        if numb.count('6')==1 and numb[0]!='0':
            for x in nn:
                if x in numb:
                    sp.append(x)
            if not sp: 
                k+=1
    print(k)
# 10 задача.
## 1. Итак, для начала нажимаем ctrl+f, в word появляется расширенный поиск, где нужно указать нужные параметры поискаи далее нам покажет, сколько раз это     слово встречается в данном файле.
# 12 задача.
## 1. По возможности преобразовать последовательнось в уравнение
## 2. Организовать подбор параметров
## 3. Обратить внимание на третий параметр replace
# 13 задача.
## 1. Накопительно нумеруем вершины графа, начиная с 1.
## 2. Суммируем все значаения или умножаем.
## 3. Выводим счетчик занчений.
![image](https://user-images.githubusercontent.com/114893510/208361587-229888fa-e09d-4d3b-b7c1-3e4a388dd44e.png)
# 14 задача.
```python

a='0123456789abcde'
for x in a:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(f//14)
        break

```
# 15 задача.
```python

for a in range(1,1000):
    if all(((x%2==0) <= (x%3!=0)) or (x+a>=100) for x in range(1,100)):
        print(a)
        break

```
# 17 задача.
```python
def f17():
    with open('17.txt') as f:
        a=[int(x) for x in f]
    mn=min(x for x in a if x % 17==0)
    maxi = -10
    count = 0
    for i in range(len(a)-1):
        if a[i]%mn ==0 or a[i+1]%mn == 0:
            sum = a[i+1]+a[i]
            count +=1
            if maxi < sum:
                maxi = sum
    print(maxi,count)
f17()
```
```python
with open('17.txt')as f:
    a=[int(x)for x in f]
    g=[x for x in a if x%10==3]
    g=max(g)
    cs=[]
    for x,y in zip(a,a[1:]):
        if (((abs(x)%10==3) and (abs(y)%10!=3)) or ((abs(y)%10==3) and (abs(x)%10!=3))) and (x**2+y**2>=g**2):
            cs.append(x**2+y**2)
    print(len(cs),max(cs))
```
# 19 задача.


## 1. Нужно определить точку вход, условие ваыугрыша, сколько очков нужно наблать, чтобы завершить игру.
## 2. Рассписать двоичное дерево на 4 хода.
## 3. Ответить на вопрос задачи, присвоив какой ход, кто совершает.


# 23 задача.

## 1. С помощью функции продукт сформировать объект со всеми комбинациями искомой строки.
## 2. Перебор в совокупности программ.
## 3. Приводим стартовое положение в первоначальное состояние.
## 4. Используем команду для пропуска итерации не подходящих программ.
## 5. Заходим в саму программу.
## 6. Заходим в программу и анализируем команды.
## 7. Проверка на 17.
## 8. Если счетчик натыкается на значение которое нельзя допускать, то мы выходим из цикла и больше не работаем в этой программе, то есть переходим к следующей программе.
## 9. Проверяем счетчик на нужное значение.
## 10. Вывели полученное значение.
```python
from itertools import product
def f23(x,y,z):
    count=0
    for i in range(1,z):
        nums=product('12',repeat=i)
        for numb in nums:
            #numb=''.join(n)
            a=x
            if x==10 and numb.count('2')>1:continue
            for ii in numb:
                if a==17: break 
                if ii=='1':a+=1
                elif ii=='2' :a*=2

            if a==y: count+=1
    return count
                
print(f23(1,10,10)*f23(10,35,25))

```
```python
def f(x,y):
    if x >y or x == 17: return 0
    elif x ==y: return 1
    return f(x+1,y)+f(x*2,y)
    
print(f(1,10)*f(10,35))
```

```mermaid
stateDiagram-v2
    >=129 --> 128: +1
    >=129 --> 65: *2
    65 --> 64: +1
    64 --> 63: +1
    64 --> 32: *2
    63 --> 62: +1
    32 --> 16: *2
    32 --> 31: +1
    128 --> 64: *2
```
# 27A задача.

## 1. Из-за того, что мало пунктов, мы можем использовать перебор.
## 2. Сначала мы загржаем данные из файла в список.
## 3. Избавляемся от первого элемента.
## 4. Затем мы создаем переменную с некоторыми параметрами нашего списка, напрмиер длина.
## 5. Сдваиваем список.
## 6. Используя срезы мы меняем список для работы. меняем список с помощью них.
## 7. Меняем таким образом, чтобы киллометр, для которого мы считаем стоимость доставки, стоял на первом месте.
## 8. Важный момент, когда мы создаем новый список с использыванием среза мы обнуляем стоимость. Чтобы она не накапливалась.
## 9. Применяем саму формулу, считаем стоимость доставки.
## 10. Cоздаем переменную для пересчета индекса элементов после середины списка. от длины списка отнимаем индекс элемента.
## 11. Считаем стоимость накоплением.
## 12. Найденную стоимость на каждом киллометре мы добавляем в новый список.
## 13. Выводим индекс минимального элемента списка со стоимостью + 1.

# 27Б задача.

## 1. Используем метод итераций вместо перебора (приближения). С каждым шагом мы приближаемся к точному определенному решению.
## 2. Вся программа находится в бесконечном цикле, выход из которого это точное решение.
## 3. Точное решение, это два раза повторяющийся ответ при шаге 1.
## 4. Если в 27-А проверя большой список фиксированно, большой цикл перебора организован с использованием трех переменных , старта финиша и шага.
## 5. Шаг настраивается таким образом, чтобы было двадцать равнораспределенных замеров по всей дороге.
## 6. После каждого прохода цикла переменные старта, конца и шага пересчитываются.
## 7. Определяем минимальную стоимость среди двадцати значений и киллометр, которому она принадлежит, новое значение старта и финиша это рамки диапазона посика.
## 8. Новое значение границ диапазона поисков это киллометр - шаг и киллометр + шаг.
## 9. После перерасчета старта и финиша пересчитывается шаг.
## 10. Целая часть от деления его на десять.
## 11. Когда шаг становится 0 присваиваем ему 1.
