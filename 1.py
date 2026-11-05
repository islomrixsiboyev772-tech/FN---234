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