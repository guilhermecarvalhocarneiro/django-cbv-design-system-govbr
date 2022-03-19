from django.urls import path
from modelo import views as v

app_name = 'modelo'

urlpatterns = [
    path('', v.index, name='modelo_index'),
]