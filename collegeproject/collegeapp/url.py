
from django.urls import path

from collegeapp import views

urlpatterns = [
    path('display/',views.display,name='display'),
    path('doc1/',views.doc1,name='doc1'),
    path('status/',views.status,name='status'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete')
]
