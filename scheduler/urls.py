from django.urls import path
from .views import TaskSchedulerView
from .views import PingView
urlpatterns = [
    path('ping', PingView.as_view()),
    path('api', TaskSchedulerView.as_view()),
]