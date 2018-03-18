from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Band
# Create your views here.


class TestPage(TemplateView):
    template_name = 'test.html'


def band(request):
    test = 'Band Page working'
    bands = Band.objects.all()
    content = {
        "test": test,
        "bands": bands,
    }
    return render(request, 'band.html', content)


def single(request, id):
    band = Band.objects.get(pk=id)
    test = 'Single Band Page working'
    content = {
        "test": test,
        "band": band,
    }
    return render(request, 'single.html', content)
