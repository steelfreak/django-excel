from django.urls import path
from . import views 

urlpatterns = [
	path('export_data_to_excel/', views.export_data_to_excel),
	path('Import_csv/', views.Import_csv, name="Import_csv"),
	path('simple_upload/', views.simple_upload, name="simple_upload"),
	# path('import_data_to_db/', views.import_data_to_db)
	]