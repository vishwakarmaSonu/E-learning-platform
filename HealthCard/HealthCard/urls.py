from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from health.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('login', Login,name="login"),
    path('video', video,name="video"),
    
    path('about', about,name="about"),
    path('register', Registeration,name="register"),
    path('logout', Logout,name="logout"),
    path('cancel_appointment<int:pid>', cancel_appointment,name="cancel_appointment"),
    path('patient_invoices<int:pid><str:task>', patient_invoices,name="patient_invoices"),

#Admin Url
    path('admin_dashboard', admin_dashboard,name="admin_dashboard"),
    path('admin_view_appointment', admin_view_appointment,name="admin_view_appointment"),
    path('admin_view_doctors', admin_view_doctors,name="admin_view_doctors"),
    path('admin_view_patients', admin_view_patients,name="admin_view_patients"),
    path('request_health_card', request_health_card,name="request_health_card"),
    path('grant_card<int:pid>', grant_card,name="grant_card"),
    path('card_cancelation<int:pid>', card_cancelation,name="card_cancelation"),
    path('delete_patient<int:pid>', delete_patient,name="delete_patient"),
    path('all_card_user', all_card_user,name="all_card_user"),
    path('admin_view_hospitals', admin_view_hospitals,name="admin_view_hospitals"),
    path('admin_view_medicals', admin_view_medicals,name="admin_view_medicals"),
    path('admin_hospital_appointment', admin_hospital_appointment,name="admin_hospital_appointment"),
    path('admin_patient_invoices<int:pid>', admin_patient_invoices,name="admin_patient_invoices"),
    path('admin_hospital_invoices<int:pid>', admin_hospital_invoices,name="admin_hospital_invoices"),
    path('admin_patient_search_by_id', admin_patient_search_by_id, name="admin_patient_search_by_id"),
    path('admin_profile', admin_profile, name="admin_profile"),
    path('edit_admin_profile', edit_admin_profile, name="edit_admin_profile"),

#Patient Url
    path('patient_dashboard', patient_dashboard,name="patient_dashboard"),
    path('patient_profile', Patient_Profile,name="patient_profile"),
    path('change_password', Change_Password,name="change_password"),
    path('search_doctor', search_doctor,name="search_doctor"),
    path('booking-success<int:pid>', payment_success,name="booking-success"),
    path('payment<int:pid>', payment,name="payment"),
    path('appointment<int:pid>', appointment,name="appointment"),
    path('p_appointment', p_appointment,name="p_appointment"),
    path('confirmed_p_appointment',confirmed_p_appointment,name="confirmed_p_appointment"),
    path('history_p_appointment',history_p_appointment,name="history_p_appointment"),
    path('p_search_appointment',p_search_appointment,name="p_search_appointment"),
    path('health_card',health_card,name="health_card"),
    path('thank_card',thank_card,name="thank_card"),
    path('apply_card',apply_card,name="apply_card"),
    path('search_hospital',search_hospital,name="search_hospital"),
    path('hospital_booking-success<int:pid>', hospital_payment_success,name="hospital_booking-success"),
    path('hospital_payment<int:pid>', hospital_payment,name="hospital_payment"),
    path('hospital_appointment<int:pid>', hospital_appointment,name="hospital_appointment"),
    path('cancel_hospital_appointment<int:pid>', cancel_hospital_appointment,name="cancel_hospital_appointment"),
    path('patient_hospital_invoices<int:pid>', patient_hospital_invoices,name="patient_hospital_invoices"),
    path('h_appointment', h_appointment,name="h_appointment"),
    path('confirmed_h_appointment',confirmed_h_appointment,name="confirmed_h_appointment"),
    path('history_h_appointment',history_h_appointment,name="history_h_appointment"),
    path('all_doctor_appointment',all_doctor_appointment,name="all_doctor_appointment"),
    path('all_hospital_appointment',all_hospital_appointment,name="all_hospital_appointment"),

