from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'subbu','age':23}

    return render(request,'forloop.html',context=d)

def navigation(request):

    return render(request,'navigation.html')