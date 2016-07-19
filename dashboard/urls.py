from django.conf.urls import url


from dashboard.views import DeleteProductView, ProductFormView, UpdateProductView, CategoryDetailsView


urlpatterns = [
    url(r'^products/$', ProductFormView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/update/$', UpdateProductView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', DeleteProductView.as_view(), name='delete'),
    url(r'^api/category/category_details/(?P<category_id>[0-9]+)/$', CategoryDetailsView.as_view(), name='category_details'),
]
