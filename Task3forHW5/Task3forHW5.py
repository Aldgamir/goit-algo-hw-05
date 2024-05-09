import timeit

def BoyerMoore(text, pattern):
    
    # Створення таблиці правосусідів
    bad_chars = {}
    for i in range(len(pattern)):
        bad_chars[pattern[i]] = len(pattern) - i - 1

    # Пошук підрядка
    result = []
    i = 0
    while i < len(text):
        if pattern[0] == text[i]:
            j = 1
            while j < len(pattern) and pattern[j] == text[i + j]:
                j += 1

            if j == len(pattern):
                result.append(i)
                i += len(pattern) - bad_chars.get(text[i], len(pattern))
            else:
                i += bad_chars.get(text[i], len(pattern))
        else:
            i += bad_chars.get(text[i], len(pattern))

    return result

def KMP(text, pattern):
    
    # Створення префікс-функції
    prefix_function = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            prefix_function[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                prefix_function[i] = 0
                i += 1
            else:
                j = prefix_function[j - 1]

    # Пошук підрядка
    result = []
    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                result.append(i - j)
                j = prefix_function[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = prefix_function[j - 1]

    return result

def RabinKarp(text, pattern):
   
    # Використання хешування для порівняння підрядків
    prime = 101  # Просте число
    hash_pattern = 0
    hash_text = 0
    h = 1  # Потужність хешування

    for i in range(len(pattern)):
        hash_pattern += ord(pattern[i]) * h
        hash_text += ord(text[i]) * h
        h = (h * prime) % prime

    result = []
    i = len(pattern)

    while i < len(text):
        if hash_pattern == hash_text:
            if pattern == text[i - len(pattern):i]:
                result.append(i - len(pattern))

        hash_text = (hash_text - ord(text[i - len(pattern)]) * prime) % prime
        hash_text = (hash_text * prime + ord(text[i])) % prime
        i += 1

    return result

# Завантаження текстів
with open('/Users/vladimirvinogradov/Desktop/GoIt/Module_3._Algorithms /HW5/Task3forHW5/Стаття 1.txt', 'r', encoding='latin-1') as f:
    text1 = f.read()

with open('/Users/vladimirvinogradov/Desktop/GoIt/Module_3._Algorithms /HW5/Task3forHW5/Стаття 2.txt', 'r', encoding='latin-1') as f:
    text2 = f.read()

# Вибір підрядків
pattern1_real = 'Структури даних'  # Існуючий підрядок
pattern1_fake = 'І час настав'  # Неіснуючий підрядок
pattern2_real = 'Ключові слова'  # Існуючий підрядок
pattern2_fake = 'І час настав'  # Неіснуючий підрядок

# Вимірювання часу виконання
print('**Стаття 1**')
print('Реальний підрядок:')
print('Boyer-Moore:', timeit.timeit(lambda: BoyerMoore(text1, pattern1_real), number=1000))
print('KMP:', timeit.timeit(lambda: KMP(text1, pattern1_real), number=1000))
print('Rabin-Karp:', timeit.timeit(lambda: RabinKarp(text1, pattern1_real), number=1000))

print('Неіснуючий підрядок:')
print('Boyer-Moore:', timeit.timeit(lambda: BoyerMoore(text1, pattern1_fake), number=1000))
print('KMP:', timeit.timeit(lambda: KMP(text1, pattern1_fake), number=1000))
print('Rabin-Karp:', timeit.timeit(lambda: RabinKarp(text1, pattern1_fake), number=1000))

print('**Стаття 2**')
print('Реальний підрядок:')
print('Boyer-Moore:', timeit.timeit(lambda: BoyerMoore(text2, pattern2_real), number=1000))
print('KMP:', timeit.timeit(lambda: KMP(text2, pattern2_real), number=1000))
print('Rabin-Karp:', timeit.timeit(lambda: RabinKarp(text2, pattern2_real), number=1000))

print('Неіснуючий підрядок:')
print('Boyer-Moore:', timeit.timeit(lambda: BoyerMoore(text2, pattern2_fake), number=1000))
print('KMP:', timeit.timeit(lambda: KMP(text2, pattern2_fake), number=1000))
print('Rabin-Karp:', timeit.timeit(lambda: RabinKarp(text2, pattern2_fake), number=1000))

print("Порівняння: ")

if timeit.timeit(lambda: BoyerMoore(text1, pattern1_real), number=1000) < timeit.timeit(lambda: KMP(text1, pattern1_real), number=1000):
    print('Boyer-Moore швидший в пошуку реального підрядка у першій статті')
elif timeit.timeit(lambda: RabinKarp(text1, pattern1_real), number=1000) < timeit.timeit(lambda: KMP(text1, pattern1_fake), number=1000):
    print('RabinKarp швидший в пошуку реального підрядка у першій статті')
else:
    print('KMP швидший в пошуку реального підрядка у першій статті')


if timeit.timeit(lambda: BoyerMoore(text1, pattern1_fake), number=1000) < timeit.timeit(lambda: KMP(text1, pattern1_fake), number=1000):
    print('Boyer-Moore швидший в пошуку неіснуючого підрядка у першій статті')
elif timeit.timeit(lambda: RabinKarp(text1, pattern1_fake), number=1000) < timeit.timeit(lambda: KMP(text1, pattern1_fake), number=1000):
    print('Rabin-Karp швидший в пошуку неіснуючого підрядка у першій статті')
else:
    print('KMP швидший в пошуку неіснуючого підрядка у першій статті')


if timeit.timeit(lambda: BoyerMoore(text2, pattern2_real), number=1000) < timeit.timeit(lambda: RabinKarp(text2, pattern2_real), number=1000):
    print ('Boyer-Moore швидший в пошуку реального підрядка у другій статті')
elif timeit.timeit(lambda: RabinKarp(text2, pattern2_real), number=1000) < timeit.timeit(lambda: RabinKarp(text2, pattern2_real), number=1000):
    print ('RabinKarp швидший в пошуку реального підрядка у другій статті')
else:
    print('KMP швидший в пошуку реального підрядка у другій статті')


if timeit.timeit(lambda: BoyerMoore(text2, pattern2_fake), number=1000) < timeit.timeit(lambda: KMP(text2, pattern2_fake), number=1000):
    print ('Boyer-Moore швидший в пошуку неіснуючого підрядка у другій статті')
elif timeit.timeit(lambda: RabinKarp(text2, pattern2_fake), number=1000) < timeit.timeit(lambda: KMP(text2, pattern2_fake), number=1000):
    print ('RabinKarp швидший в пошуку неіснуючого підрядка у другій статті')
else:
    print ('KMP швидший в пошуку неіснуючого підрядка у другій статті')