#Doctor Url
    path('doctor_dashboard', doctor_dashboard,name="doctor_dashboard"),
    path('doctor_profile', Doctor_Profile,name="doctor_profile"),
    path('doctor_change_password', Doctor_Change_Password,name="doctor_change_password"),
    path('d_appointment', d_appointment,name="d_appointment"),
    path('update_status<int:pid>', update_status,name="update_status"),
    path('confirmed_d_appointment',confirmed_d_appointment,name="confirmed_d_appointment"),
    path('history_d_appointment',history_d_appointment,name="history_d_appointment"),
    path('add_medicine<int:pid>', add_medicine, name="add_medicine"),
    path('doctor_invoice<int:pid>', doctor_invoices, name="doctor_invoice"),
    path('doctor_cancel_appointment<int:pid>', doctor_cancel_appointment, name="doctor_cancel_appointment"),
    path('doc_patient_dashboard<int:pid>', doc_patient_dashboard, name="doc_patient_dashboard"),
    path('doctor_status<int:pid>', doctor_status, name="doctor_status"),
    path('d_search_appointment',d_search_appointment,name="d_search_appointment"),
    path('all_patient_appointment',all_patient_appointment,name="all_patient_appointment"),
    path('doctor_patient_search_by_id', doctor_patient_search_by_id, name="doctor_patient_search_by_id"),
    path('my_patient', my_patient, name="my_patient"),
    path('add_prescription<int:pid>', add_prescription, name="add_prescription"),
    path('add_presc<int:pid>', add_presc, name="add_presc"),
    path('add_medical<int:pid>', add_medical, name="add_medical"),
    path('add_bill<int:pid>', add_bill, name="add_bill"),
    path('add_bil<int:pid>', add_bil, name="add_bil"),
    path('delete_presc<int:pid>', delete_presc, name="delete_presc"),
    path('delete_bill<int:pid>', delete_bill, name="delete_bill"),

#Hospital Url
    path('hospital_dashboard', hospital_dashboard, name="hospital_dashboard"),
    path('hospital_profile', Hospital_Profile, name="hospital_profile"),
    path('hospital_change_password', Hospital_Change_Password, name="hospital_change_password"),
    path('hospital_view_appointment', hospital_view_appintment, name="hospital_view_appointment"),
    path('hospital_view_confirmed_appointment', hospital_view_confirmed_appintment,name="hospital_view_confirmed_appointment"),
    path('hospital_view_history_appointment', hospital_view_history_appintment,name="hospital_view_history_appointment"),
    path('hospital_update_status<int:pid>', hospital_update_status, name="hospital_update_status"),
    path('cancel_hospital_appointment<int:pid>', cancel_hospital_appointment, name="cancel_hospital_appointment"),
    path('hospital_search_appointment', hospital_search_appointment, name="hospital_search_appointment"),
    path('patient_search_by_id', patient_search_by_id, name="patient_search_by_id"),
    path('hospital_view_invoices', hospital_view_invoices, name="hospital_view_invoices"),
    path('hospital_status<int:pid>', hospital_status, name="hospital_status"),
    path('hospital_invoices2<int:pid>', hospital_invoices2, name="hospital_invoices2"),
    path('add_price_hospital<int:pid>', add_price_hospital, name="add_price_hospital"),

#Medical Url
    path('medical_dashboard', medical_dashboard,name="medical_dashboard"),
    path('medical_profile', Medical_Profile,name="medical_profile"),
    path('medical_change_password', Medical_Change_Password,name="medical_change_password"),
    path('medical_patient_search_by_id', medical_patient_search_by_id, name="medical_patient_search_by_id"),
    path('medical_invoices<int:pid>', medical_invoices, name="medical_invoices"),
    path('medical_add_medicine<int:pid>', medical_add_medicine, name="medical_add_medicine"),
    path('all_patient_invoices', all_patient_invoices, name="all_patient_invoices"),
    path('medical_status<int:pid>', medical_status, name="medical_status"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)