from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import ClienteRegisterForm, LoginForm
from .models import Cliente




class TurneroListView(View):
    def get(self,request, *args, **kwargs):
        posts = Cliente.objects.all()
        context={
            'posts' : posts
        }
        return render(request, 'turnero_list.html', context)
    
class LoginFormView(View):
    def get(self,request, *args, **kwarg):
        form = LoginForm()
        context={
            'form':form
        }
        return render(request, 'login.html', context)
    
    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar al usuario
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # Iniciar sesión
                login(request, user)
                return redirect('registro')  # Redirigir a la página de inicio después del inicio de sesión
        else:
            form = LoginForm(request)

        return render(request, 'login.html', {'form': form})



class TurneroRegisterView(View):
    def get(self,request, *args, **kwargs):
        form=ClienteRegisterForm()
        context={
            'form':form
        }
        return render(request, 'turnero_register.html', context)
    
    def post(self,request, *args, **kwargs):
        if request.method=="POST":
            form = ClienteRegisterForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get('nombre')
                cedula_ruc = form.cleaned_data.get('cedula_ruc')
                prioridad = form.cleaned_data.get('prioridad')
                servicios = form.cleaned_data.get('servicios')

                p, created = Cliente.objects.get_or_create(nombre=nombre, cedula_ruc=cedula_ruc, prioridad= prioridad, servicios=servicios)
                p.save()
                return redirect('turnero:registro')


        context={

        }
        return render(request, 'turnero_register.html', context)
    
class TurneroOrderView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Cliente,pk=pk)
        context={
            'post':post
        }
        return render(request, 'turnero_order.html', context)
    





