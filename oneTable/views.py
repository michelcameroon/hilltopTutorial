from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


#from django.views.generic import (ListView, DetailView, TemplateView, CreateView)








from django.views.generic import (TemplateView, ListView)








#from .forms import AuthorForm, BookForm
from .models import OneTable




#from .views import IndexView, oneTableListView

# urls.py
#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^welcome/', WelcomeView.as_view()),
#    url(r'^list/', oneTableListView.as_view()),




#class IndexView(TemplateView):
#    template_name = 'index.html'


#class AuthorCreateView(CreateView):
#    model = Author
#    template_name = 'my-author-create.html'
#    form_class = AuthorForm
#    success_url = '/my-books'



class OneTableListView(ListView):
    model = OneTable
#    template_name = 'oneTableList.html'
    template_name = 'onetable_list.html'


