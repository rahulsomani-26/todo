from django.shortcuts import render


def todo(request):
    return render(request,'index.html',{'title':'ToDo'})