from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #requerido para los tokens de SIMPLEJWT
from usuarios.models import (
    Empleado,
    DatosLaborales,
    HistorialUsuario,
    Departamento,
    Cargo,
    Contrato,
    User
)
#SERIALIZER PARA JWT
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','correo','nombre','apellidos','genero','rol','fechaCreacion']

#SERIALIZERS PARA EL MANEJO DE LOS USUARIOS
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','correo','nombre','apellidos','genero','rol','fechaCreacion']

    def create(self,validated_data):
        usuario = User(**validated_data)
        usuario.set_password(validated_data['password']) #this encrypts the password 
        usuario.save()
        return usuario

class EditarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','correo','nombre','apellidos','genero','rol']

class ListarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'correo': instance['correo'],
            'password': instance['password'],
            'nombre': instance['nombre'],
            'apellidos': instance['apellidos'],
            'genero': instance['genero'],
            'rol': instance['rol'],
            'fechaCreacion': instance['fechaCreacion'],
            'last_login': instance['last_login']
        }

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

# SERIALIZERS PARA MANEJAR TABLAS SECUNDARIOAS DE USUARIOS
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['idEmpleado','fechaNac','lugarNac','RFC','CURP','celular','calle','noInt','noExt','fk_User','fk_CP']

class DatosLaboralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosLaborales
        fields = ['idDatosLab','codigo','fechaIng','fechaBaja','sueldoMensual','referencia1','referencia2','ubicacion','procedencia','observaciones','fk_Empleado','fk_Cargo','fk_Contrato']

class HistorialUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialUsuario
        fields = ['id','usuario','entidad','modulo','movimiento','fecha','observaciones']

# SERIALIZERS PARA MANEJAR TABLAS EXTRAS DE USUARIOS
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['idDepto','nombre']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['idCargo','nombre','fk_Depto']

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ['idContrato','tipo']