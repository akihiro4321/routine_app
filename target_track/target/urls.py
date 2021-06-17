from django.urls import path

from target import views

app_name = 'target'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('set-goal/', views.GoalCreateView.as_view(), name='set-goal'),

]