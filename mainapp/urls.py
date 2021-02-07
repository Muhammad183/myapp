from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('inner_page/', views.inner_page, name='inner_page'),
    path("buy/", views.buy_new, name="buy"),
    path("about/", views.about, name="about"),
]
