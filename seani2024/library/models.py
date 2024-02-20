from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(verbose_name="Nombre",max_length=100)
    description = models.CharField(verbose_name="Descripción",max_length=200)

    def num_questions(self):
        return self.question_set.count()
    
    num_questions.short_description = "Numero de preguntas"
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'modulo'
        verbose_name_plural ='modulos'

class Question(models.Model):
    module=models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        verbose_name="Módulo",)
    question_text= models.TextField(
        verbose_name="Texto de la Pregunta",
        null=True,blank=True)
    question_image = models.ImageField(
        verbose_name="Imagen de la Pregunta",
        upload_to="questions",
        null=True,blank=True)
    answer1 = models.CharField(
        verbose_name="Respuesta A",
        max_length=200)
    answer2 = models.CharField(
        verbose_name="Respuesta B",
        max_length = 200)
    answer3 = models.CharField(
        verbose_name="Respuesta C",
        max_length = 200,
        null=True,blank=True)
    answer4 = models.CharField(
        verbose_name="Respuesta D",
        max_length = 200,
        null=True,blank=True)
    correct  = models.CharField(
        verbose_name="Respuesta Correcta",
       max_length = 5)
    
    def __str__(self):
        return f"{ self.module} - {self.id}"
    
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural ='preguntas'
