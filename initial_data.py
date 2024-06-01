from user_class_gym import Client
from membership_class import Membership
from commons import get_current_date
from lockers_class import Locker
from gym_class import Gym


# ------------ Creating the initial lockers ------------#
dummy_lockers = [
    Locker(1, False, "blue", "simple", 3291121),
    Locker(2, False, "red", "double", 3123223),
    Locker(3, False, "green", "simple", 3332213),
    Locker(4, False, "blue", "simple", 5151213),
    Locker(5, True, "red", "simple", None),
    Locker(6, True, "green", "simple", None),
    Locker(7, True, "blue", "simple", None),
    Locker(8, True, "red", "simple", None),
    Locker(9, True, "green", "double", None),
    Locker(10, True, "blue", "simple", None),
    Locker(11, True, "red", "simple", None),
    Locker(12, True, "green", "simple", None),
    Locker(13, True, "blue", "simple", None),
    Locker(14, True, "red", "double", None),
    Locker(15, True, "green", "simple", None),
    Locker(16, True, "blue", "double", None),
    Locker(17, True, "red", "simple", None),
    Locker(18, True, "green", "double", None),
    Locker(19, True, "blue", "simple", None),
    Locker(20, True, "red", "simple", None),
]

# ------------ Creating the initial memberships ------------#
dummy_memberships = [
    Membership("Daily", True, 10000),
    Membership("Monthly", True, 110000),
    Membership("Three Months", True, 280000),
]

# ------------ Creating the initial users ------------#
dummy_users = [
    Client(
        3291121,
        "Oscar",
        "Murillo",
        23,
        "5555555555",
        True,
        dummy_memberships[2],
        True,
        get_current_date(),
        "2024-05-24",
        True,
        dummy_lockers[0],
    ),
    Client(
        3123223,
        "Carlos",
        "Jaramillo",
        32,
        "2222222222",
        True,
        dummy_memberships[2],
        True,
        get_current_date(),
        "2024-02-24",
        True,
        dummy_lockers[1],
    ),
    Client(
        2322012,
        "Santiago",
        "Molina",
        21,
        "3333333333",
        True,
        dummy_memberships[2],
        True,
        get_current_date(),
        "2024-05-24",
        True,
        dummy_lockers[2],
    ),
    Client(
        3332213,
        "Andrés",
        "Molina",
        19,
        "4444444444",
        True,
        dummy_memberships[2],
        True,
        get_current_date(),
        "2024-05-24",
        True,
        dummy_lockers[3],
    ),
    Client(
        5151213,
        "Jose",
        "Molina",
        24,
        "6666666666",
        True,
        dummy_memberships[2],
        True,
        get_current_date(),
        "2024-05-24",
        True,
        dummy_lockers[4],
    ),
    Client(
        6634234,
        "Fernando",
        "Espinoza",
        46,
        "7777777777",
        True,
        dummy_memberships[2],
        True,
        get_current_date(),
        "2024-05-24",
        False,
        None,
    ),
]

# ------------- Creating initial gym --------------------#
michael_gym = Gym(3221231, "Michael Gym", "Calle 123")


