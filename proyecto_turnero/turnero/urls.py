from django.urls import path
from .views import LoginFormView, TurneroRegisterView, TurneroOrderView, TurneroListBox1View, TurneroListBox2View, TurneroListBox3View, TurneroCheckView1, TurneroUpdateView1, TurneroDeleteView1, TurneroCheckView2, TurneroUpdateView2, TurneroDeleteView2, TurneroCheckView2, TurneroCheckView3, TurneroUpdateView3, TurneroDeleteView3

app_name="turnero"

urlpatterns = [
    
    path('',LoginFormView.as_view(), name="login"),
    path('login/', LoginFormView.as_view(), name='login'),
    path('registro/',TurneroRegisterView.as_view(), name="registro"),
    path('orden/', TurneroOrderView.as_view(), name="orden"),
    path('box1/', TurneroListBox1View.as_view(), name="box1"),
    path('box2/', TurneroListBox2View.as_view(), name="box2"),
    path('box3/', TurneroListBox3View.as_view(), name="box3"),

    path('<int:pk>/box1/atendido/', TurneroCheckView1.as_view(), name="atendidobox1"),
    path('<int:pk>/box1/update/', TurneroUpdateView1.as_view(), name="editarbox1"),
    path('<int:pk>/box1/delete/', TurneroDeleteView1.as_view(), name="eliminarbox1"),

    path('<int:pk>/box2/atendido/', TurneroCheckView2.as_view(), name="atendidobox2"),
    path('<int:pk>/box2/update/', TurneroUpdateView2.as_view(), name="editarbox2"),
    path('<int:pk>/box2/delete/', TurneroDeleteView2.as_view(), name="eliminarbox2"),

    path('<int:pk>/box3/atendido/', TurneroCheckView3.as_view(), name="atendidobox3"),
    path('<int:pk>/box3/update/', TurneroUpdateView3.as_view(), name="editarbox3"),
    path('<int:pk>/box3/delete/', TurneroDeleteView3.as_view(), name="eliminarbox3")

]




