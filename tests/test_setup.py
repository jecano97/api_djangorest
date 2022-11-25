from faker import Faker

from rest_framework import status
from rest_framework.test import APITestCase

class TestSetUp(APITestCase): #ESTA CLASE, PERMITE HACER EL LOGIN, PARA PODER OBTENER EL TOKEN Y LLAMAR A TODOS LOS ENDPOINTS

    def setUp(self):
        from usuarios.models import User

        # print("enta el setup")

        faker = Faker()

        self.login_url = '/login/'
        self.user = User.objects.create_superuser(
            username=faker.name(),
            correo=faker.email(),
            nombre='Test2',
            apellidos='Tests',
            genero='M',
            rol='Tester',
            password='tester'
        )

        # print("usuario->",self.user.username)
        
        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'password': 'tester'
            },
            format='json'
        )
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #import pdb; pdb.set_trace() #PERMITE PAUSAR LA EJECUCION, Y ASI PODER REALIZAR TECNICAS DE DEBUG (como revisar que contiene una variable especifica) (SE USA EL caracter 'c' para indicar que continue con el fujo normal)
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()

    # def test_sasa(self): #BORRAR ESTA FUNCION
    #     pass