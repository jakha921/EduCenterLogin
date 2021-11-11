from django import forms
from django.db.models import fields
from django.forms import ModelForm, TextInput
from .models import clients, parents

class clientsForm(ModelForm):
    class Meta:
        model = clients
        fields = ['groups_clients_id', 'user_name', 'contc', 'id_cart_seria', 'id_cart_num', 'address', 'password']

        widgets = {
            "user_name": TextInput(attrs={
                'class' : "input100",
                'type'  : "text",
                'name'  : "name",
                'placeholder' : "Full name",
            }),
            
            "contc": TextInput(attrs={
                'class' : "input100",
                'type' : "number",
                'name' : "phone",
                'placeholder' : "Phone",
            }),

            "id_cart_seria": TextInput(attrs={
                'class' : "input100",
                'type' : "text",
                'name' : "pass_series",
                'placeholder' : "AA",
            }),

            "id_cart_num": TextInput(attrs={
                'class' : "input100",
                'type' : "number",
                'name' : "pass_number",
                'placeholder' : "1234567",
            }),

            "address": TextInput(attrs={
                'class' : "input100",
                'type' : "text",
                'name' : "address",
                'placeholder' : "Navoi st, 3v home, 20 flat",
            }),

            "password": TextInput(attrs={
                'class' : "input100",
                'type' : "password",
                'name' : "pass",
                'placeholder' : "Password",
            }),


        }
class parentsForm(ModelForm):
    class Meta:
        model = parents
        fields = ['parent_name', 'phone', 'address', 'password']

        widgets = {
            "parent_name": TextInput(attrs={
                'class' : "input100",
                'type'  : "text",
                'name'  : "name",
                'placeholder' : "Full name",
            }),
            
            "phone": TextInput(attrs={
                'class' : "input100",
                'type' : "number",
                'name' : "phone",
                'placeholder' : "Phone",
            }),

            "address": TextInput(attrs={
                'class' : "input100",
                'type' : "text",
                'name' : "address",
                'placeholder' : "Navoi st, 3v home, 20 flat",
            }),

            "password": TextInput(attrs={
                'class' : "input100",
                'type' : "password",
                'name' : "pass",
                'placeholder' : "Password",
            }),


        }