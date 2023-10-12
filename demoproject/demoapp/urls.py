from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('add/addrecord/',views.addrecord,name='addrecord'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='updaterecord'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('search/',views.search,name='search')

]