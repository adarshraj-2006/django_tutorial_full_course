from django.shortcuts import render
from .forms import PizzaForm

# from django.http import HttpResponse

def home(request):
    return render(request,'pizza/home.html')
def order(request):
    if (request.method == 'POST'):
        filled_form =PizzaForm(request.POST, request.FILES)
        if filled_form.is_valid():
            note= 'Thanks for ordering ! you %s %s amd %s pizza on way' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'])

            return render(request, 'pizza/order.html', {
                'note': note,
                'pizzaform': filled_form
            })
    
    else:
        form =PizzaForm()

        return render(request, 'pizza/order.html',{'pizzaform':form})
