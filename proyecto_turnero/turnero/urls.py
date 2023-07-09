from django.urls import path
from .views import TurneroListView, TurneroRegisterView, TurneroOrderView, LoginFormView

app_name="turnero"

urlpatterns = [
    
    path('',TurneroListView.as_view(), name="home"),
    path('registro/',TurneroRegisterView.as_view(), name="registro"),
    path('<int:pk/', TurneroOrderView.as_view(), name="orden"),
    path('login/', LoginFormView.as_view(), name='login')
]

