from user_class_gym import Client
from commons import users_list, save_user
from general_report import General_report, general_users

firts_user = Client(3291121, "Oscar", "Murillo", 23, "2020-01-30")
second_user = Client(3123223, "Carlos", "Jaramillo", 32, "2021-03-20")
third_user = Client(2322012, "Santiago", "Molina", 33, "2019-05-24")


def create_user(_id, name, last_name, age, date):
    save_user(Client(_id, name, last_name, age, date), Client, users_list)


save_user([firts_user, second_user, third_user], Client, users_list)

for user in general_users:
    print(f"User: {user.get_name}")
