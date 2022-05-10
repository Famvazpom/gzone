from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *


#Error 403 - Forbidden
def handler404(request,exception):
    return render(request, 'blog/page-404.html',status=404)

def handler403(request,exception):
    return render(request, 'blog/page-403.html',status=403)

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

class LandingView(TemplateView):
    template_name = 'landing.html'

class HomeView(TemplateView):
    template_name = "blog/page-blank.html"

class PostListView(ListView):
    paginate_by = 9
    template_name = "blog/post-list.html"
    model = Post
    queryset = Post.objects.order_by('-fecha')

class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model= Post

class PostUpdateView(UpdateView):
    template_name = "blog/post-create.html"
    model = Post
    form_class = PostUpdateForm

class PostCreateView(CreateView):
    template_name = "blog/post-create.html"
    model = Post
    form_class = PostForm

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class PerfilUpdateView(TemplateView):
    template_name = "perfil.html"

    def get(self,request,*args, **kwargs):
        context = self.get_context_data()
        context['form_perfil'] = PerfilForm(instance = self.request.user.perfil)
        context['form_usuario'] = UsuarioForm(instance = self.request.user)
        return render(request,self.template_name,context)

    def post(self,request,*args, **kwargs):
        context = self.get_context_data()
        form_perfil = PerfilForm(request.POST,request.FILES,instance = self.request.user.perfil)
        form_usuario = UsuarioForm(request.POST,instance = self.request.user)
        if form_perfil.is_valid() and form_usuario.is_valid():
            form_perfil.save()
            form_usuario.save()
        context['form_perfil'] = form_perfil
        context['form_usuario'] = form_usuario
        return render(request,self.template_name,context)

