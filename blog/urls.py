from django.conf.urls import url
from blog import views_api

urlpatterns = [
    url(r'^get_category_list/', views_api.get_category_list, name='get_category_list'),
    url(r'add_category/', views_api.add_category, name='add_category'),
]
