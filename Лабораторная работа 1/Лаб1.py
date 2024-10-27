import math

def get_coef(prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        prompt (str): Приглашение для ввода коэффициента

    Returns:
        float: Коэффициент биквадратного уравнения
    '''

    print(prompt)
    coef_str = input()
    while (True):
        # Читаем коэффициент из командной строки до тех пор пока не будет корректный ввод
        try:
            # Пробуем перевести строку в действительное число
            coef = float(coef_str)
            break
        except:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
    return coef

def get_roots(a,b,c):
    '''
    Вычисление корней биквадратного уравнения

    Args:
        a (float): коэффициент A
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''

    result = []
    D = b*b - 4*a*c

    if D == 0.0:
        root = -b / (2.0*a)
        if root == 0.0:
            result.append(root)
        elif root > 0.0:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))

    elif D > 0.0:
        sqrt_D = math.sqrt(D)
        root1 = (-b + sqrt_D) / (2.0*a)
        root2 = (-b - sqrt_D) / (2.0*a)
        if (root1 == 0.0 or root2 == 0.0):
            result.append(0.0)
        if root1 > 0.0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))
        if root2 > 0.0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))

    return result

def main():
    '''
    Основная функция
    '''
    a = get_coef('Введите коэффициент A:')
    b = get_coef('Введите коэффициент B:')
    c = get_coef('Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Два корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Два корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))



if __name__ == "__main__":
    main()