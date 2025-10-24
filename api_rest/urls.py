from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('cadastro/', views.register, name='cadastro'),  # Página de cadastro
    path('upload_image/', views.upload_image, name='upload_image'),  # Página de upload
    path('report/<int:upload_id>/', views.view_report, name='view_report'),  # URL para visualizar o laudo
    path('report/<int:upload_id>/pdf/', views.export_pdf, name='export_pdf'),  # Exportar PDF
    path('report/<int:upload_id>/email/', views.send_email, name='send_email'),  # Enviar por e-mail
]
