from rest_framework import routers
from django.urls import include,path
from .views import ProjectViewSet,ClientLocationViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('project', ProjectViewSet) 
router.register('client',ClientLocationViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]