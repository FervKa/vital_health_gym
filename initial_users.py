from user_class_gym import Client
from membership_class import Membership
from commons import get_current_date


# ------------ Creating the initial memberships ------------#
""" three_months_membershipership = Membership(
    "Three Months",
)
month_membership = Membership("Month")
peer_day_membership = Membership("Peer day") """
# ------------ Creating the initial users ------------#
dummy_users = [
    Client(
        3291121,
        "Oscar",
        "Murillo",
        23,
        "5555555555",
        True,
        True,
        get_current_date(),
    ),
    Client(
        3123223,
        "Carlos",
        "Jaramillo",
        32,
        "2222222222",
        False,
        True,
        "2024-03-20",
    ),
    Client(
        2322012,
        "Santiago",
        "Molina",
        21,
        "3333333333",
        True,
        False,
        "2024-05-24",
    ),
    Client(
        3332213,
        "Andrés",
        "Molina",
        19,
        "4444444444",
        False,
        False,
        "2024-05-24",
    ),
    Client(
        5151213,
        "Jose",
        "Molina",
        24,
        "6666666666",
        True,
        True,
        "2024-02-24",
    ),
    Client(
        6634234,
        "Fernando",
        "Espinoza",
        46,
        "7777777777",
        False,
        False,
        "2024-01-24",
    ),
]
