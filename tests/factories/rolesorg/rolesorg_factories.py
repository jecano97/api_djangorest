from faker import Faker
from rolesorg.models import RolesOrg

faker = Faker()

class RolesOrgFactory:

    def build_rolesorg_JSON(self):
        return {
            'cveMo': faker.random_number(digits=1),
            'codigo': str(faker.random_number(digits=11)),
            'consecutivo': str(faker.random_number(digits=5)),
            'descriEng': 'Test',
            'descriSpa': 'Prueba',
            'definicionEng': 'It is a test',
            'definicionSpa': 'Es una prueba',
            'fuenteInf': 'NA',
            'fecRegInf': '2022-06-22'
        }
    
    def create_rolesorg(self):
        return RolesOrg.objects.create(**self.build_rolesorg_JSON())