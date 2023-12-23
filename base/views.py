from django.shortcuts import render, redirect

def principal(request):
    titulo="Bienvenid@s"
    # sliders= Slider.objects.filter(estado=True)
    # productos= Producto.objects.all()
    context={
        "titulo": titulo,
        # "sliders": sliders,
        # "productos":productos 
    }
    return render(request, "index.html", context)