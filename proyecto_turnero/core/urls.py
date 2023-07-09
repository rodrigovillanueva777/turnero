from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('turnero/', HomeView.as_view(), name="home"),

    path('', include('turnero.urls', namespace='turnero')),
]
