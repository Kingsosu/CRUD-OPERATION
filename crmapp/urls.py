from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('register', v.register, name='register'),
    path('my_login', v.my_login, name='my_login'),   
    path('user_logout', v.user_logout, name='user_logout'),
    
    # CRUD
    path('dashboard', v.dashboard, name='dashboard'),
    path('create_record', v.create_record, name='create_record'),
    path('update_record/<int:pk>', v.update_record, name='update_record'),
    path('record/<int:pk>', v.signular_record, name='record'),
    path('delete_record/<int:pk>/', v.delete_record, name='delete_record')
]
