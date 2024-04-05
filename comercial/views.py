from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import RegistroUsuario, ActualizarUsuarioForm, CambiarContraseniaForm

# Create your views here.
def login_usuario(request):
    titulo="Ingreso"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, '¡Bienvenido/a! Has ingresado satisfactoriamente')
            return redirect('index')
        else:
            messages.error(request, 'Error. Usuario o contraseña inválidos')

    context={
        "titulo": titulo,
    }
    return render(request, "comercial/login.html", context)

def logout_usuario(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión satisfactoriamente.')
    return redirect('login')

def registro_usuario(request):
    
    titulo="Registro"
    form = RegistroUsuario(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        first_name=form.cleaned_data.get('first_name')
        last_name=form.cleaned_data.get('last_name')
        tipo_documento=form.cleaned_data.get('tipo_documento')
        documento=form.cleaned_data.get('documento')
        numero_telefono=form.cleaned_data.get('numero_telefono')
        numero_celular=form.cleaned_data.get('numero_celular')
        direccion=form.cleaned_data.get('direccion')
        municipio=form.cleaned_data.get('municipio')
        barrio_vereda=form.cleaned_data.get('barrio_vereda')

        user = Usuario.objects.create_user(username=username, email=email, password=password)

        user.first_name = first_name
        user.last_name = last_name
        user.tipo_documento = tipo_documento
        user.documento = documento
        user.numero_telefono = numero_telefono
        user.numero_celular = numero_celular
        user.direccion = direccion
        user.municipio = municipio
        user.barrio_vereda = barrio_vereda

        user.save()
            
        if user:
            login(request, user)
            messages.success(request, 'Te has registrado correctamente')
            return redirect('index')

    context={
        "titulo": titulo,
        "form": form
    }
    return render(request, "comercial/registro.html", context)

# Función para actualizar los datos del usuario. se valida que el documento no pertenezca a otro usuario.    
def actualizar_datos(request, id):
    user = Usuario.objects.get(id = id)
    titulo="Actualización de datos"

    if request.method=="POST":
        form= ActualizarUsuarioForm(request.POST)
        if form.is_valid():
            aviso_validar_documento = False
            #Obteniendo los datos del formulario.
            email=form.cleaned_data.get('email')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            tipo_documento=form.cleaned_data.get('tipo_documento')
            documento=form.cleaned_data.get('documento')
            numero_telefono=form.cleaned_data.get('numero_telefono')
            numero_celular=form.cleaned_data.get('numero_celular')
            direccion=form.cleaned_data.get('direccion')
            municipio=form.cleaned_data.get('municipio')
            barrio_vereda=form.cleaned_data.get('barrio_vereda')

            #Asignando variables
            user.email=email
            user.first_name = first_name
            user.last_name = last_name
            user.tipo_documento = tipo_documento
            id_usuario_actual = user.id
            datos = Usuario.objects.filter(documento=documento).values()
            if datos.exists():  # Verificar si hay elementos en el QuerySet
                primer_dato = datos.first()
                if id_usuario_actual != primer_dato['id'] and primer_dato['id'] != 1:
                    aviso_validar_documento = True
                    messages.error(request, '!Atención¡ Ingresa otro numero de documento. El que ingresaste está siendo usado por otro usuario/a.')
                else:
                    user.documento = documento
            else:
                user.documento = documento
            user.numero_telefono = numero_telefono
            user.numero_celular = numero_celular
            user.direccion = direccion
            user.municipio = municipio
            user.barrio_vereda = barrio_vereda

            user.save()
           
            if aviso_validar_documento:
                messages.success(request, 'Los damás datos se han actualizado de forma exitosa.')
            else:
                messages.success(request, 'Has actualizado tus datos de forma exitosa.')
            return redirect("index")
        else:
            messages.error(request, 'Error al actualizar.')
    else:
        form=ActualizarUsuarioForm()

    context={
        "titulo": titulo,
        "form":form
    }
    return render(request, "usuario/actualizar_datos.html", context)

# Función para eliminar usuarios: Cerrar la cuenta del usuario.
def cerrar_cuenta_usuario(request, id):
    user = Usuario.objects.get(id = id)
    user.delete()
    logout(request)
    messages.success(request, 'Has cerrado tu cuenta de forma exitosa.')
    return redirect("index")

@login_required
def cambiar_contrasenia(request):
    #user = Usuario.objects.get(id = id)
    titulo="Cambio de contraseña"

    if request.method == 'POST':
        form = CambiarContraseniaForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para no desloguear al usuario.
            messages.success(request, 'Has cambiado tu contraseña correctamente.')
            return redirect('index')  
    else:
        form = CambiarContraseniaForm(user=request.user)

    context={
        "titulo": titulo,
        "form":form
    }
    return render(request, "usuario/cambiar_contrasenia.html", context)