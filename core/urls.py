from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.work_list, name='work_list'),
    path('works/<int:work_id>/',views.work_detail,name='work_detail'),
    path('characters/', views.character_list, name='character_list'),
    path('characters/<int:character_id>/', views.character_detail, name='character_detail'),
    path('characters/search/', views.character_search, name='character_search'),
    path('routes/', views.route_list, name='route_list'),
    path('routes/<int:route_id>/', views.route_detail, name='route_detail'),
    path('diagnosis/',views.diagnosis,name='diagnosis'),
]