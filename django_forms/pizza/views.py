from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request,'pizza/home.html')
def order(request):
    if request.method == "POST":
        topping1 = request.POST.get("topping1")
        topping2 = request.POST.get("topping2")
        size = request.POST.get("size")

        print(topping1, topping2, size)

    return render(request, 'pizza/order.html')
