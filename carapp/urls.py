from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.homePage,name='homePage'),
    url(r'^carDetails/(\d+)$',views.carDetails,name='carDetails'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^addToCart/(\d+)/$', views.addToCart, name="addToCart"),
    # url(r'^delete/(\d+)/$', views.delete, name="delete"),
    # url(r'^order-summary/$', views.order_details, name="order_summary"),
    # url(r'^success/$', views.success, name='purchase_success'),
    # url(r'^item/delete/(?P<item_id>[-\w]+)/$', views.delete_from_cart, name='delete_item'),
    # url(r'^checkout/$', views.checkout, name='checkout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)