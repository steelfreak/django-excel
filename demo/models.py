from django.db import models

# Create your models here.

class Employee(models.Model):
	employee_name = models.CharField(max_length=100)
	employee_contact = models.CharField(max_length=100)
	employee_address = models.CharField(max_length=500)


# 	def __str__(self):
# 		return self.employee_name


# class ExcelFile(models.Model):
# 	file = models.FileField(upload_to="excel")
