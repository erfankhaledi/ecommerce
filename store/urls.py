from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
        HomeView,
          ItemDetailView,
            add_to_cart,remove_from_cart,
              remove_single_item_from_cart,
                OrderSummaryView,
                    CheckoutView,
                        PaymentView,
                            AddCouponView,
                                RequestRefundView
                    )

app_name = "store"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('order-summary/', OrderSummaryView.as_view(), name="order-summary"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('product/<slug>/', ItemDetailView.as_view(), name="product"),
    path('payment/<payment_option>/', PaymentView.as_view(), name="payment"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart')

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)