from django.urls import path,include
from . import views

urlpatterns = [
    # TRYING LOGIN path('',views.collegue_login), #localhost:p/colleague
    path('home/',views.home,name = 'homepage'),
    #TODO CHANGE THIS PATH THROUGH OUT APP SO FIRST PAGE IS "" NAVS TO HOME
    path('',views.colleague_form,name = 'colleague_insert'), #get and post request for insert opertation
    path('<int:id>/', views.colleague_list,name = 'colleague_update'), #get and post request for update opertation
    path('delete/<int:id>/',views.colleague_delete,name='colleague_delete'),#delete operation
    path('list/',views.colleague_list,name = 'colleague_list'), #get and post request for retrive/display records
    path('equipment/',views.equipment_list,name = 'equipment_update'),
]