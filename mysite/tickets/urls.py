from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeEvents.as_view(), name='home'),
    path('events/<int:pk>/', CreateTicket.as_view(), name='reserve_ticket'),
    path('about/', about, name='about'),
    path('success/', success, name='success'),
    # path('test_email/', test_email, name='test_email')
]
