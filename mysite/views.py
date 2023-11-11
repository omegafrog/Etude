from django.http import HttpResponse
from django.shortcuts import render

from mysite.models import MainContent


def index(request):

    content_list = MainContent.objects.order_by('pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)
    # Create your views here.

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')