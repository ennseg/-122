import PySimpleGUI as sg
import webbrowser
import os

sg.theme('Black')
urls = {
    'GitHub': 'https://github.com/ennseg',
    'LycTPU': 'https://lyctpu.github.io/',
    'EGE_demo_2023': 'https://github.com/lyctpu/ege/blob/main/2023demo/%D0%98%D0%9D%D0%A4-11%20%D0%95%D0%93%D0%AD%202023_%D0%94%D0%95%D0%9C%D0%9E.pdf',
    'EGE_demo_2023_otvet': 'https://deepnote.com/@lyctpu/EGE23-e70e0880-8033-40a8-abb8-4157d3d12909',
}
s=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27']
a=[
#1
'''
1. Определить точки, из которых выходят 3 линии.
2. Поподставять эти точки и , определить длины линий между ними и увидеть точки соединённые двумя дорогами.
3. Поподставять и потом посчитать ответ.


''',#2
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(y<=x) or (z<=w) or not(z))==False:
                    print(x,y,z,w)


''',#3
'''
Фильтруй все столбци таблицы


''',#4
'''
1. Построить бинарное дерево с известными данными.
2. Определить количесвтво нужных символов для кодировк.
3. Начать кодировку с минимального набора с минимального кода.
4. Берем минимальный код и смотрим оставшихся вариантов хватает, чтобы закрыть все симолы, ели их не хваитет для кодирования символа, то увеличиваем длину кода.


''',#5
'''
for i in range(1,100):
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo='10'+num[2:]+'0'

    if num.count('1')%2!=0:
        chislo='11'+num[2:]+'1'
    if int(chislo,2)>40:
        print (i, int(chislo,2))
        break


''',#6
'''
from turtle import *
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(2)
done()

''',#7
'''
Испольуем формулу V=M*i*t для звука
t - время
i - раширение
m - частота дискретезации
v - объем файла в битах


''',#8
'''
from itertools import product
k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
nums=product('01234567',repeat=5)
for n in nums:
    numb=''.join(n)
    if numb.count('6')==1 and numb[0]!='0':
        if all(not(x in numb) for x in nn):
            k+=1
print(k)


''',#9
'''
# загрузка текста из txt
text=t.split(";")
#result = [int(item) for item in text]
result = list(map(int, text))
x=0
y=x+6
counter=double_num=0

while True:
   n=0
   res6=result[x:y]
   for element in res6:
      if res6.count(element)>2:
         for yy in range(res6.count(element)): res6.remove(element) 
         # удаление значений больше 2 штук
      if res6.count(element)==2:
         n+=2   
         double_num=element 
         res6.remove(element)
         res6.remove(element)

   if n==2 and len(res6)==4:  
      if (sum(res6)/len(res6))<=(double_num*2): counter+=1

   print(counter)
   if y>=len(result):break         
   x=x+6
   y=x+6


''',#10
'''
Итак, для начала нажимаем ctrl+f, в word появляется расширенный поиск, где нужно указать нужные параметры поискаи далее нам покажет, сколько раз это слово встречается в данном файле.


''',#11
'''
Не требует особого решения, в силу саоей простоты


''',#12
'''
spisok=[]
for num in range(2,1000):
    if all(num%delit!=0 for delit in range(2,num)):
        spisok.append(num)
        
for y in range (100):
    if y*4+117 in spisok:
        print(y)
        break


''',#13
'''
1. Накопительно нумеруем вершины графа, начиная с 1.
2. Суммируем все значаения или умножаем.
3. Выводим счетчик занчений.


