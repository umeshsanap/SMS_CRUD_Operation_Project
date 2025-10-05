from django.db import models

# Create your models here.


class StudentManagement(models.Model):
    Std_Grade = (
        ('A', 'A-Division'),
        ('B','B-Division'),
        ('C','C-Division'),
        ('E','E-Division'),
        ('F','F-Division')
    )
    std_Class = (
        ('1','1 class'),
        ('2','2 class'),
        ('3','3 class'),
        ('4','4 class')
    )
    std_name = models.CharField(max_length=50)
    std_roll_no = models.IntegerField()
    std_division = models.CharField(max_length=1,  choices=Std_Grade)
    std_standard = models.CharField(max_length=1, choices=std_Class)
    std_email = models.EmailField(unique=True)
    std_address = models.CharField(max_length=50)

    def __str__(self):
        return f"name :{self.std_name}, rollNo : {self.std_roll_no}, standard : {self.std_standard}, division : {self.std_division}"