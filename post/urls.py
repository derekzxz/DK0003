from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category, name="category"),
    url(r'^post/(?P<post_slug>[-\w]+)/$', views.detail, name="detail"),
]