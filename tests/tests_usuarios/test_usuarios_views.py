from rest_framework import status

from tests.test_setup import TestSetUp
from tests.factories.usuarios.usuarios_factories import UsersFactory
from usuarios.models import *

class UsersTestCase(TestSetUp):
    url = '/apiusuarios/'

    def test_get_users(self):
        user = UsersFactory().create_users()
        response = self.client.get(
            self.url + 'Usuario/',
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['nombre'], user.nombre)
        self.assertEqual(len(response.data), 2)
        # import pdb; pdb.set_trace()

    def test_create_users(self):
        user = UsersFactory().build_users_JSON()
        response = self.client.post(
            self.url + 'Usuario/',
            user,
            format='json'
        )

        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['mensaje'], 'Registro creado')
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(response.data['data']['nombre'], user['nombre'])

    def test_update_user(self):
        user = UsersFactory().create_users()
        response = self.client.put(
            self.url + 'Usuario/' + str(user.id) + '/',
            {
                'username': user.username,
                'correo':user.correo,
                'nombre':'Test2_edit',
                'apellidos':'Tests2_edit',
                'genero':user.genero,
                'rol':user.rol
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['mensaje'], 'Registro actualizado')
        self.assertNotEqual(response.data['data']['nombre'], user.nombre)
        # import pdb; pdb.set_trace()

    def test_delete_user(self):
        user = UsersFactory().create_users()
        response = self.client.delete(
            self.url + 'Usuario/' + str(user.id) + '/',
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['mensaje'], 'Usuario eliminado correctamente!')
        self.assertEqual(User.objects.all().count(), 1)

    def test_set_password_user(self):
        user = UsersFactory().create_users()
        response = self.client.post(
            self.url + 'Usuario/' + str(user.id) + '/set_password/',
            {
                "password": '1234567',
                "password2": '1234567'
            },
            format='json'
        )

        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['mensaje'], 'Contraseña actualizada correctamente')

