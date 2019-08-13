from django.urls import path
from . import views

urlpatterns = [
    path('all', views.AuthList.as_view()),
    path('<pk>', views.AuthDetail.as_view()),
]
