from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class TestPage(TemplateView):
    template_name = 'test.html'


def band(request):
    test = 'Band Page working'
    content = {
        "test": test,
    }
    return render(request, 'band.html', content)


def single(request, id):
    test = 'Single Band Page working'
    content = {
        "test": test,
    }
    return render(request, 'single.html', content)
