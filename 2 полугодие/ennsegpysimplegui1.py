import PySimpleGUI as sg

sg.theme('Black')
s=['2','5','9','12','14','15','16','17','23','24','25','26','27']
a=[
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(y<=x) or (z<=w) or not(z))==False:
                    print(x,y,z,w)


''',
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


''',
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

''',
'''
spisok=[]
for num in range(2,1000):
    if all(num%delit!=0 for delit in range(2,num)):
        spisok.append(num)
        
for y in range (100):
    if y*4+117 in spisok:
        print(y)
        break


''',
'''
alph='0123456789abcde'
for x in alph:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(x,f//14)
        break


''',
'''
for a in range(1,100):
    if all(((x%2==0) <= (x%3!=0)) or (x+a>=100) for x in range(1,1000)):
        print(a)
        break


''',
'''
#sys.setrecursionlimit(2500)
itog1=itog2=1
for x1 in range(1,2024):
    itog1=itog1*x1
for x2 in range(1,2021):
    itog2=itog2*x2
print(itog1/itog2)


''',
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

            
''',
'''
def f(x,y):
    if x>y or x==17:
        return 0
    elif x==y:
        return 1
    return f(x+1,y) +f(x*2,y)
print(f(1,10)*f(10,35))

    
''',
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


''',
'''
for i in range(2023,10**10,2023):
    num=str(i)
    if (num[0]=='1') and (num[2:6]=='2139') and (num[-1]=='4'):
        print(i,i//2023)


''',
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


''',
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
layout = [[sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(90,50), key='outputt')],
          [sg.Button('Старт', font=('Impact', 12), button_color=('black', '#FFFFFF'), key='process'),
           sg.Button('Выход', font=('Impact', 12), button_color=('black', '#FFFFFF'), key='button')]]

# Create the window
window = sg.Window('Сборник ЕГЭ', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        choice=a[s.index(values['Combo'])]
        window['outputt'].update(choice)
    if event == 'button':
        break

# Close the window
window.close()