from django.shortcuts import render
from .models import Sorry
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import SorryForm
from django.shortcuts import redirect
from django.views import View
# Create your views here.

def sorry_list(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.all().order_by('-id')
    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys})

def sorry_detail(request, pk):
    sorry = get_object_or_404(Sorry, pk=pk)
    return render(request, 'sorry/sorry_detail.html', {'sorry':sorry})

def sorry_new(request):

    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()
    return render(request, 'sorry/sorry_edit.html', {'form':form})


def mainView(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.all().order_by('-id')
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()
    # return render(request, 'sorry/sorry_edit.html', {'form':form})
    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys, 'form':form})
