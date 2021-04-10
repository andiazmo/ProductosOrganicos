from rest_framework import serializers
from .models import *

class carritoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields= ('usuario_id','item_compras', 'precio_total')
