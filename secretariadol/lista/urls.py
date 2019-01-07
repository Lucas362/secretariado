from django.conf.urls import url, include
from rest_framework import routers
from lista.cadastro import views
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'person', views.PersonViewSet)

schema_view = get_swagger_view(title='Pastebin API')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^root/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', schema_view),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
    url(r'^login', views.login),
    # path('auth/login/', views.LoginView.as_view(), name="auth-login")
]