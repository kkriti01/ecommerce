from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from rest_framework import viewsets


from .forms import UpdateProductForm
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductFormView(View):
    template_name = 'dashboard/home.html'

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        return render(request, self.template_name, {'product': product})


class UpdateProductView(View):
    form_class = UpdateProductForm
    template_name = 'dashboard/product/updateProduct.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        instance = get_object_or_404(Product, pk=pk)
        form = self.form_class(request.POST or None, instance=instance)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        instance = get_object_or_404(Product, pk=pk)
        form = self.form_class(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:home'))
        return render(request, self.template_name, {'form': form})


class DeleteProductView(View):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'dashboard/product/product_confirm_delete.html', {'product': product})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return HttpResponseRedirect(reverse('dashboard:home'))


class CategoryDetailsView(View):

    def get(self, request, *kwargs, **args):
        categoryid = self.kwargs['category_id']
        if categoryid:
            try:
                category = Category.objects.get(id=categoryid)
                product = category.product.all()
            except Category.DoesNotExist:
                return HttpResponse("category with this id DoesNotExist")
            prod_list = []
            for items in product:
                prod_list.append({
                    'id': items.id,
                    'name': items.name,
                    'description': items.description,
                    'stock': items.stock,
                    'price': items.price,
                    'image': items.image.url if items.image else '',
                })
            return JsonResponse({"product": prod_list})
        else:
            return HttpResponse("category Does Not Exist")

