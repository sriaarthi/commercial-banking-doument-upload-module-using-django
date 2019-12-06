from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.

# def form(request):
#     # return HttpResponse("Hello World")
#     return render(request, 'form.html', {
#     "heading": "Commercial Banking!",
#     "title": "Processing Form with DJANGO"
# })

# def upload(request):

    # if request.method == 'POST':
    #     data = request.POST['files']

    # else:
    # return render(request, 'process.html')

def index(request):
    customers = Customer.objects.all()
    return render(request, 'index.html', {'customers': customers})