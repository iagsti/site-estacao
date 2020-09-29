from django.shortcuts import render


def museu_index(request):
    return render(request, 'museu.html')
