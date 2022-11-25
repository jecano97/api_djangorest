from rest_framework import status

from tests.test_setup import TestSetUp
from tests.factories.rolesorg.rolesorg_factories import RolesOrgFactory
from rolesorg.models import RolesOrg

class RolesOrgTestCase(TestSetUp):
    url = '/apirolesorg/'

    def test_get_rolesorg(self):
        rolorg = RolesOrgFactory().create_rolesorg()
        response = self.client.get(
            self.url + 'RolesOrg/',
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['descriEng'], rolorg.descriEng)
        self.assertEqual(len(response.data), 1)
        # import pdb; pdb.set_trace()

    def test_create_rolesorg(self):
        rolorg = RolesOrgFactory().build_rolesorg_JSON()
        response = self.client.post(
            self.url + 'RolesOrg/',
            rolorg,
            format='json'
        )

        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['mensaje'], 'Registro creado')
        self.assertEqual(RolesOrg.objects.all().count(), 1)
        self.assertEqual(response.data['data']['codigo'], rolorg['codigo'])
        # import pdb; pdb.set_trace()

    def test_update_rolesorg(self):
        rolorg = RolesOrgFactory().create_rolesorg()
        response = self.client.put(
            self.url + 'RolesOrg/' + str(rolorg.idRolOrg) + '/',
            {
                'cveMo': rolorg.cveMo,
                'codigo': rolorg.codigo,
                'consecutivo': rolorg.consecutivo,
                'descriEng': 'Test Edit',
                'descriSpa': 'Prueba Editada',
                'definicionEng': rolorg.definicionEng,
                'definicionSpa': rolorg.definicionSpa,
                'fuenteInf': rolorg.fuenteInf,
                'fecRegInf': rolorg.fecRegInf
            },
            format='json'
        )

        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['mensaje'], 'Registro actualizado')
        self.assertNotEqual(response.data['data']['descriEng'], rolorg.descriEng)

    def test_rolesorg_delete(self):
        rolorg = RolesOrgFactory().create_rolesorg()
        response = self.client.delete(
            self.url + 'RolesOrg/' + str(rolorg.idRolOrg) + '/',
            format='json'
        )

        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['mensaje'], 'Registro eliminado correctamente')
        self.assertEqual(RolesOrg.objects.all().count(), 0)

        