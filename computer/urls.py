from django.urls import path
from . import views

app_name="chub"

urlpatterns = [
    # path('',views.IndexView.as_view(), name='index'),

    path('brand_create-form/', views.CompBrandCreateView.as_view(), name= 'brand-create-form'),
    path('generation_create-form/', views.CompGenerationCreateView.as_view(), name= 'gen-create-form'),
    path('create-form/', views.ComputerCreateView.as_view(), name= 'create-form'),

    path('', views.ComputerListView.as_view(), name= 'index'),
    path('gen-list/', views.CompGenListView.as_view(), name= 'genlist'),
    path('brand-list',views.CompBrandListView.as_view(), name='brand-list'),

    path('update/<int:pk>', views.ComputerUpdateView.as_view(), name= 'update'),
    path('gen-update/<int:pk>',views.CompGenUpdateView.as_view(), name='gen-update'),
    path('brand-update/<int:pk>',views.CompBrandUpdateView.as_view(), name='brand-update'),

    path('delete/<int:pk>', views.ComputerDeleteView.as_view(), name= 'delete'),
    path('gen-delete/<int:pk>', views.CompGenDeleteView.as_view(), name='gen-delete'),
    path('brand-delete/<int:pk>', views.CompBrandDeleteView.as_view(), name='brand-delete'),


]
