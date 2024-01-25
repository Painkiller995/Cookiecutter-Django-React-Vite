from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("example", ExampleViewSet)


app_name = "api"
urlpatterns = router.urls
