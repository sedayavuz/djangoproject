from django.shortcuts import render


# Create your views here.

from django.shortcuts import render
from .executivemodels import Executive
from django.http import HttpResponse,HttpResponseRedirect

from .models import Post
from .mmodels import Messages
from .forms import MForm



def management_view(request):
    return render(request, 'yonetim.html', {'yoneticiler': Executive.objects.all()})
def loadPosts(request):
    return render(request, 'root.html', {'posts': Post.objects.all()})
def AboutUs(request):
    return render(request, 'mainpage.html', {})


def post_new(request):
    if request.method == "POST":
        form = MForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            tel = request.POST["tel"]
            mail = request.POST["mail"]
            message = request.POST["message"]
            m = Messages(name=name,tel=tel,mail=mail,message=message)
            m.save()
            print name,tel
            return HttpResponseRedirect("/")
    else:
        form = MForm()
    return render(request, 'contact.html', {'form': form})
