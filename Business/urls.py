from django.conf.urls import url
from Business import views

urlpatterns = [
    url(r'plans/', views.get_plans),
]