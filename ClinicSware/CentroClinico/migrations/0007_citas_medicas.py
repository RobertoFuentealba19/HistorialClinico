# Generated by Django 4.2.1 on 2023-05-28 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CentroClinico', '0006_alter_paciente_historial_clinico_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citas_medicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('nombre_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroClinico.paciente')),
            ],
        ),
    ]
