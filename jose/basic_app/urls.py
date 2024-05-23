from django.urls import path
from basic_app import views


app_name = "basic_app"   

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path("artists/artist1/", views.ArtistOne.as_view(), name='artistone'),
    path("artists/artist2/", views.ArtistTwo.as_view(), name='artisttwo'),
    path("managers/manager1/", views.ManagerOne.as_view(), name='managerone'),
    path("managers/manager2/", views.ManagerTwo.as_view(), name='managertwo'),
    path("about/", views.About.as_view(), name='about'),
    path("Faq/", views.FAQ.as_view(), name='faq'),
    path("legal/", views.Legal.as_view(), name='legal'),
    path("contact/", views.contact_form, name='contact'),
    path("contact-success/", views.ContactSuccess.as_view(), name='contact-success'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)