# # ARITHMETIC
#
# # Addition
#
# print(4 + 3)
#
# # Subtraction
#
# print(4 - 3)
#
# # Multiplication
#
# print(4 * 3)
#
# # Division
#
# print(6 / 4) #prints float
# print(6 // 4) #prints int
#
# # Remainder
#
# print(6 % 4)
#
# # Exponent
#
# print(6 ** 2)
#
# x = 10
# for x in [x - 3, 51]:
#     while x < 50:
#         x = x + 3
#         if x <= 50:
#             print(x)
#         else:
#             exit()
#
# # Comparison operators that give Boolean results:
#     # >
#     # <
#     # >=
#     # <=
#     # == checks if first value is equal to the second
#     # != checks if first value does not equal the second

# Weight converter program
weight = input("How much do you weigh?: ")
weight_unit = input("Is that in kg or lbs? ")
if weight_unit.lower == "k" or weight_unit.lower == "kg":
    print("Weight in Kg: " + weight)
    print(f"Weight in Lbs: {float(weight) * 2.204623}")
else:
    print(f"Weight in Lbs: {weight}")
    print(f"Weight in Kg: {float(weight) * 0.4535924}")



