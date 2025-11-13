from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from sensores.models import Sensor, Motor, SensorMotor, DadosSensor
from sensores.form import SensorForm, MotorForm, SensorMotorForm, DadosSensorForm
from django.urls import reverse_lazy


class SensorListView(ListView):
    model = Sensor
    template_name = 'sensor_list.html'

class SensorCreateView(CreateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'sensor_form.html'
    success_url = reverse_lazy('sensor_list')

class SensorUpdateView(UpdateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'sensor_form.html'
    success_url = reverse_lazy('sensor_list')

class SensorDeleteView(DeleteView):
    model = Sensor
    template_name = 'sensor_confirm_delete.html'
    success_url = reverse_lazy('sensor_list')


class MotorListView(ListView):
    model = Motor
    template_name = 'motor_list.html'

class MotorCreateView(CreateView):
    model = Motor
    form_class = MotorForm
    template_name = 'motor_form.html'
    success_url = reverse_lazy('motor_list')

class MotorUpdateView(UpdateView):
    model = Motor
    form_class = MotorForm
    template_name = 'motor_form.html'
    success_url = reverse_lazy('motor_list')

class MotorDeleteView(DeleteView):
    model = Motor
    template_name = 'motor_confirm_delete.html'
    success_url = reverse_lazy('motor_list')


class SensorMotorListView(ListView):
    model = SensorMotor
    template_name = 'sensormotor_list.html'

class SensorMotorCreateView(CreateView):
    model = SensorMotor
    form_class = SensorMotorForm
    template_name = 'sensormotor_form.html'
    success_url = reverse_lazy('sensormotor_list')

class SensorMotorUpdateView(UpdateView):
    model = SensorMotor
    form_class = SensorMotorForm
    template_name = 'sensormotor_form.html'
    success_url = reverse_lazy('sensormotor_list')

class SensorMotorDeleteView(DeleteView):
    model = SensorMotor
    template_name = 'sensormotor_confirm_delete.html'
    success_url = reverse_lazy('sensormotor_list')

class DadosSensorListView(ListView):
    model = DadosSensor
    template_name = 'dadossensor_list.html'

class DadosSensorCreateView(CreateView):
    model = DadosSensor
    form_class = DadosSensorForm
    template_name = 'dadossensor_form.html'
    success_url = reverse_lazy('dadossensor_list')

class DadosSensorUpdateView(UpdateView):
    model = DadosSensor
    form_class = DadosSensorForm
    template_name = 'dadossensor_form.html'
    success_url = reverse_lazy('dadossensor_list')

class DadosSensorDeleteView(DeleteView):
    model = DadosSensor
    template_name = 'dadossensor_confirm_delete.html'
    success_url = reverse_lazy('dadossensor_list')

def dashboard(request):
    total_motores = Motor.objects.count()
    total_sensores = Sensor.objects.count()
    total_sensor_motor = SensorMotor.objects.count()
    ultimos_dados = DadosSensor.objects.order_by('-DataHora')[:10]

    context = {
        'total_motores': total_motores,
        'total_sensores': total_sensores,
        'total_sensor_motor': total_sensor_motor,
        'ultimos_dados': ultimos_dados,
    }
    return render(request, 'dashboard.html', context) 