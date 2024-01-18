from django import forms
from django.forms import ModelChoiceField, ModelForm, widgets
from .models import Usuario
from django.forms import Widget
from django.contrib.auth.models import Group, Permission
from django.contrib.admin.widgets import FilteredSelectMultiple


class UsuarioForm(ModelForm):
    """ rol= ModelChoiceField(
        queryset=Group.objects.all(),
        label="Rol",
    ) """
    class Meta:
        model= Usuario
        fields= "__all__"
        exclude=["estado","user"]
        """ widgets={
            'fecha_nacimiento':Widget.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }  """