''',#14
'''
alph='0123456789abcde'
for x in alph:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(x,f//14)
        break


''',#15
'''
for a in range(1,100):
    if all(((x%2==0) <= (x%3!=0)) or (x+a>=100) for x in range(1,1000)):
        print(a)
        break


''',#16
'''
#sys.setrecursionlimit(2500)
itog1=itog2=1
for x1 in range(1,2024):
    itog1=itog1*x1
for x2 in range(1,2021):
    itog2=itog2*x2
print(itog1/itog2)


''',#17
'''
with open('17.txt') as f:
    nums=[int(x) for x in f]
    maxi=[]
    s=[]
   
    for i in range(len(nums)):
      if nums[i]%10==3:
         maxi.append(nums[i])
    maximum=0
    for i in range(len(nums)-1):
        a=abs(nums[i])%10
        b=abs(nums[i+1])%10
        if ((a==3) and (b!=3)) or ((a!=3) and (b==3)):
        if (nums[i]**2+nums[i+1]**2) >= max(maxi)**2: 
            s.append(nums[i]+nums[i+1])
            if nums[i]**2+nums[i+1]**2>maximum:
                maximum=nums[i]**2+nums[i+1]**2
print(len(s), maximum)


''',#18
'''  
1. Левый верхний угол берём значение из 1 таблицы.
2. В ячейке справа складываем значение этой ячейки из таблицы 1 и значения 1 ячейки, аналогично для ячейки снизу.
3. Далее используем макс()+зн этой ячейки из таблицы 1 (макс() для ячеек сверху с снизу относительно даной).
4. За барьерами используем формулы сложения верхнего и данного значения , аналогично для горизонтального.


''',#19
'''  
1. Нарисовать двоичное дерево, начиная с победных ходов.
2. Расписываем дерево на 4 и более хода.
3. Считаем по усл задачи где чей ход extra (обычно ответ это число, которое можно получить только 1 способом).        


''',#20
'''
1. Нарисовать двоичное дерево, начиная с победных ходов.
2. Расписываем дерево на 4 и более хода.
3. Считаем по усл задачи где чей ход extra (обычно ответ это число, которое можно получить только 1 способом).        


''',#21
'''
1. Нарисовать двоичное дерево, начиная с победных ходов.
2. Расписываем дерево на 4 и более хода.
3. Считаем по усл задачи где чей ход extra (обычно ответ это число, которое можно получить только 1 способом).        


''',#22
'''
1. Каждому процессу присваиваем цвет.
2. Закрашиваем клеточки в таблице относительно конца процесса.


''',#23
'''
def f(x,y):
    if x>y or x==17:
        return 0
    elif x==y:
        return 1
    return f(x+1,y) +f(x*2,y)
print(f(1,10)*f(10,35))

    
''',#24
'''
with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    k=kmax=0
    for i in s:
        if i=='*'
            k+=1
            kmax=max(k,kmax)
        else:k=0
print(kmax)


''',#25
'''
for i in range(2023,10**10,2023):
    num=str(i)
    if (num[0]=='1') and (num[2:6]=='2139') and (num[-1]=='4'):
        print(i,i//2023)


''',#26
'''
with open('26.txt') as f:
    s=[int(x) for x in f]
    s=sorted(s[1:],reverse=True)
    k,mini=1,s[0]
    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
    print(k,mini)


''',#27
'''
with open('27-B.txt') as f:
        n=int(f.readline())
        m=([int(x) for x in f][:n]*3)[n//2:-n//2]
    print(0,m)
    
    pr=[0]*(len(m)+1)
    for i in range(1, len(pr)):
        pr[i]=pr[i-1]+m[i-1]
    
    po=[0]*(len(m)+1)
    for i in range(len(po)-2, -1,-1):
        po[i]=po[i+1]+m[i]
    print(pr)
    print(po)
    st=[0]*n
    fn=[0]*n
    st[0]=sum(pr[:n//2+1])
    fn[0]=sum(po[-n//2:])
    s1=s2=0
    
    for i in range(1,n):
        s1=m[i-1]*(n//2)+pr[i]
        s2=m[-i]*(n//2-1)+po[-i-1]
        st[i]=st[i-1]+pr[n//2+i]-s1
        fn[-i]=fn[(-i+1)%n]+po[-(n//2+i)]-s2
    c=0
    m=float('inf')
    for i,t in enumerate(zip(st,fn),start=1):
        if sum(t)<m:
            c,m=i,sum(t)
    print(c,a)
            
'''

]
# Define the layout
layout = [[sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'), sg.Output(s=(90,25), key='outputt')], [sg.Button('Старт', font=('Impact', 12), button_color=('black', '#FFFFFF'), key='process'),
	   sg.Button('Полезные ссылки', font=('Impact', 12), button_color=('black', '#FFFFFF'), key='button'),
	   sg.Button('Выход', font=('Impact', 12), button_color=('black', '#FFFFFF'), key='exit')],
	  [sg.Output(s=(70, 20), key='outputt'),sg.Image('1.png',expand_x=True, expand_y=True, key='img')]
	 ]

# Create the window
window = sg.Window('Сборник ЕГЭ', layout)

# Event loop
while True:
    event, values = window.read()

    if event == "exit":
        break

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        
        choice=a[s.index(values['Combo'])]
        im=str(s.index(values['Combo'])+1)+'.png'
        window['outputt'].update(choice)
        window['img'].update(im)
        
    if event == 'button':
        urls = {
    'GitHub': 'https://github.com/ennseg',
    'LycTPU': 'https://lyctpu.github.io/',
    'EGE_demo_2023': 'https://github.com/lyctpu/ege/blob/main/2023demo/%D0%98%D0%9D%D0%A4-11%20%D0%95%D0%93%D0%AD%202023_%D0%94%D0%95%D0%9C%D0%9E.pdf',
    'EGE_demo_2023_otvet': 'https://deepnote.com/@lyctpu/EGE23-e70e0880-8033-40a8-abb8-4157d3d12909',
	}
        items = sorted(urls.keys())

        sg.theme("Black")
        font = ('Impact', 12)

        layout2 = [[sg.Text(txt, tooltip=urls[txt], enable_events=True, font=font,
                           key=f'URL {urls[txt]}')] for txt in items]

        ulr_window = sg.Window('Hyperlink', layout2, size=(250, 150), finalize=True)

        while True:
            event, values = ulr_window.read()
            if event == sg.WINDOW_CLOSED:
                ulr_window.close()
                break
            elif event.startswith("URL "):
                url = event.split(' ')[1]
                webbrowser.open(url)

# Close the window
window.close()
