from django.urls import path
from . import views

app_name = 'materials'
urlpatterns = [
    path('', views.materials_home, name='materials_home'),
    path('add/', views.CreateMaterialView.as_view(), name='material_add'),
    path('<int:pk>/edit/', views.UpdateMaterialView.as_view(), name='material_edit'),
    path('<int:pk>/delete/', views.DeleteMaterialView.as_view(), name='material_delete'),
]
