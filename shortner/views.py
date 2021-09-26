from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from .models import Url

# Create your views here.
def index(request):
    if request.method=="POST":
        url = request.POST['url']
        
        if url[:8]!="https://":
            print(url[:6])
            url = "https://"+url
        
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url,uuid=uid)
        new_url.save()

        return redirect('go/'+uid)

    return render(request, 'index.html')


def go(request, pk):
    # return HttpResponse("hello")

    url_details = Url.objects.get(uuid=pk)
    context = {
        'link':url_details.link,
        'uid':url_details.uuid,
    }

    return render(request,'short.html',context)

def tothelink(request,link):
    url_details = Url.objects.get(uuid=link)

    return redirect(url_details.link)


