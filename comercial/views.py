from django.shortcuts import render, redirect
from .models import Direccion, Usuario
from .forms import UsuarioForm
from django.contrib.auth.models import User, Group
# Create your views here.

#@permission_required('comunidad.add_usuario', raise_exception=True)
def usuario_crear(request):
    titulo="Registro"
    accion="Registrarme"
    usuarios= Usuario.objects.all()
    if request.method=="POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['documento']):
                user = User.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['documento']
                user.first_name= request.POST['primer_nombre']
                user.last_name= request.POST['primer_apellido']
                user.email= request.POST['correo']
                #user.password=make_password("@" + request.POST['primer_nombre'][0] + request.POST['primer_apellido'][0] + request.POST['documento'][-4:])
                user.save()
            else:
                user=User.objects.get(username=request.POST['documento'])
            rol_id = request.POST.get('rol')  # Obtén el ID del grupo seleccionado en el formulario
            if rol_id:
                rol = Group.objects.get(id=rol_id)
                user.groups.add(rol)  # Asocia el usuario al grupo
            usuario = Usuario.objects.create(
                nombre=request.POST['nombre'],
                apellidos=request.POST['apellidos'],
                tipo_documento=request.POST['tipo_documento'],
                documento=request.POST['documento'],
                correo=request.POST['correo'],
                celular=request.POST['celular'],
                telefono_fijo=request.POST['telefono_fijo'],
                password=request.POST['password'],
                direccion=request.POST['direccion'],
                user=user,
                
            )
            #messages.success(request, f'¡El Usuario se agregó de forma exitosa!')
            """ if usuario.imagen:
                 img = Image.open(usuario.imagen.path)
                 img= img.resize((500,500))
                 img.save(usuario.imagen.path) """
            usuario.save()
            return redirect('usuarios')

        else:
            #messages.success(request, f'¡Error al agregar al Usuario!')
            form = UsuarioForm(request.POST)
    else:
        form=UsuarioForm()
    context={
        "titulo":titulo,
        "usuarios":usuarios,
        "form":form,
        "accion":accion
    }
    return render(request,"comercial/registro.html", context)