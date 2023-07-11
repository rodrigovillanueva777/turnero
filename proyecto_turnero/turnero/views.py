from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import ClienteRegisterForm, LoginForm
from .models import Cliente
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy



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
                atendido = form.cleaned_data.get('atendido')

                p, created = Cliente.objects.get_or_create(nombre=nombre, cedula_ruc=cedula_ruc, prioridad= prioridad, servicios=servicios, atendido=atendido)
                p.save()
                return redirect('turnero:registro')
        context={
            'form': form
        }
        return render(request, 'turnero_register.html', context)
    
    


class TurneroOrderView(View):
    def get(self, request):
        clientes_box1 = Cliente.objects.filter(servicios=1, atendido=False).order_by('prioridad', 'fecha_hora')[:7]
        clientes_box2 = Cliente.objects.filter(servicios=2, atendido=False).order_by('prioridad', 'fecha_hora')[:7]
        clientes_box3 = Cliente.objects.filter(servicios=3, atendido=False).order_by('prioridad', 'fecha_hora')[:7]

        context = {
            'clientes_box1': clientes_box1,
            'clientes_box2': clientes_box2,
            'clientes_box3': clientes_box3
}
        return render(request, 'turnero_order.html', context)



class TurneroListBox1View(View):
    def get(self,request, *args, **kwargs):
        clientes_box1 = Cliente.objects.filter(servicios=1).order_by('atendido','prioridad', 'fecha_hora')
        clientes_box2 = Cliente.objects.filter(servicios=2).order_by('atendido', 'prioridad', 'fecha_hora')
        clientes_box3 = Cliente.objects.filter(servicios=3).order_by('atendido','prioridad', 'fecha_hora')

        context = {
            'clientes_box1': clientes_box1,
            'clientes_box2': clientes_box2,
            'clientes_box3': clientes_box3
}
        return render(request, 'turnero_listbox1.html', context)
    
    def post(self,request, *args, **kwargs):
        if request.method=="POST":
            form = ClienteRegisterForm(request.POST)
            if form.is_valid():
                atendido = form.cleaned_data.get('atendido')

                p, created = Cliente.objects.get_or_create(atendido=atendido)
                p.save()
                return redirect('turnero:box1')
        context={
            'form': form
        }
        return render(request, 'turnero_listbox1.html', context)
    


class TurneroListBox2View(View):
    def get(self,request, *args, **kwargs):
        clientes_box1 = Cliente.objects.filter(servicios=1).order_by('atendido','prioridad', 'fecha_hora')
        clientes_box2 = Cliente.objects.filter(servicios=2).order_by('atendido', 'prioridad', 'fecha_hora')
        clientes_box3 = Cliente.objects.filter(servicios=3).order_by('atendido','prioridad', 'fecha_hora')

        context = {
            'clientes_box1': clientes_box1,
            'clientes_box2': clientes_box2,
            'clientes_box3': clientes_box3
}
        return render(request, 'turnero_listbox2.html', context)
    
    def post(self,request, *args, **kwargs):
        if request.method=="POST":
            form = ClienteRegisterForm(request.POST)
            if form.is_valid():
                atendido = form.cleaned_data.get('atendido')

                p, created = Cliente.objects.get_or_create(atendido=atendido)
                p.save()
                return redirect('turnero:box2')
        context={
            'form': form
        }
        return render(request, 'turnero_listbox2.html', context)


class TurneroListBox3View(View):
    def get(self,request, *args, **kwargs):
        clientes_box1 = Cliente.objects.filter(servicios=1).order_by('atendido','prioridad', 'fecha_hora')
        clientes_box2 = Cliente.objects.filter(servicios=2).order_by('atendido', 'prioridad', 'fecha_hora')
        clientes_box3 = Cliente.objects.filter(servicios=3).order_by('atendido','prioridad', 'fecha_hora')

        context = {
            'clientes_box1': clientes_box1,
            'clientes_box2': clientes_box2,
            'clientes_box3': clientes_box3
}
        return render(request, 'turnero_listbox3.html', context)
    
    def post(self,request, *args, **kwargs):
        if request.method=="POST":
            form = ClienteRegisterForm(request.POST)
            if form.is_valid():
                atendido = form.cleaned_data.get('atendido')

                p, created = Cliente.objects.get_or_create(atendido=atendido)
                p.save()
                return redirect('turnero:box3')
        context={
            'form': form
        }
        return render(request, 'turnero_listbox3.html', context)




class TurneroCheckView1(UpdateView):
    model = Cliente
    fields = ['atendido']
    template_name = 'turnero_check.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('turnero:box1')
    
class TurneroUpdateView1(UpdateView):
    model = Cliente
    fields = ['nombre', 'cedula_ruc','prioridad','servicios']
    template_name = 'turnero_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('turnero:box1')
    
class TurneroDeleteView1(DeleteView):
    model=Cliente
    template_name='turnero_delete.html'
    success_url= reverse_lazy('turnero:box1')




class TurneroCheckView2(UpdateView):
    model = Cliente
    fields = ['atendido']
    template_name = 'turnero_check.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('turnero:box2')
    
class TurneroUpdateView2(UpdateView):
    model = Cliente
    fields = ['nombre', 'cedula_ruc','prioridad','servicios']
    template_name = 'turnero_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('turnero:box2')
    
class TurneroDeleteView2(DeleteView):
    model=Cliente
    template_name='turnero_delete.html'
    success_url= reverse_lazy('turnero:box2')




class TurneroCheckView3(UpdateView):
    model = Cliente
    fields = ['atendido']
    template_name = 'turnero_check.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('turnero:box3')
    
class TurneroUpdateView3(UpdateView):
    model = Cliente
    fields = ['nombre', 'cedula_ruc','prioridad','servicios']
    template_name = 'turnero_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('turnero:box3')
    
class TurneroDeleteView3(DeleteView):
    model=Cliente
    template_name='turnero_delete.html'
    success_url= reverse_lazy('turnero:box3')