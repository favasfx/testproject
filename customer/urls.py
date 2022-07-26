from django.urls import path
from.import views


urlpatterns = [path('test',views.test,name='ab'),
path('head',views.head,name='cd'),

path('cus',views.cus,name='ef')

    
]
