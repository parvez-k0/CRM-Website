from django.urls import path
from . import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('logout/',views.logout,name='logout'),
    path('viewcustomers/',views.viewcustomers,name='viewcustomers'),
    path('viewenquiries/',views.viewenquiries,name='viewenquiries'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('product/',views.product,name='product'),
    path('viewcomplaints/',views.viewcomplaints,name="viewcomplaints"),
    path('viewfeedbacks/',views.viewfeebacks,name="viewfeedbacks"),
    path('delres/<id>',views.delres,name="delres"),
    path('changepassword/',views.changepassword,name="changepassword"),
]