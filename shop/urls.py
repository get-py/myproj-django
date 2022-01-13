from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import review_new, review_list, ReviewViewSet


app_name = "shop"

router = DefaultRouter()
router.register("reviews", ReviewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("reviews/", review_list, name="review_list"),
    path("reviews/new/", review_new, name="review_new")
]
