a = "zv" # задаём названия для матриц
z = ['***', #
     ' * ', # записываем значения в матрицы
     '***'] #
v = ['* *', #
     '* *', # записываем значения в матрицы
     ' * '] #
mat = [z,v] # создаем список из матриц
t = list('zv') # создаем список из матриц
ch = [t.index(l) for l in a] # запускаем цикл по перебору обозначений матриц
for i in range(len(mat[0])): # запускаем цикл по перебору содержания(строк) матриц
    for y in ch: # перебираем значения матрицы
        print(mat[y][i], end = ' ') # печатаем матрицы
#    for y in range(len(ch)): - альтернативный вариант
#        print(mat[ch[y]][i], end = ' ') - альтернативный вариант
    print() # печатаем значения матриц в правильном(вертикальном) порядке
