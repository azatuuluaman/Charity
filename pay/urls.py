from django.contrib import admin
from django.urls import path, include
from .views import TransactionView
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('transaction', Transaction)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('transaction/', TransactionView.as_view()),
]

