from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import *

class UserCreationForm(forms.ModelForm):
    #crear new users incluyendo todos los campos requeridos
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'username')

    def clean_password2(self):
        #para ver que las 2 passwords sean iguales
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las Contrasenas no son iguales")
        return password2

    def save(self, commit=True):
        #guardar la contrasena en hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    #este es para actualizar al usuario y todos sus campos excepto la password creo
    password = ReadOnlyPasswordHashField

    class Meta:
        model = CustomUser
        fields = ('email','username','password','is_active','is_admin')
    
    def clean_password(self):
        #
        return self.initial["password"]
    
class UserAdmin(BaseUserAdmin):
    #el form para agregar y cambia instancias de usuario
    form = UserChangeForm
    add_form = UserCreationForm

    #campos que apareceran en admin en el User Model
    list_display = ('id_user','email','username','is_admin','password')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info', {'fields': ('username','fechaNac',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','password1','password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()