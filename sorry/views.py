from django.shortcuts import render

# Create your views here.

def sorry_list(request):
    return render(request, 'sorry/sorry_list.html', {})
