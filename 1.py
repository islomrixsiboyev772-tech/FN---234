# 1----------------------------------
# def nums(a):
#     dct = {}
#     for son in a:
#         if son not in dct:
#             dct[son] = 1
#         else:
#             dct[son] +=1
#     print(max(dct))

# lst = [2, 2, 1, 1, 1, 2, 2]
# nums(lst)


# 2--------------------------------
# def search_by_genre(cinema: list, genre: str) -> list:
#     lst = []
#     for kino in cinema:
#         if kino['genre'] == genre:
#             lst.append(kino)
#     return lst


# cinema = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]
# print(search_by_genre(cinema, "Fantastika"))
# print(search_by_genre(cinema, "Drama"))
# print(search_by_genre(cinema, "Komediya"))


# 3--------------------------
# def merge_unique_ids(active_users: list, new_users: list) -> list:
#     natija = list(set(active_users + new_users))
#     natija.sort()

#     return natija
        
# active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
# new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']

# print((merge_unique_ids(active_users, new_users)))


# 4-------------------------
# def sorted_by_price(products: list) -> list:
#     natija = sorted(products, key=lambda x: int(x[1]), reverse=True)

#     print(natija)

# products = [
#     ('Olma', '12000', '50'),
#     ('Banan', '8000', '100'),
#     ('Gilos', '15000', '70'),
#     ('Apelsin', '9000', '80'),
#     ('Anor', '30000', '20'),
#     ('Uzum', '20000', '40'),
#     ('Tarvuz', '25000', '15'),
#     ('Shaftoli', '18000', '60'),
#     ('Qovun', '40000', '25'),
#     ('Qulupnay', '35000', '10')
# ]
# print(sorted_by_price(products))


# 5---------------------------

def are_numbers_ascending(text: str) -> bool:
    sonlar = []

    for i in text.split():
        if i.isdigit():
            sonlar.append(int(i))

    for i in range(len(sonlar) - 1):
        if sonlar[i] >= sonlar[i + 1]:
            return False

    return True


print(are_numbers_ascending("1 qutida 5 ta yashil, 9 ta qizil, 12 ta sariq top bor edi"))
print(are_numbers_ascending("musobaqada 5 ga 5 korinishida oyinlar otkazildi"))
print(are_numbers_ascending("26 oquvchidan 3 tasi 5 baxo oldi"))
