from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda', views.about, name='hakkimizda'),
    path('iletisim', views.contact_us, name='iletisim'),
]
