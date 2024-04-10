from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post-detail/<int:pk>', views.post_detail, name='post_detail'),
    path('politics/', views.politics, name='politics'),
    path('business/', views.business, name='business'),
    path('culture/', views.culture, name='culture'),
    path('technology/', views.technology, name='technology'),
    path('sports/', views.sports, name='sports'),
    path('education/', views.education, name='education'),
    path('search/', views.search_results, name='search_results'),
]
