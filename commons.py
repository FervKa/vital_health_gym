def validate_id(id):
    if isinstance(id, int):
        return id
    else:
        raise ValueError("Invalid user ID, it must be int")


users_list = []


def save_user(users, class_type, users_list):
    if isinstance(users, class_type):
        users_list.append(users)
    elif isinstance(users, list):
        for user in users:
            users_list.append(user)
