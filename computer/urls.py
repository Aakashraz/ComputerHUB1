from django.urls import path
from . import views

app_name="chub"

urlpatterns = [
    # path('',views.IndexView.as_view(), name='index'),

    # path('brand_create-form/', views.CompBrandCreateView.as_view(), name= 'brand-create-form'),
    path('brand_create-form/', views.ComputerBrandView.as_view(), name= 'brand-create-form'),       #using only View class

    # path('generation_create-form/', views.CompGenerationCreateView.as_view(), name= 'gen-create-form'),
    path('generation_create-form/', views.ComputerGenerationView.as_view(), name= 'gen-create-form'),   #using only View class

    path('create-form/', views.ComputerCreateView.as_view(), name= 'create-form'),

    # path('brand-list',views.CompBrandListView.as_view(), name='brand-list'),
    path('brand-list',views.ComputerBrandPageView.as_view(), name='brand-list'),        #using only View class

    # path('gen-list/', views.CompGenListView.as_view(), name= 'genlist'),
    path('gen-list/', views.ComputerGenerationPageView.as_view(), name= 'genlist'),     #using only View class

    path('', views.ComputerListView.as_view(), name= 'index'),

    # path('brand-update/<int:pk>',views.CompBrandUpdateView.as_view(), name='brand-update'),
    path('brand-update/<int:pk>',views.ComputerBrandUpdateView.as_view(), name='brand-update'),     #using only View class

    # path('gen-update/<int:pk>',views.CompGenUpdateView.as_view(), name='gen-update'),
    path('gen-update/<int:pk>',views.ComputerGenerationUpdateView.as_view(), name='gen-update'),    #using only View class

    path('update/<int:pk>', views.ComputerUpdateView.as_view(), name= 'update'),

    # path('brand-delete/<int:pk>', views.CompBrandDeleteView.as_view(), name='brand-delete'),
    path('delete/<int:pk>', views.ComputerBrandDeleteView.as_view(), name= 'brand-delete'),     #using only View class

    # path('gen-delete/<int:pk>', views.CompGenDeleteView.as_view(), name='gen-delete'),
    path('gen-delete/<int:pk>', views.ComputerGenerationDeleteView.as_view(), name='gen-delete'),   #using only View class


    path('delete/<int:pk>', views.ComputerDeleteView.as_view(), name= 'delete'),

]