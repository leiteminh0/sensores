from django.urls import path
from django.views.generic import RedirectView
from sensores.views import (
    SensorListView, SensorCreateView, SensorUpdateView, SensorDeleteView,
    MotorListView, MotorCreateView, MotorUpdateView, MotorDeleteView,
    SensorMotorListView, SensorMotorCreateView, SensorMotorUpdateView, SensorMotorDeleteView,
    DadosSensorListView, DadosSensorCreateView, DadosSensorUpdateView, DadosSensorDeleteView,
    dashboard
)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='motor_list'), name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    
    path('sensores/', SensorListView.as_view(), name='sensor_list'),
    path('sensores/novo/', SensorCreateView.as_view(), name='sensor_create'),
    path('sensores/<int:pk>/editar/', SensorUpdateView.as_view(), name='sensor_update'),
    path('sensores/<int:pk>/delete/', SensorDeleteView.as_view(), name='sensor_delete'),

    path('motores/', MotorListView.as_view(), name='motor_list'),
    path('motores/novo/', MotorCreateView.as_view(), name='motor_create'),
    path('motores/<int:pk>/editar/', MotorUpdateView.as_view(), name='motor_update'),
    path('motores/<int:pk>/delete/', MotorDeleteView.as_view(), name='motor_delete'),

    path('sensormotor/', SensorMotorListView.as_view(), name='sensormotor_list'),
    path('sensormotor/novo/', SensorMotorCreateView.as_view(), name='sensormotor_create'),
    path('sensormotor/<int:pk>/editar/', SensorMotorUpdateView.as_view(), name='sensormotor_update'),
    path('sensormotor/<int:pk>/delete/', SensorMotorDeleteView.as_view(), name='sensormotor_delete'),

    path('dadossensor/', DadosSensorListView.as_view(), name='dadossensor_list'),
    path('dadossensor/novo/', DadosSensorCreateView.as_view(), name='dadossensor_create'),
    path('dadossensor/<int:pk>/editar/', DadosSensorUpdateView.as_view(), name='dadossensor_update'),
    path('dadossensor/<int:pk>/delete/', DadosSensorDeleteView.as_view(), name='dadossensor_delete'),
]