from faker import Faker
from usuarios.models import User

faker = Faker()

class UsersFactory:

    def build_users_JSON(self):
        return {
            'username': faker.name(),
            'password':'tester2',
            'correo':faker.email(),
            'nombre':'Test2',
            'apellidos':'Tests2',
            'genero':'F',
            'rol':'Tester2',
            'fechaCreacion': ''
        }

    def create_users(self):
        return User.objects.create(**self.build_users_JSON())

        