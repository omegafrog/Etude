from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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
def detail(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id);
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)