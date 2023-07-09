from django.views.generic import View
from django.shortcuts import render
from turnero.forms import LoginForm

class HomeView(View):
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
                return redirect('registro')
        else:
            form = LoginForm(request)

        return render(request, 'login.html', {'form': form})

