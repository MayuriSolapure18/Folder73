from django.urls import path
from .views import AddProduct, ShowProduct, UpdateProduct,DeleteProduct

urlpatterns=[
    path('add/',AddProduct,name='AddProduct'),
    path('show/',ShowProduct,name='ShowProduct'),
    path('update/<int:update>',UpdateProduct,name='update'),
    path('delete/<int:delete>',DeleteProduct,name='delete'),
    
    

    
    
]