from rest_framework.viewsets import ModelViewSet

from api.serializers import TermsSerializer, ProductSerializer
from api.models import Product, Terms

class TermViewset(ModelViewSet):
    serializer_class = TermsSerializer
    queryset = Terms.objects.all()

class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()