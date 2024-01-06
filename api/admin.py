from django.contrib import admin

from api.models import Terms, Product

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
        fields = '__all__'
    
class TermsAdmin(admin.ModelAdmin):
    class Meta:
        model = Terms
        fields = '__all__'

admin.site.register(Product, ProductAdmin)
admin.site.register(Terms, TermsAdmin)