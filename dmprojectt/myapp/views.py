from django.http import HttpResponse
from django.shortcuts import render
from.models import Place,team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
# def subtraction(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
# def multiplication(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
# def division(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})

