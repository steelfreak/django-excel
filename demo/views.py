from django.shortcuts import render
from .resources import EmployeeResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from .models import Employee

import pandas as pd
import os
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage



def simple_upload(request):
	if request.method == 'POST':
		employee_resource = EmployeeResource()
		dataset = Dataset()
		new_employee = request.FILES['myfile']

		if not new_employee.name.endswith('xlsx'):
			messages.info(request, 'wrong format')
			return render(request, 'upload.html')

		imported_data = dataset.load(new_employee.read(),format='xlsx')
		for data in imported_data:
			value = Employee(
				data[0],
				data[1],
				data[2],
				data[3]
				)
			value.save()
	return render(request, 'upload.html')






def export_data_to_excel(request):
	objs = Employee.objects.all()
	data = []

	for obj in objs:
		data.append({
			"employee_name" : obj.employee_name,
			"employee_contact": obj.employee_contact,
			"employee_address": obj.employee_address
			})

	pd.DataFrame(data).to_excel('output.xlsx')
	return JsonResponse({
			'status' : 200
		})



def Import_csv(request):
	print('s')
	try:
		if request.method == "POST" and request.FILES['myfile']:
			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			upload_file_url = fs.url(filename)
			excel_file = upload_file_url
			print(excel_file)
			empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
			print(type(empexceldata))
			dbframe = empexceldata
			for dbframe in dbframe.itertuples():
				obj = Employee.objects.create(employee_name=dbframe.employee_name,  
											  employee_contact=dbframe.employee_contact,
											  employee_address=dbframe.employee_address,
											  )
				print(type(obj))
				obj.save()

			return render(request, 'importexcel.html', {'upload_file_url':upload_file_url })
	except Exception as identifier:
		print(identifier)
	return render(request, 'importexcel.html', {})
	
# def import_data_to_db(request):
# 	if request.method =='POST':
# 		file = request.FILES['files']
# 		obj = ExcelFile.objects.create(
# 			file = file
# 		)
# 		path = str(obj.file)
# 		print(f'{settings.BASE_DIR}/{path}')
# 		df = pd.read_excel(path)
# 		for d in df.values:
# 			print(d)

# 	return render(request, 'excel.html')