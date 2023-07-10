from django.urls import path
from .views import LoginFormView, TurneroRegisterView, TurneroOrderView, TurneroListBox1View, eliminar_cliente

app_name="turnero"

urlpatterns = [
    
    path('',LoginFormView.as_view(), name="login"),
    path('login/', LoginFormView.as_view(), name='login'),
    path('registro/',TurneroRegisterView.as_view(), name="registro"),
    path('orden/', TurneroOrderView.as_view(), name="orden"),
    path('box1/', TurneroListBox1View.as_view(), name="box1"),
    path('eliminarCliente/<int:id>', eliminar_cliente, name="eliminarcliente"),
    
]




