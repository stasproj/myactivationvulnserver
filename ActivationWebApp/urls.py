from django.urls import path
from . import views
urlpatterns = [path('', views.KeyPanel),
               path('iskeyvalid/', views.iskeyvalid)]
