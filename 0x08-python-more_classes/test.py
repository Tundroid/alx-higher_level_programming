#!/usr/bin/python3
class User:
    id = 1


u = User()
u.id = 89
User.id = 98
print(u.id)
print(User.id)