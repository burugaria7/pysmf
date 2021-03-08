from django.urls import path
from . import views

app_name = 'makesmf'

urlpatterns = [
    path('', views.hello, name='hello'),
    # path('func1/', views.func1, name='func1'),
    # path('func2/', views.func2, name='func2'),
]