"""Игра угадай число!
Компьютер сам загадывает и угадывает число!
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    number_min = 1 # нижняя граница интервала поиска
    number_max = 101 # верхняя граница интервала поиска
    
    
    while True:
        count += 1
        predict_number = np.random.randint(number_min, number_max) # предполагаемое число в заданном интервале
        if predict_number < number: # если предложенное число меньше загаданного
            number_min = predict_number # увеличиваем нижнюю границу интервала
        elif predict_number > number: # если предложенное число больше загаданного 
            number_max = predict_number # уменьшаем верхнюю границу интервала
        else:
            break # выход из цикла если угадано
    
    return count

def score_game(random_predict) -> int:
    """За какое в среднем количество попыток угадывает за 1000 подходов

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == '__main__':
    # запуск функции
    score_game(random_predict)