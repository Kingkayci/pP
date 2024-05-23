from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactUsForm

# Create your views here.


def contact_form(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basic_app:contact-success')
    else:
        form = ContactUsForm()
    return render(request, template_name='contact-us.html', context={'contact':form})


class HomePage(TemplateView):
    template_name = 'index.html'

class ArtistOne(TemplateView):
    template_name = 'artists/artists1.html'

class ArtistTwo(TemplateView):
    template_name = 'artists/artists2.html'

class About(TemplateView):
    template_name = 'about.html'

class ManagerOne(TemplateView):
    template_name = 'managers/manager1.html'

class ManagerTwo(TemplateView):
    template_name = 'managers/manager2.html'

class FAQ(TemplateView):
    template_name = 'faq.html'

class Legal(TemplateView):
    template_name = 'legal.html'

class ContactSuccess(TemplateView):
    template_name = 'contact-success.html'