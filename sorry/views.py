from django.shortcuts import render
from .models import Sorry
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import SorryForm
from django.shortcuts import redirect
from django.views import View
import operator
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

def sorry_detail(request, pk):
    sorry = get_object_or_404(Sorry, pk=pk)
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()
    return render(request, 'sorry/sorry_detail.html', {'sorry':sorry, 'form':form})

# Filter relationship






def sorry_filter_ex(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.filter(relationship='Ex-Lover').order_by('-id')
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()

    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys, 'form':form})

def sorry_filter_fa(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.filter(relationship='Family').order_by('-id')
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()

    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys, 'form':form})

def sorry_filter_so(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.filter(relationship='Lover').order_by('-id')
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()

    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys, 'form':form})
def sorry_filter_fr(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.filter(relationship='Friend').order_by('-id')
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()

    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys, 'form':form})

def sorry_filter_en(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.filter(relationship='Enemy').order_by('-id')
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()

    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys, 'form':form})

def sorry_filter_co(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.filter(relationship='Co-Worker').order_by('-id')
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()

    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys, 'form':form})

def sorry_filter_st(request):
    # sorrys = Sorry.objects.get(published_date__lte=timezone.now()).order_by('published_date')
    sorrys = Sorry.objects.filter(relationship='Stranger').order_by('-id')
    if request.method == "POST":
        form = SorryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sorry_list')
    else:
        form =SorryForm()

    return render(request, 'sorry/sorry_list.html', {'sorrys': sorrys, 'form':form})


# def sorry_Filter(self, request, *args, **kwargs):
#     # Here you list all your filter names
#     filter_names = ('Ex-Lover', 'Family', 'Significant Other', 'Friend', 'Enemy', 'Co-Worker', 'Stranger' )
#
#
#     queryset = Sorry.objects.all();
#     filter_clauses = [Q(filter=request.GET[filter])
#                       for filter in filter_names
#                       if request.GET.get(filter)]
#     if filter_clauses:
#         queryset = queryset.filter(reduce(operator.and_, filter_clauses))
