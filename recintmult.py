# def recintmult(first_number: int, second_number: int, n) -> int:
#     first_number_str = str(first_number)
#     second_number_str = str(second_number)
#
#     if len(first_number_str) and len(second_number_str) == 1:
#         return first_number * second_number
#     else:
#         middle_f = int(len(first_number_str)/2)
#         middle_s = int(len(second_number_str)/2)
#         a = int(first_number_str[:middle_f])
#         b = int(first_number_str[middle_f:])
#         c = int(second_number_str[:middle_s])
#         d = int(second_number_str[middle_s:])
#         print(a, b, c, d)
#
#     ac = recintmult(a, c, n)
#     ad = recintmult(a, d, n)
#     bc = recintmult(b, c, n)
#     bd = recintmult(b, d, n)
#
#     print("вызываю итог", ac, ad, bc, bd)
#     itog(ac, ad, bc, bd, n)
#
#
# def itog(ac, ad, bc, bd, n) -> int:
#     print("ура")
#     return 10 ** n * ac + 10 ** n/2 + (ad + bc) + bd
#
#


