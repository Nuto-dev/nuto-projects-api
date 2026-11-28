from django.urls import path, include

urlpatterns = [
    path('spaces/v1/', include('workspace.space.urls')),
    path('spaces/relations/v1/', include('workspace.relations.urls')),
]