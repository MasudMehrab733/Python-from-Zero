# #using if else condition
# age = 18
# input("age of the candidate: ")
# if age>18:
#     print("your eligible for married.")
#
# else:
#         print("Not eligible")
#
#
#
#
# is eligible for scholarship or not
gpa = float(input("Enter your gpa: "))
if gpa >3.50:
    print(f" With gpa {gpa} is eligible for scholarship.")
elif 3.00 <=gpa<=3.50 :
    print(f"With gpa {gpa} is pending for discussion.")

elif gpa < 3.00:
    print(f"With gpa {gpa} is not eligible for scholarship.")
else:
    print("Rejected perticipate.")


