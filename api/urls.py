from django.urls import path 
from rest_framework import routers

from api.views import TermViewset, ProductViewset

router = routers.SimpleRouter()
router.register(r'terms', TermViewset)
router.register(r'products', ProductViewset)
urlpatterns = router.urls

urlpatterns += router.urls
