from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    #return HttpResponse("<h1>hello world</h1>")
    return render(request, 'home.html',{'name':'suraj pawar'})
def index(request):
    return HttpResponse('''<h1>“Success makes life easier. It doesn't make living easier.” <b>by Suraj Sanjeev Pawar</b></h1>''')
    #return render(request, 'home.html',{'name':'suraj pawar'})
def about(request):
    return HttpResponse("<h1>About Harry Bhai<h1>")
def index1(request):
    #return render(request, 'index1.html')
    return render(request, 'index1.html',{'name':'suraj pawar'})