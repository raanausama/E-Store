# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Category, Brand, Cart, UserProfile, Coupon, Payment,ProductDetail, ProductVariant, Promotion, Material, Review, Order,OrderProduct, OrderPromotion, Address, Wishlist, Size, Color, Style,PaymentMethod,ShippingAddress,Checkout, Dashboard , Customer

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class User_Profile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['shipping_address', 'phone_number', 'date_of_birth', 'gender']

class Pro_ducts(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    

class Br_and(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'



class Cat_gory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']

class Product_variant(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['product','size','color','quantity']

class Ma_terial(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description']

class Product_detail(forms.ModelForm):
    class Meta:
        model = ProductDetail
        fields = ['product','material','dimensions','weight']

class Re_view(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class CART(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

class Or_der(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class Order_product(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = '__all__'

class add_ress(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class paymentform(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class Whishlistform(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = '__all__'

class Couponform(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'

class promoform(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = '__all__'


class orderpromoform(forms.ModelForm):
    class Meta:
        model = OrderPromotion
        fields = '__all__'


class sizeform(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'


class colorform(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'


class styleform(forms.ModelForm):
    class Meta:
        model = Style
        fields = '__all__'

class paymentmethodform(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class shippingaddressform(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class checkoutform(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'

class dashboardform(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'

class customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


