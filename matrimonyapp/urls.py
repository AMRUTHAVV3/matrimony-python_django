from django.urls import path
from matrimonyapp import views
urlpatterns=[
       path('index/',views.index_fn),
       path('addcustomer/',views.addcustomer_fn,name='addcustomer_fn'),
       path('savecustomer_fn/',views.savecustomer_fn,name='savecustomer_fn'),
       path('displaycustomer/',views.displaycustomer_fn,name='displaycustomer_fn'),
       path('editcustomer_fn/<int:dataid>/',views.editcustomer_fn,name='editcustomer_fn'),
       path('updatecategory/<int:dataid>/',views.updatecategory,name='updatecategory'),
       path('deletecustomer_fn/<int:dataid>/',views.deletecustomer_fn,name='deletecustomer_fn'),
       path('login_fn/', views.login_fn, name='login_fn'),
       path('admin_login/', views.admin_login, name='admin_login'),
       path('admin_logout/',views.admin_logout, name='admin_logout'),
       path('viewfeedback_fn/',views.viewfeedback_fn, name='viewfeedback_fn'),

]