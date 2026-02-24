from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.deposit_form, name='deposit_form'),
    path('deposit/', views.deposit_form, name='deposit_form'),
    path('receipt/<str:ref>/', views.transaction_receipt, name='transaction_receipt'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    
    # Add this line for logout
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
