from django import forms
from app.models import Prenda

class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = "__all__"
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'input'}))
    color = forms.CharField(label="Color", widget=forms.TextInput(attrs={'class': 'input'}))
    talla = forms.CharField(label="Talla", widget=forms.TextInput(attrs={'class': 'input'}))
    material = forms.CharField(label="Material", widget=forms.TextInput(attrs={'class': 'input'}))
    genero = forms.CharField(label="Género", widget=forms.TextInput(attrs={'class': 'input'}))
    marca = forms.CharField(label="Marca", widget=forms.TextInput(attrs={'class': 'input'}))
    categoria = forms.CharField(label="Categoría", widget=forms.TextInput(attrs={'class': 'input'}))
    precio = forms.FloatField(label="Precio", widget=forms.NumberInput(attrs={'class': 'input'}))
    cantidad = forms.IntegerField(label="Cantidad", widget=forms.NumberInput(attrs={'class': 'input'}))
