from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('serwis/', views.SerwisIndexView.as_view(), name='serwis-index'),
    path('serwis/add/', views.SerwisCreate.as_view(), name='serwis-create'),
    path('serwis/<int:pk>/del/', views.SerwisDelete.as_view(), name='serwis-delete'),
    path('serwis/<int:pk>/update/', views.SerwisUpdate.as_view(), name='serwis-update'),
]
