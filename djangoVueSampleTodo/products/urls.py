from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductDummyApiView, product_list, product_detail

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path("dummy/", ProductDummyApiView.as_view()),
    
    path('list/', product_list),

    path('list/<int:pk>', product_detail),
]