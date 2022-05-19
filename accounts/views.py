from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from .models import UsuarioP3

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


def login(request):
    return render(request, 'login.html')

def registro(request):
    usuariop=UsuarioP3.objects.all()
    datos = {'usuariosp': usuariop}
    return render(request, 'registro.html', datos)

def validarUsuarioP(request):
    try:
        v_name=request.POST.get('name')
        v_password=request.POST.get('password')

        usuariop=UsuarioP3.objects.get(password=v_password, nombre=v_name)
        
        
            #crear la sesion y redireccionar
        request.session['nombre']=usuariop.nombre
        return redirect('/verM')
        
    except:
        return redirect('/errorlogin') 

def errorlogin(request):
    return render(request, 'errorlogin.html')        
