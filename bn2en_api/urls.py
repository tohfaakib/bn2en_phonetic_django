from django.urls import path
from .views import Bn2EnView

urlpatterns = [
    path('bn2en/', Bn2EnView.as_view({'post': 'list'})),
]
