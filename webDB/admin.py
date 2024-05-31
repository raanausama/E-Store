from django.contrib import admin

# Register your models here.

from .models import Product, Category, Brand, Cart, UserProfile, Coupon, Payment,ProductDetail, ProductVariant, Promotion, Material, Review, Order,OrderProduct, OrderPromotion, Address, Wishlist, Size, Color, Style,PaymentMethod,ShippingAddress,Checkout, Dashboard  # Import other models as needed


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(Coupon)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(ProductDetail)
admin.site.register(ProductVariant)
admin.site.register(Promotion)
admin.site.register(Material)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Address)
admin.site.register(OrderPromotion)
admin.site.register(Wishlist)
admin.site.register(Style)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(PaymentMethod)
admin.site.register(ShippingAddress)
admin.site.register(Checkout)
admin.site.register(Dashboard)
