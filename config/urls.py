from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('aidialer/', include('aidialer.urls'))
    # path('api/dialer/', include('aidialer.urls')),
]

urlpatterns += staticfiles_urlpatterns()
