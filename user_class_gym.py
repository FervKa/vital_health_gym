import users_gym


class Client:
    def __init__(self, id: int, name: str, last_name: str, age: int):
        self._id = id
        self._name = name
        self.last_name = last_name
        self.age = age
        self.status = False

    @property
    def _id(self):
        return self._id

    @_id.setter
    def _id(self, id):
        if isinstance(id, int) and id >= 0:
            self._id = id
        else:
            raise ValueError("Invalid user ID")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def join_gym(self):
        self.status = True
        print(f"User {self.name} {self.last_name} joined the gym")

    def left_gym(self):
        self.status = False
        print(f"User {self.name} {self.last_name} left the gym")


firts_user = Client(3291121, "Oscar", "Murillo", 23)
firts_user.join_gym()
firts_user.left_gym()


""" # Methods for interacting with the gym environment
    def join_gym(self, user):
        Join a specific gym.
        if not isinstance(user, users_gym.users):
            raise TypeError("Argument must be of type 'users_gym.Gym'")

        print(f"User {self.name} {self.last_name} joined the gym")
        user.add_user(self)

    def leave_gym(self, user):
        Leave a specific gym.
        if not isinstance(user, users_gym.users):
            raise TypeError("Argument must be of type 'users_gym.Gym'")

        user.remove_user(self)
        print(f"User {self.name} {self.last_name} left the gym") """
