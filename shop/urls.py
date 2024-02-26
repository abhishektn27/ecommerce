from django.urls import path,include

from shop import views

urlpatterns = [
    path('', views.allproducts,name='allproducts'),
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin,name='signin'),
    path('signout/', views.signout,name='signout'),
    path('<slug:slug_cat>/', views.allproducts,name='product_by_category'),
    path('<slug:slug_cat>/<slug_prod>/', views.cat_prod, name='product_details'),

]