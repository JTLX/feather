from django.conf.urls import url, include
from rest_framework.authtoken import views as drf_views
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
   url(r'^', include(router.urls)),
   url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
]
