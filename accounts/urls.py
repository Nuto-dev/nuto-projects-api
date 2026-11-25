from django.urls import path, include

urlpatterns = [
    path('users/v1/', include('accounts.users.urls')),
]