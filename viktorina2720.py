def quiz():
    ans = ['30', '1', '46', 'Ключевская сопка', '2024']
    ques = ['сколько градусов в arcsin 1/2? ', 'какое место занимает Китай в мире по численности населения? ', 'сколько хромосом у человека? ', 'какое название имеет камчатский вулкан(первое слово обязательно с большой буквы)? ', 'в каком году следующие выборы президента России? ']
    counter = 0
    for i in range (5):
        usersAns = input(f'{i + 1}-{ques[i]}')
        if usersAns == ans[i]:
            print("верно")
            counter += 1
        else:
            print("неверно")
    return f'правильных ответов - {counter}'
def solve():
    x = quiz()
    return int(input(f'{x} есть желание сыграть еще? 1 - да, 0 - да(Нет)'))
def foo():
    arg = 1
    while arg == 1:
        arg = solve()
    print('ок, до встречи!')
if __name__ == '__main__':
    foo()