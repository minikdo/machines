from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('serwis/', views.SerwisIndexView.as_view(), name='serwis-index'),
    path('serwis/add/', views.SerwisCreate.as_view(), name='serwis-create'),
    path('serwis/<int:pk>/del/', views.SerwisDelete.as_view(), name='serwis-delete'),
    path('serwis/<int:pk>/update/', views.SerwisUpdate.as_view(), name='serwis-update'),
    path('sprzety/', views.SprzetIndexView.as_view(), name='sprzet-index'),
    path('sprzety/<int:pk>/', views.SprzetDetailView.as_view(), name='sprzet-detail'),
    path('sprzety/add/', views.SprzetCreate.as_view(), name='sprzet-create'),
    path('sprzety/<int:pk>/del/', views.SprzetDelete.as_view(), name='sprzet-delete'),
    path('sprzety/<int:pk>/update/', views.SprzetUpdate.as_view(), name='sprzet-update'),
    path('kompysprzet/add/', views.KompySprzetCreate.as_view(), name='kompysprzet-create'),
]
