
# Create your views here.
# views.py

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import csv
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen import canvas

from django.shortcuts import render, redirect,redirect,get_object_or_404
from .forms import UserRegistrationForm, UserLoginForm
from .forms import User_Profile, Pro_ducts, Br_and, Cat_gory, Ma_terial, Product_variant, Re_view, Product_detail, CART, Or_der, add_ress, Order_product, paymentform, Whishlistform, Couponform,promoform, orderpromoform, sizeform, styleform,colorform,paymentmethodform, shippingaddressform, checkoutform, dashboardform,customerform
from .models import UserProfile, Product, Brand, Category,ProductVariant,Material,PaymentMethod,ProductDetail,Payment,Review,Cart,Checkout,Color,Coupon,Dashboard,ShippingAddress,Size,Style,Address,Customer
from django.core.paginator import Paginator

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                # Handle invalid login
                pass
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def UserProfileview(request):
    success = False
    if request.method == 'POST':
        form= User_Profile(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= User_Profile()
            data=UserProfile.objects.all()
    else:
        form= User_Profile()
        data=UserProfile.objects.all()
    return render (request, 'userprofile.html', {'form': form, 'data': data, 'success': success})

def delete_view1(request,id):
    instance = get_object_or_404(UserProfile, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('profile')
    else:
        form = User_Profile(instance=instance)
    return render (request, 'delete1.html', {'form': form})
 
def update_view1(request,id):
    instance = get_object_or_404(UserProfile, id=id)
    if request.method == 'POST':
        form = User_Profile(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = User_Profile(instance=instance)
    return render (request, 'update1.html', {'form': form})
    # form = User_Profile()
    # return render (request, 'userprofile.html', {"form": form})

def Products(request):
    success = False
    if request.method == 'POST':
        form= Pro_ducts(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= Pro_ducts()
            data=Product.objects.all()
    else:
        form= Pro_ducts()
        data=Product.objects.all()
    paginator = Paginator(data, 5)  # Show 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_count = paginator.count
   
    return render(request, 'products.html', {'page_obj': page_obj, 'form': form,'data': data, 'success': success, 'result_count': result_count})

def export_csv2(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Price', 'Image'])

    for obj in Product.objects.all():
        writer.writerow([obj.id, obj.name, obj.price, obj.image])

    return response


def export_excel2(request):
    data = list(Product.objects.values('id', 'name', 'price', 'image'))
    df = pd.DataFrame(data)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    df.to_excel(response, index=False)
    
    return response

def export_pdf2(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle('Data Export')

    data = Product.objects.all()

    y = 800
    # pdf.drawString(100, y, 'ID')
    pdf.drawString(150, y, 'Name')
    pdf.drawString(250, y, 'Price')
    pdf.drawString(350, y, 'Image')

    for obj in data:
        y -= 20
        # pdf.drawString(100, y, str(obj.id))
        pdf.drawString(150, y, obj.name)
        
        price = str(obj.price) if obj.price is not None else "N/A"
        pdf.drawString(250, y, price)
        
        image = obj.image.url if obj.image else "No Image"
        pdf.drawString(350, y, image)

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


# def export_pdf2(request):
    
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="data.pdf"'

#     buffer = BytesIO()
#     pdf = canvas.Canvas(buffer, pagesize=A4)
#     pdf.setTitle('Data Export')

#     data = Product.objects.all()

#     y = 800
#     pdf.drawString(100, y, 'ID')
#     pdf.drawString(150, y, 'Name')
#     pdf.drawString(100, y, 'Price')
#     pdf.drawString(300, y, 'Image')


#     for obj in data:
#         y -= 20
#         pdf.drawString(100, y, str(obj.id))
#         pdf.drawString(150, y, obj.name)
#         pdf.drawString(100, y, obj.price)
#         pdf.drawString(300, y, obj.image)


#     pdf.showPage()
#     pdf.save()

#     buffer.seek(0)
#     return HttpResponse(buffer, content_type='application/pdf')


def delete_view2(request,id):
    instance = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('products')
    else:
        form = Pro_ducts(instance=instance)
    return render (request, 'delete2.html', {'form': form})
 
def update_view2(request,id):
    instance = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = Pro_ducts(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = Pro_ducts(instance=instance)
    return render (request, 'update2.html', {'form': form})

def search_view(request):
    query = request.GET.get('query')
    form= Pro_ducts()

    if query:
        data = Product.objects.filter(name__icontains=query) 
    else:
        data = Product.objects.all()

    paginator = Paginator(data, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_count = paginator.count
    
    return render(request, 'products.html', {'page_obj': page_obj, 'form': form, 'query': query, 'result_count': result_count})
    # form = Pro_ducts()
    # return render (request, 'products.html', {"form": form})


def Brandform(request):
    success = False
    if request.method == 'POST':
        form= Br_and(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= Br_and()
            data=Brand.objects.all()
    else:
        form= Br_and()
        data=Brand.objects.all()
    paginator = Paginator(data, 5)  # Show 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_count = paginator.count
    return render(request, 'brands.html', {'page_obj': page_obj, 'form': form,'data': data, 'success': success, 'result_count': result_count})

def delete_view3(request,id):
    instance = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('brands')
    else:
        form = Br_and(instance=instance)
    return render (request, 'delete3.html', {'form': form})
 
def update_view3(request,id):
    instance = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        form = Br_and(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('brands')
    else:
        form = Br_and(instance=instance)
    return render (request, 'update3.html', {'form': form})

def search_view3(request):
    query = request.GET.get('query')
    form= Br_and()

    if query:
        data = Brand.objects.filter(name__icontains=query) 
    else:
        data = Brand.objects.all()

    paginator = Paginator(data, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_count = paginator.count
    
    return render(request, 'brands.html', {'page_obj': page_obj, 'form': form, 'query': query, 'result_count': result_count})
    # form = Br_and()
    # return render (request, 'brands.html', {"form": form})

def Categoryview(request):
    success = False
    if request.method == 'POST':
        form= Cat_gory(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= Cat_gory()
            data=Category.objects.all()
    else:
        form= Cat_gory()
        data=Category.objects.all()
    paginator = Paginator(data, 5)  # Show 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_count = paginator.count
    return render(request, 'category.html', {'page_obj': page_obj, 'form': form,'data': data, 'success': success, 'result_count': result_count})
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Description'])

    for obj in Category.objects.all():
        writer.writerow([obj.id, obj.name, obj.description])

    return response


def export_excel(request):
    data = list(Category.objects.values('id', 'name', 'description'))
    df = pd.DataFrame(data)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    df.to_excel(response, index=False)
    
    return response


def export_pdf(request):
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle('Data Export')

    data = Category.objects.all()

    y = 800
    pdf.drawString(100, y, 'ID')
    pdf.drawString(150, y, 'Name')
    pdf.drawString(300, y, 'Description')

    for obj in data:
        y -= 20
        pdf.drawString(100, y, str(obj.id))
        pdf.drawString(150, y, obj.name)
        pdf.drawString(300, y, obj.description)

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
  

def delete_view4(request,id):
    instance = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('category')
    else:
        form = Cat_gory(instance=instance)
    return render (request, 'delete4.html', {'form': form})
 
def update_view4(request,id):
    instance = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = Cat_gory(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = Cat_gory(instance=instance)
    return render (request, 'update4.html', {'form': form})

def search_view4(request):
    query = request.GET.get('query')
    form= Cat_gory()

    if query:
        data = Category.objects.filter(name__icontains=query) 
    else:
        data = Category.objects.all()

    paginator = Paginator(data, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_count = paginator.count
    
    return render(request, 'category.html', {'page_obj': page_obj, 'form': form, 'query': query, 'result_count': result_count})


def Productvariantview(request):
    success = False
    if request.method == 'POST':
        form= Product_variant(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= Product_variant()
            data=ProductVariant.objects.all()
    else:
        form= Product_variant()
        data=ProductVariant.objects.all()
    paginator = Paginator(data, 5)  # Show 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_count = paginator.count
    return render(request, 'provariant.html', {'page_obj': page_obj, 'form': form,'data': data, 'success': success, 'result_count': result_count})

def delete_view5(request,id):
    instance = get_object_or_404(ProductVariant, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('provar')
    else:
        form = Product_variant(instance=instance)
    return render (request, 'delete5.html', {'form': form})
 
def update_view5(request,id):
    instance = get_object_or_404(ProductVariant, id=id)
    if request.method == 'POST':
        form = Product_variant(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('provar')
    else:
        form = Product_variant(instance=instance)
    return render (request, 'update5.html', {'form': form})

def search_view5(request):
    query = request.GET.get('query')
    form= Product_variant()

    if query:
        data = ProductVariant.objects.filter(id__icontains=query) 
    else:
        data = ProductVariant.objects.all()

    paginator = Paginator(data, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result_count = paginator.count
    
    return render(request, 'provariant.html', {'page_obj': page_obj, 'form': form, 'query': query, 'result_count': result_count})

 
    # form = Product_variant()
    # return render (request, 'provariant.html', {"form": form})


def Materialview(request):
    success = False
    if request.method == 'POST':
        form= Ma_terial(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= Ma_terial()
            data=Material.objects.all()
    else:
        form= Ma_terial()
        data=Material.objects.all()
    return render (request, 'material.html', {'form': form, 'data': data, 'success': success})

def delete_view6(request,id):
    instance = get_object_or_404(Material, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('material')
    else:
        form = Ma_terial(instance=instance)
    return render (request, 'delete6.html', {'form': form})
 
def update_view6(request,id):
    instance = get_object_or_404(Material, id=id)
    if request.method == 'POST':
        form = Ma_terial(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('material')
    else:
        form = Ma_terial(instance=instance)
    return render (request, 'update6.html', {'form': form})
    # form = Ma_terial()
    # return render (request, 'material.html', {"form": form})

def Productdetailview(request):
    success = False
    if request.method == 'POST':
        form= Product_detail(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= Product_detail()
            data=ProductDetail.objects.all()
    else:
        form= Product_detail()
        data=ProductDetail.objects.all()
    return render (request, 'prodetail.html', {'form': form, 'data': data, 'success': success})

def delete_view7(request,id):
    instance = get_object_or_404(ProductDetail, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('detail')
    else:
        form = Product_detail(instance=instance)
    return render (request, 'delete7.html', {'form': form})
 
def update_view7(request,id):
    instance = get_object_or_404(ProductDetail, id=id)
    if request.method == 'POST':
        form = Product_detail(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('detail')
    else:
        form = Product_detail(instance=instance)
    return render (request, 'update7.html', {'form': form})
    # form = Product_detail()
    # return render (request, 'prodetail.html', {"form": form})

def Revieww(request):
    success = False
    if request.method == 'POST':
        form= Re_view(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= Re_view()
            data=Review.objects.all()
    else:
        form= Re_view()
        data=Review.objects.all()
    return render (request, 'review.html', {'form': form, 'data': data, 'success': success})

def delete_view8(request,id):
    instance = get_object_or_404(Review, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('review')
    else:
        form = Re_view(instance=instance)
    return render (request, 'delete8.html', {'form': form})
 
def update_view8(request,id):
    instance = get_object_or_404(Review, id=id)
    if request.method == 'POST':
        form = Re_view(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = Re_view(instance=instance)
    return render (request, 'update8.html', {'form': form})
    # form = Re_view()
    # return render (request, 'review.html', {"form": form})

def cartview(request):
    success = False
    if request.method == 'POST':
        form= CART(request.POST)
        data = None
        if form.is_valid():
            form.save()
            success = True
            form= CART()
            data=Cart.objects.all()
    else:
        form= CART()
        data=Cart.objects.all()
    return render (request, 'cart.html', {'form': form, 'data': data, 'success': success})

def delete_view8(request,id):
    instance = get_object_or_404(Cart, id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('cart')
    else:
        form = CART(instance=instance)
    return render (request, 'delete8.html', {'form': form})
 
def update_view8(request,id):
    instance = get_object_or_404(Cart, id=id)
    if request.method == 'POST':
        form = CART(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('cart')
    else:
        form = CART(instance=instance)
    return render (request, 'update8.html', {'form': form})
 
    # form = CART()
    # return render (request, 'cart.html', {"form": form})

def order(request):
    form = Or_der()
    return render (request, 'order.html', {"form": form})

def orderproduct(request):
    form = Order_product()
    return render (request, 'OP.html', {"form": form})

def address(request):
    form = add_ress()
    return render (request, 'address.html', {"form": form})

def paymentview(request):
    form = paymentform()
    return render (request, 'payment.html', {"form": form})

def whishlistview(request):
    form = Whishlistform()
    return render (request, 'whishlist.html', {"form": form})

def couponview(request):
    form = Couponform()
    return render (request, 'coupon.html', {"form": form})

def promoview(request):
    form = promoform()
    return render (request, 'promotion.html', {"form": form})

def orderpromoview(request):
    form = orderpromoform()
    return render (request, 'orderpromo.html', {"form": form})

def colorview(request):
    form = colorform()
    return render (request, 'color.html', {"form": form})

def sizeview(request):
    form = sizeform()
    return render (request, 'size.html', {"form": form})

def styleview(request):
    form = styleform()
    return render (request, 'style.html', {"form": form})

def paymentmethodview(request):
    form = paymentmethodform()
    return render (request, 'paymethod.html', {"form": form})

def shippingaddressview(request):
    form = shippingaddressform()
    return render (request, 'shipaddress.html', {"form": form})

def checkoutview(request):
    form = checkoutform()
    return render (request, 'checkout.html', {"form": form})

def dashboardview(request):
    form = dashboardform()
    return render (request, 'dashboard.html', {"form": form})

def customerview(request):
    form = customerform()
    return render (request, 'customer.html', {"form": form})


# templatess
def cart2(request):
    return render(request, 'webDB/cart2.html')

def checkout2(request):
    return render(request, 'webDB/checkout2.html')

def contact(request):
    return render(request, 'webDB/contact.html')

def index(request):
    return render(request, 'webDB/index.html')

def login2(request):
    return render(request, 'webDB/login2.html')

def myAccount(request):
    return render(request, 'webDB/my-account.html')

def productdetail(request):
    return render(request, 'webDB/product-detail.html')

def productlist(request):
    return render(request, 'webDB/product-list.html')