from django.db import models

# Create your models here.

class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name = "Etapa"
    )
    application_date = models.DateField(
        verbose_name ="Fecha de aplicacion"
    )

    @property
    def year(self):
        return self.aplication_date.year

    @property
    def month(self):
        months = ['enero', 'febrero', 'Marzo', 'abril', 'Mayo',
                'Julio', 'Junio', 'Septiembre', 'Octubre', 
                'Noviembre', 'Diciembre']
        return months[self.application_date.month - 1]

    def __str__(self):
        return f"{ self.stage} - { self.month }, { self.year}"

    class Meta:
        verbose_name="etapa"
        verbose_name_plural="etapas"
