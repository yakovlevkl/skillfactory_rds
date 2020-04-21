#!/bin/python3

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в
        зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
    '''
    count = 1
    mark = 0
    predict = np.random.randint(1,101)
    print (count, mark, number, predict)
    while number != predict:
        
        count+=1
        if number > predict: 
            if mark == 2 :
                predict += 1
            else:
                predict += 10
                mark = 1
        elif number < predict:
            if mark == 1 :
                predict -= 1
            else:
                predict -= 10
                mark = 2
        print (count, mark, number, predict)
    return(count) # выход из цикла, если угадали  

        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v3)
