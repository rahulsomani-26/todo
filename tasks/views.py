from django.shortcuts import render

# Create your views here.
def homeless(request):
    return render(request,'home.html',{'title':'Tasks'})