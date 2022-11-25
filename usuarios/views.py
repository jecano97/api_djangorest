from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from usuarios.models import User
from usuarios.serializers import (
    EmpleadoSerializer,
    DatosLaboralesSerializer,
    HistorialUsuarioSerializer,
    CargoSerializer,
    DepartamentoSerializer,
    ContratoSerializer,
    PasswordSerializer,
    EditarUsuarioSerializer,
    UsuarioSerializer,
    ListarUsuarioSerializer,
    CustomTokenObtainPairSerializer, CustomUserSerializer
)
# Create your views here.

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesión Exitoso.'
                }, status = status.HTTP_200_OK)
            return Response({'error':'Contraseña o username incorrecto.'}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Contraseña o nombre de usuario incorrectos'}, status = status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView): #ESTA FUNCION ESTA DE ADORNO, PORQUE REALMENTE AL HACER EL LOGOUT NO SE ELIMINA EL TOKEN, ESO SI, EL TOKEN ASIGNADO AL USUARIO SE ACTUALIZA POR OTRO
    #PERO EL ANTERIOR SIGUE FUNCIONANDO
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(correo=request.data.get('email',''))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message':'Sesión cerrada correctamente.'}, status = status.HTTP_200_OK)
        return Response({'error', 'No existe este usuario'}, status = status.HTTP_400_BAD_REQUEST)

class UsuarioViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UsuarioSerializer
    list_serializer_class = ListarUsuarioSerializer
    query = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all().values('id','username','correo','password','nombre','apellidos','genero','rol','fechaCreacion','last_login')
        return self.queryset
    
    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({'mensaje': 'Contraseña actualizada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':password_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def set_active_on(self, request, pk=None):
        user = self.get_object(pk)
        if user.is_active == False:
            user.is_active = True
            user.save()
            return Response({'mensaje': 'Usuario activado correctamente'}, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje': 'El usuario ya esta activo'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def set_active_off(self, request, pk=None):
        user = self.get_object(pk)
        if user.is_active == True:
            user.is_active = False
            user.save()
            return Response({'mensaje': 'Usuario desactivado correctamente'}, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje': 'El usuario ya esta desactivado'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        usuarios = self.get_queryset()
        users_serializer = self.list_serializer_class(usuarios, many=True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'mensaje':'Registro creado','data':user_serializer.data}, status = status.HTTP_201_CREATED)
        return Response({'error':user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):#SE TRAE 1 USUARIO ESPECIFICO, RECIBIENDO EL ID POR PARAMETRO MEDIANTE PETICION GET
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        usuario = self.get_object(pk)
        user_serializer = EditarUsuarioSerializer(usuario, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'mensaje':'Registro actualizado','data':user_serializer.data}, status = status.HTTP_200_OK)
        return Response({'error':user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        usuario = User.objects.filter(id=pk).first()
        # usuario = self.model.objects.filter(id=pk).update(is_active=False)
        if usuario:
            usuario.delete()
            return Response({'mensaje':'Usuario eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'mensaje':'No se a encontrado un usuario con estos datos'}, status = status.HTTP_404_NOT_FOUND)

#VISTAS PARA EL CONTROL DE LAS TABLAS SECUNDARIAS DE USUARIOS

class VistaEmpleado(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idEmpleado = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idEmpleado=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaDatosLaborales(viewsets.ModelViewSet):
    serializer_class = DatosLaboralesSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDatosLab = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idDatosLab=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaHistorialUsuario(viewsets.ModelViewSet):
    serializer_class = HistorialUsuarioSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(id=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

#VISTAS PARA EL CONTROL DE LAS TABLAS EXTRAS DE USUARIOS
class VistaCargo(viewsets.ModelViewSet):
    serializer_class = CargoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idCargo = pk).first()

class VistaDepartamento(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDepto = pk).first()

class VistaContrato(viewsets.ModelViewSet):
    serializer_class = ContratoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idContrato = pk).first()


