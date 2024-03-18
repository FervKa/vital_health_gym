import users_gym


class GymClient:
    def __init__(self, id_code: int, name: str, last_name: str, age: int):
        self.id_code = id_code
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def id_code(self):
        return self.id_code

    @id_code.setter
    def id_code(self, value):
        if isinstance(value, int) and value >= 0:
            self.id_code = value
        else:
            raise ValueError("Invalid user ID")

    # Methods for interacting with the gym environment
    def join_gym(self, user):
        """Join a specific gym."""
        if not isinstance(user, users_gym.users):
            raise TypeError("Argument must be of type 'users_gym.Gym'")

        print(f"User {self.name} {self.last_name} joined the gym")
        user.add_user(self)

    def leave_gym(self, user):
        """Leave a specific gym."""
        if not isinstance(user, users_gym.users):
            raise TypeError("Argument must be of type 'users_gym.Gym'")

        user.remove_user(self)
        print(f"User {self.name} {self.last_name} left the gym")


""" user1 = GymClient(1, "Oscar", "Murillo", 23)
print(vars(user1)) """
