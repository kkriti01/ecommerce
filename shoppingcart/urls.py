from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from dashboard.views import CategoryViewSet, ProductViewSet
from dashboard import urls as dashboardUrl
from account import urls as accountUrl
from . import views

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'', include(dashboardUrl, namespace="dashboard")),
    url(r'^account/', include(accountUrl, namespace="account")),
    url(r'^$', views.home),
    url(r'^cart/$', views.CartView.as_view(), name="cart"),
    url(r'^cart/remove_item/$', views.remove_item, name="remove_item"),
    url(r'^cart/discard_cart/$', views.discard_cart, name="discard_cart"),
    url(r'^cart/increased_item_quantity/$', views.increase_item_quantity, name="increased_item_quantity"),
    url(r'^cart/decreased_item_quantity/$', views.decrease_item_quantity, name="decreased_item_quantity"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
