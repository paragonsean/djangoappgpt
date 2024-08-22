from . import views
from django.urls import path


app_name = "aidialer"

urlpatterns = [
    path(
        '',
        views.ai_dialer_view,
        name='ai_dialer_view'
    ),

    path(
        'call/<str:call_sid>/',
        views.call_contact,
        name='call_contact'
    )
    
]