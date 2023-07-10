from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import ClienteRegisterForm, LoginForm
from .models import Cliente
from django.contrib.auth import authenticate, login
from django.http import HttpResponse



class LoginFormView(View):
    def get(self,request, *args, **kwargs):
        form = LoginForm()
        context={
            'form':form
        }
        return render(request, 'login.html', context)
    
    def post(self,request, *args, **kwargs):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar al usuario
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # Iniciar sesión
                login(request, user)
                return redirect('turnero:registro')
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
            'form': form
        }
        return render(request, 'turnero_register.html', context)
    
    



#class TurneroOrderView(View):
 #   def get(self, request, pk, *args, **kwargs):
  #      post = get_object_or_404(Cliente,pk=pk)
   #     context={
    #        'post':post
     #   }
      #  return render(request, 'turnero_order.html', context)

class TurneroOrderView(View):
    def get(self, request):
        clientes_box1 = Cliente.objects.filter(servicios=1, atendido=False).order_by('prioridad', 'turno')[:7]
        clientes_box2 = Cliente.objects.filter(servicios=2, atendido=False).order_by('prioridad', 'turno')[:7]
        clientes_box3 = Cliente.objects.filter(servicios=3, atendido=False).order_by('prioridad', 'turno')[:7]

        context = {
            'clientes_box1': clientes_box1,
            'clientes_box2': clientes_box2,
            'clientes_box3': clientes_box3
}
        return render(request, 'turnero_order.html', context)



class TurneroListBox1View(View):
    def get(self,request, *args, **kwargs):
        clientes_box1 = Cliente.objects.filter(servicios=1, atendido=False).order_by('prioridad', 'turno')
        clientes_box2 = Cliente.objects.filter(servicios=2, atendido=False).order_by('prioridad', 'turno')
        clientes_box3 = Cliente.objects.filter(servicios=3, atendido=False).order_by('prioridad', 'turno')

        context = {
            'clientes_box1': clientes_box1,
            'clientes_box2': clientes_box2,
            'clientes_box3': clientes_box3
}
        return render(request, 'turnero_listbox1.html', context)
    
    def post(self,request, *args, **kwargs):
        cliente_id = request.POST.get('cliente_id')
        cliente = Cliente.objects.get(atendido=cliente_id)
        cliente.atendido = not cliente.atendido
        cliente.save()
        return redirect('turnero:box1')
        #if request.method == "POST":
         #   form = ClienteRegisterForm(request.POST)
          #  if form.is_valid():
           #     atendido = form.cleaned_data.get('atendido')

            #    p, created = Cliente.objects.get_or_create(atendido=atendido)
             #   p.save()

              #  return redirect('turnero:box1')
            
        #context={
         #   'form': form
        #}
        #return render(request, 'turnero_listbox1.html', context)

def eliminar_cliente(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()

    return redirect ('turnero:box1')