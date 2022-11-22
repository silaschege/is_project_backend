from pickle import NONE
from django.contrib import messages
from django.contrib.auth import get_user_model 
from installments.models import InstallmentModel,InstallmentNumberModel
User = get_user_model()
from manufacturer.models import ManufactureRegisterModel
from .models import ProductCategoryModel, ProductNameModel,ProductsModel,PackagingMetric,PackagingQuantity

from django.shortcuts import render, redirect
from .forms import (ManufacturerAddProductForm,
ManufacturerAddProductName,
AdminAddCategoryForm,
AdminAddProductPackagingMetric
,AdminAddProductPackagingQuantity)
from django.http import HttpResponseRedirect

# Create your views here.


               
def FarmerInstallmentsListView (request):
    user = request.user 
    installmentNumber = InstallmentNumberModel.objects.filter(user_id=user).filter(balance__gte=1)
    return render(request,'Farmerproducts/FarmerInstallmentList.html',{
        'installmentNumber':installmentNumber
    })



def FarmerAddPlantsList(request,category_id):
    # this is all the plants that are in the system
    addPlantsList = ProductsModel.objects.filter(productCategory=category_id)
    return render(request,'Farmerproducts/FarmerAddPlantsList.html',{
        'addPlantsList': addPlantsList,
    })

def FarmerAddPlantsCategoryList(request):
    # this is all the plants that are in the system
    addPlantCategoryList = ProductCategoryModel.objects.all()
    return render(request,'Farmerproducts/FarmerAddPlantCategoryList.html',{
        
        'addPlantCategoryList': addPlantCategoryList,
    })

###################################################################################################################
# manufacturer



def ManufacturerAddProduct(request):
    # check if form is submitted
    submitted = False
    if request.method == "POST":
        form = ManufacturerAddProductForm(request.POST, request.FILES)
    
        if form.is_valid():
             
            product = form.save(commit=False)
            product.productManufacturer = request.user # logged in user
            product.save()
            messages.success(request, ("Your product has been added!"))
            return 	HttpResponseRedirect('ManufacturerAddProduct?submitted=True')	
            
    else:
        # if submitted is not done
        form = ManufacturerAddProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'manufacturerProducts/manufacturerAddProducts.html', {'form':form, 'submitted':submitted})

def ManufacturerLoadProductsName(request):
    product_category_id = request.GET.get('productCategory')
    product_name = ProductNameModel.objects.filter(productCategory=product_category_id).order_by('productName')
    return render(request, 'manufacturerProducts/manufacturerLoadProductDropDown.html', {'product_name':product_name})

def ManufacturerStore(request):
    manufacturer = request.user 
    storeProducts=ProductsModel.objects.filter(productManufacturer=manufacturer)
    return render(request,'manufacturerProducts/Store.html',{
        'storeProducts':storeProducts
    }

    )

def ManufacturerUpdateStore(request,product_id):
    manufacturerUpdate = ProductsModel.objects.get(id=product_id)
    form = ManufacturerAddProductForm(request.POST,request.FILES,instance=manufacturerUpdate)
    if form.is_valid():
            form.save()
            messages.success(request, (" Your store item has been updated succesfully!!!"))
            return redirect('ManufacturerSelectUpdate',product_id=product_id)	

    return render(request,'manufacturerProducts/manufacturerUpdateStore.html',{
       
        'form':form,
    }

    )

def ManufacturerSelectUpdate(request,product_id):
    manufacturerUpdate = ProductsModel.objects.filter(id=product_id)
    return render(request,'manufacturerProducts/ManufacturerSelectUpdate.html',{
        'manufacturerUpdate':manufacturerUpdate,
        
    }

    )

def ManufacturerAddProductNameView(request):
        # check if form is submitted
    submitted = False
    if request.method == "POST":
        form = ManufacturerAddProductName(request.POST, request.FILES)
    
        if form.is_valid():
            
            product = form.save(commit=False)
            product.productManufacturer = request.user # logged in user
            product.save()
            messages.success(request, ("Your product name has been added!"))
            return 	HttpResponseRedirect('ManufacturerAddProductName?submitted=True')	
            
    else:
        # if submitted is not done
        form = ManufacturerAddProductName
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'manufacturerProducts/manufacturerAddProductName.html', {'form':form, 'submitted':submitted})

def ManufacturerProductNames(request):
    product=ProductNameModel.objects.all()

    return render(request, 'manufacturerProducts/manufacturerAllProductNames.html', {'product':product})





###########################################################################################################
#admin
def AdminAddCategory (request):
    submitted = False 
    if request.method == 'POST':
        form = AdminAddCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, (" Your Category has been added succesfully!!!"))
        return HttpResponseRedirect('AdminAddCategoryU?submitted=True')	
    else:
        form = AdminAddCategoryForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'admin/addCategory.html',{'form':form,'submitted':submitted})

def AdminAddPackagingMetric(request):
    submitted = False 
    if request.method == 'POST':
        form = AdminAddProductPackagingMetric(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, (" Your Packaging Metric  has been added succesfully!!!"))
       
        return HttpResponseRedirect('AdminAddPackagingMetric?submitted=True')	
    else:
        form = AdminAddProductPackagingMetric
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'admin/addProductPackagingMetric.html',{'form':form,'submitted':submitted})
   

def AdminAddPackagingQuantity(request):
    submitted = False 
    if request.method == 'POST':
        form = AdminAddProductPackagingQuantity(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, (" Your  Packaging Quantity has been added succesfully!!!"))
       
        return HttpResponseRedirect('AdminAddPackagingQuantity?submitted=True')	
    else:
        form = AdminAddProductPackagingQuantity
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'admin/addProductPackagingQuantity.html',{'form':form,'submitted':submitted})

def AdminAllProducts(request):
    products=ProductsModel.objects.all()
    return render(request,'admin/adminAllProducts.html',{'products':products})

def AdminAllCategory(request):
    products=ProductCategoryModel.objects.all()
    form_class = AdminAddCategoryForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST,request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data.get('categoryName')
            form.cleaned_data.get('')
            form.save()
    return render(request,'admin/adminAllCategory.html',{'products':products,'form':form})

def AdminAllPackagingMetric(request):
    products=PackagingMetric.objects.all()
    
    return render(request,'admin/adminAllPackagingMetric.html',{'products':products})

def AdminAllPackagingQuantity(request):
    products=PackagingQuantity.objects.all()
    return render(request,'admin/adminAllPackagingQuantity.html',{'products':products})

def  AdminDeleteCategory(request,id):
    products=ProductCategoryModel.objects.filter(id=id)
    products.delete()
    messages.success(request, (" Your Category has been deleted succesfully!!!"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def  AdminDeletePackagingMetric(request,id):
    products=PackagingMetric.objects.filter(id=id)
    products.delete()
    messages.success(request, (" Your Packaging Metric has been deleted succesfully!!!"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def  AdminDeletePackagingQuantity(request,id):
    products=PackagingQuantity.objects.filter(id=id)
    products.delete()
    messages.success(request, (" Your Packaging Metric has been deleted succesfully!!!"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



    
    







