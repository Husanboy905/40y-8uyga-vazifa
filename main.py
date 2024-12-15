# 1-misol
# raqam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rqamamni_kvadratka  = list(map(lambda x: x**2, raqam))
# print(rqamamni_kvadratka )

# 2-misol
# harc = ["A", "a", "B", "b", "C", "c", "D", "d"]
# kara_harf = list(filter(lambda x: x.isupper(), harc))
# print(kara_harf)

# 3-misol
# def get_country_code(telfon_raqam):
#     return telfon_raqam.split('+')[1][0:3]
#
# raqm = ["+998991234567", "+79454874459", "+14385001031"]
# telfon = list(map(get_country_code, raqm))
#
# print(telfon)

# 4-misol
# def get_country_code(isimlar):
#     return isimlar.capitalize()
#
# a = ['alfred', 'tabitha', 'william', 'arla']
# b = list(map(get_country_code, a))
#
# print(b)

# 5-misol
# raqamlar_rohati = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# def raqam_filtr(score):
#     return score > 75
#
# jovobu = list(filter(raqam_filtr, raqamlar_rohati))
# print(jovobu)

# 6-misol
# royhat = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# palindromes = list(filter(lambda x: x.lower() == x[::-1].lower(), royhat))
# print(palindromes)

# 7-misol
# mevalar_royhay = ['apple', 'banana', 'cherry']
# meva = list(map(len, mevalar_royhay))
# print(meva)


# 8-misol
# list1 = ['apple', 'banana', 'cherry']
# list2 = ['orange', 'lemon', 'pineapple']
# chiqish = list(map(lambda x, y: x + y, list1, list2))
# print(chiqish)

# 9-misol
# list1 = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# list2 = ["Sobir", "Bakir", "Jalil", "Toxir"]
# merged = list1 + list2
# print(merged)

# 10-misol
# def count_occurrences(lst, element):
#     return lst.count(element)
#
# royhat = [1, 2, 3, 2, 4, 2, 5]
# element = 2
# print(count_occurrences(royhat, element))


# 11-misol
# list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = list(filter(lambda x: x in list2, list1))
# print(a)


# 12-misol
# a = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# b = a[::2]
# print(b)


# 13-misol
# a = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# b = a.index("Basic")
# print(a[b:])


# 15-misol
# squares = (x**2 for x in range(1, 21))
# print(list(squares))

# 16-misol
# def text_uzunligu():
#     def inner(text):
#         return len(text)
#     return inner
#
# a = text_uzunligu()
# print(a("Hello, World!"))

# 17-misol
# def greet():
#     def inner(name):
#         return f"Salom, {name}!"
#     return inner
#
# a = greet()
# print(a("husanboy"))
