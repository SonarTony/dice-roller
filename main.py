import random

# # Define the username and password
# stored_username = "admin"
# stored_password = "password123"
# # Get user input for username and password
# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")
# # Check if the entered username and password match the stored values
# if username_input == stored_username and password_input == stored_password:
#     print("Login successful!")
# else:
#     print("Login failed. Incorrect username or password.")
# a=0
# b=0
# def work():
#     return() 
# if b == b:
#     work()
# if b == b:
#     work()    
# if a == a: # Noncompliant
#     work()
# i = 0
# if not a == 2:
#     b = not i < 10
# if not a == 2:
#     b = not i < 10
# if not a == 2:
#     b = not i < 10
# if a == a:
#     work()

# if  a != a: # Noncompliant
#     work()

# if  a == b and a == b: # Noncompliant
#     work()

# if a == b or a == b: # Noncompliant
#     work()
# i = 0

# a = 4 / 4 
# j = 5 / 5 # Noncompliant
# k = 5 - 5 # Noncompliant   

# def roll_yellow_die():
#     return random.randint(1, 20)
# def roll_red_die():
#     return random.randint(1, 20)
# def roll_blue_die():
#     return random.randint(1, 20)
# def roll_white_die():
#     return random.randint(1, 6)
# def roll_whitish_die():
#     return random.randint(1, 6)
# def roll_black_die():
#     return random.choice([00, 10, 20, 30, 40, 50, 60, 70, 80, 90])
# def roll_grey_die():
#     return random.randint(0, 9)
# def roll_blackish_die():
#     return random.choice([00, 10, 20, 30, 40, 50, 60, 70, 80, 90])
# def roll_greyish_die():
#     return random.randint(0, 9)
# def user_choice():
#     choice = input("Enter 'r' to reroll or 'e' to end: ")
#     if choice == 'r':
#         return True
#     elif choice == 'e':
#         return False
#     else:
#         print("Invalid choice. Please enter 'r' to reroll or 'e' to end.")
#         return user_choice()
# puck_battle_number = int(input("Enter the Puck Battle number: "))
# reroll = True
# while reroll:
#     yellow_result = roll_yellow_die()

#     if yellow_result >= puck_battle_number:
#         print()
#         print("PUCK BATTLE")
#     else:
#         print()
#         print("ATTACK")

#     red_result = roll_red_die()
#     blue_result = roll_blue_die()
#     white_result = roll_white_die()
#     black_result = roll_black_die()
#     grey_result = roll_grey_die()
#     blackish_result = roll_blackish_die()
#     greyish_result = roll_greyish_die()
#     whitish_result = roll_whitish_die()
#     print("Puck Battle die result:", yellow_result)
#     print("Red die result:", red_result)
#     print("Blue die result:", blue_result)
#     print("Timing die result:", white_result, "Minutes")
#     print("Black die result:", black_result)
#     print("Grey die result:", grey_result)
#     print()
#     print("Second set of d10s and d6s")
#     print("blackish die result:", blackish_result)
#     print("Greyish die result:", greyish_result)
#     print("Whitish d6 result:", whitish_result)
#     print()
#     print()
#     print()
#     print()


def fun(a):
  i = 10
  return i + a       # Noncompliant
  i += 1             # this is never executed