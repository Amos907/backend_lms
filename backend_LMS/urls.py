
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-loans/', include('loans.urls')),
    path('payments/',include('mpesa_payments.urls')),
    path('api/', include(('core.routers', 'core'), namespace='core-api')),
]