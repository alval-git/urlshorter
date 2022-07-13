from django.shortcuts import render,redirect
from .models import ShortUrl
from .utils import generateShortUrl
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.
@login_required()
def CreateShortUrlView(request):
        template_name = 'gen_short_url.html'
        user = request.user
        if (request.method=="POST"):
            data = request.POST
            if (data['long_url'].startswith('http://') | data['long_url'].startswith('https://')):

                if (ShortUrl.objects.filter(long_url=data['long_url']).first()):
                    request.session["gen_url"] = "Для этого адреса уже был сгенерирован короткий url"
                    return render(request, template_name, {"message": request.session["gen_url"]})

                slug = generateShortUrl()
                gen_url = "https://urlshort10.herokuapp.com/" + slug
                request.session["gen_url"] = gen_url
                ShortUrl.objects.create(long_url=data['long_url'], short_url=gen_url, user=user, slug=slug)
                return render(request, template_name, {"gen_url": request.session["gen_url"]})
            else:
                request.session["gen_url"] = "Не корректно введен адрес страницы"
                return render(request, template_name, {"message": request.session["gen_url"]})
        else:
            return render(request, template_name)



class RedirectDetail(DetailView):
    template_name = 'redirect.html'
    model = ShortUrl
    def dispatch(self, request, *args, **kwargs):
        current_path = request.path.replace('/', '')
        redirect_url = get_object_or_404(ShortUrl, slug=current_path).long_url
        return redirect(redirect_url)


class UserUrlsList(ListView):
    model = ShortUrl
    template_name = 'user_url_list.html'

    def get_queryset(self):
        user = self.request.user
        user_urls = ShortUrl.objects.filter(user=user).all()
        return user_urls

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
