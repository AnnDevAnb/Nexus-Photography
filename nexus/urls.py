from django.contrib import admin
from .views import home_view,service_view,gallery_view,contact_view
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_view),
    path("service/",service_view),
    path("gallery/",gallery_view),
    path('contact/',contact_view),
    path('enquiry/',contact_view, name='enquiry'),
]