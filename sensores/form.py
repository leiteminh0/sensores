from django import forms
from sensores.models import Sensor, Motor, SensorMotor, DadosSensor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['Nome', 'Tipo']
        labels = {'Nome': 'Nome do Sensor', 'Tipo': 'Tipo do Sensor'}

class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = ['Marca', 'Modelo', 'Potencia', 'Descricao']
        labels = {'Marca': 'Marca', 'Modelo': 'Modelo', 'Potencia': 'Potência', 'Descricao': 'Descrição'}

class SensorMotorForm(forms.ModelForm):
    class Meta:
        model = SensorMotor
        fields = ['MotorId', 'SensorId']
        labels = {'MotorId': 'Motor', 'SensorId': 'Sensor'}

class DadosSensorForm(forms.ModelForm):
    class Meta:
        model = DadosSensor
        fields = ['MotorId', 'SensorId', 'Valor']
        labels = {'MotorId': 'Motor', 'SensorId': 'Sensor', 'Valor': 'Valor da Medição'}
