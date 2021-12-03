from django.urls import path
from . import views

app_name = "apiapp"

urlpatterns = [
    path('list_items', views.ListItemAPIView.as_view()),
    path('create_order/', views.CreateOrderOnCheckoutAPIView.as_view())
]