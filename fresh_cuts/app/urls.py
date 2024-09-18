from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
    path('logout',views.logout),
    path('register',views.register),
    path('shopregister',views.shopregister),
    path('userhome',views.userhome),
    path('adminhome',views.adminhome),
    path('shophome',views.shophome),
    path('addpro',views.addpro),
    path('viewpro',views.viewpro),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),
    path('profile',views.profile),
    path('upload',views.upload),
    path('userviewproduct',views.userviewproduct),
    path('prodetails/<int:id>',views.prodetails),
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

    

]

