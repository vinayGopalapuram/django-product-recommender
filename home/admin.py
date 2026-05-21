from django.contrib import admin
from .models import Product

# Admin class for Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'p_category', 'p_price', )  # Fields to display in the list
    search_fields = ('p_name', 'p_category')  # Fields to search in the admin
    list_filter = ('p_category', )  # Fields to filter by in the admin


# Register the models and their respective admin classes
admin.site.register(Product, ProductAdmin)

