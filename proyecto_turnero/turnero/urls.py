from django.urls import path
from .views import LoginFormView, TurneroRegisterView, TurneroOrderView, TurneroListBox1View, TurneroUpdateView, TurneroDeleteView, TurneroCheckView

app_name="turnero"

urlpatterns = [
    
    path('',LoginFormView.as_view(), name="login"),
    path('login/', LoginFormView.as_view(), name='login'),
    path('registro/',TurneroRegisterView.as_view(), name="registro"),
    path('orden/', TurneroOrderView.as_view(), name="orden"),
    path('box1/', TurneroListBox1View.as_view(), name="box1"),
    path('<int:pk>/atendido/', TurneroCheckView.as_view(), name="atendido"),
    path('<int:pk>/update/', TurneroUpdateView.as_view(), name="editar"),
    path('<int:pk>/delete/', TurneroDeleteView.as_view(), name="eliminar"),
     path('cliente/<int:pk>/check/', TurneroCheckView.as_view(), name='cliente_check')
    
]




