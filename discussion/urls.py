from django.urls import path, include
from rest_framework.routers import DefaultRouter

from discussion import views
from discussion.views import HotPotatoViewSet

app_name = "discussion"

router = DefaultRouter()
router.register("hotpotatos", HotPotatoViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("hotpotatos.json/", views.hotpotato_list),
]
