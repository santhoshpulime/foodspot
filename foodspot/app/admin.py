from django.contrib import admin
from .models import order_code_for_user,item_details,restaurant_details,user_detail,restaurants_category,bookeditem
admin.site.register(restaurant_details)
admin.site.register(user_detail)
admin.site.register(restaurants_category)
admin.site.register(item_details)
admin.site.register(bookeditem)
admin.site.register(order_code_for_user)