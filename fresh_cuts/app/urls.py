from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
    path('logout',views.logout),
    path('register',views.register),
    path('shopregister',views.shopregister),
    path('userhome',views.userhome),
    path('adminhome',views.adminhome),
    # path('shophome',views.shophome),
    path('deliveryhome',views.deliverys),
    path('addpro',views.addpro),
    path('viewpro',views.viewpro),
    # path('shop_view/<int:id>',views.shop_view),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),
    path('profile',views.profile),
    # path('viewpro',views.shops),
    path('upload',views.upload),
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('userviewproduct',views.userviewproduct),
    path('prodetails/<int:id>',views.prodetails),
    path('shopprodetails/<int:id>',views.shopprodetails),
    path('addtocart/<int:id>',views.user_cart),
    path('user_view_cart',views.user_view_cart),
    path('qty_incri/<int:id>',views.qty_incri),
    path('qty_decri/<int:id>',views.qty_decri),
    path('buynow/<int:id>',views.buynow),
    path('deleteitem/<int:id>',views.deleteitem),
    path('orderdetails',views.orderdetails),
    path('delregister',views.delregister),
    path('viewshop',views.viewshop),
    path('aboutus',views.aboutus),
    path('contact',views.contact),
    path('service',views.service),
    path('bookinghistry',views.bookinghistry),




    

]

