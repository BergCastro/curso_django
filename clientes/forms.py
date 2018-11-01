from django.forms import ModelForm
from .models import Cliente

class ClientesForm(ModelForm):
    class Meta:
        model = Cliente 
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo' ]