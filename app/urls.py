from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.MerchList.as_view()),
    # url(r'^api-auth/', ('rest_framework.urls', namespace='rest_framework'))url(r'^$', 'home'),
    
]