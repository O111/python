"""Игра угадай число
Компьютер сам загадывает число от 1 до 100 и сам угадывает число по алгоритму
"""

import numpy as np

def predict(predict_number:int) -> int:
    """Угадываем число от 1 до 100, учитывая больше оно или меньше загаданного и устанавливая новую отгадку в середину диапазона

    Args:
        predict_number (int): Загаданное число
        
    Returns:
        int: Число попыток
    """
    
    max_number = 100   # первоначальная верхняя граница диапазона угадывания
    min_number = 1     # первоначальная нижняя граница диапазона угадывания
    
    count = 0
    number = max_number   # первоначальная отгадка, которая не отлавливается нашим алгоритмом; с нее начинаем 
    
    while True:
        
        count += 1        
        
        if number == predict_number:
            break   # выход из цикла, если угадали
        elif number > predict_number:
            max_number = number
            number = min_number + (max_number - min_number) // 2
        else:
            min_number = number
            number = min_number + (max_number - min_number) // 2
          
    return(count)


def score_game() -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем seed для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    
    return(score)

# RUN
score_game()
