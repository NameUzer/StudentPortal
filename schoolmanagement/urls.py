from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),


    path('adminlogin', LoginView.as_view(template_name='school/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='school/studentlogin.html')),
    path('teacherlogin', LoginView.as_view(template_name='school/teacherlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='school/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),


    path('admin-teacher', views.admin_teacher_view,name='admin-teacher'),
    path('admin-add-teacher', views.admin_add_teacher_view,name='admin-add-teacher'),
    path('admin-view-teacher', views.admin_view_teacher_view,name='admin-view-teacher'),
    path('admin-approve-teacher', views.admin_approve_teacher_view,name='admin-approve-teacher'),
    path('approve-teacher/<int:pk>', views.approve_teacher_view,name='approve-teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher_view,name='delete-teacher'),
    path('delete-teacher-from-school/<int:pk>', views.delete_teacher_from_school_view,name='delete-teacher-from-school'),
    path('update-teacher/<int:pk>', views.update_teacher_view,name='update-teacher'),



    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-add-student', views.admin_add_student_view,name='admin-add-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('delete-student-from-school/<int:pk>', views.delete_student_from_school_view,name='delete-student-from-school'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('admin-approve-student', views.admin_approve_student_view,name='admin-approve-student'),
    path('approve-student/<int:pk>', views.approve_student_view,name='approve-student'),
    path('admin-view-student-fee', views.admin_view_student_fee_view,name='admin-view-student-fee'),


    path('admin-attendance', views.admin_attendance_view,name='admin-attendance'),
    path('admin-take-attendance/<str:cl>', views.admin_take_attendance_view,name='admin-take-attendance'),
    path('admin-view-attendance/<str:cl>', views.admin_view_attendance_view,name='admin-view-attendance'),


    path('admin-fee', views.admin_fee_view,name='admin-fee'),
    path('admin-view-fee/<str:cl>', views.admin_view_fee_view,name='admin-view-fee'),

    path('admin-notice', views.admin_notice_view,name='admin-notice'),



    path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
    path('teacher-attendance', views.teacher_attendance_view,name='teacher-attendance'),
    path('teacher-take-attendance/<str:cl>', views.teacher_take_attendance_view,name='teacher-take-attendance'),
    path('teacher-view-attendance/<str:cl>', views.teacher_view_attendance_view,name='teacher-view-attendance'),
    path('teacher-notice', views.teacher_notice_view,name='teacher-notice'),

    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    path('student-attendance', views.student_attendance_view,name='student-attendance'),




    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),

    path('admin_teacher_student_cards', views.admin_teacher_student_card, name= 'cards'),
    path('ForgotPW',views.ForgotPW, name='ForgotPW'),

    path('admin-addbook', views.admin_addbook_view, name='admin-addbook'),
    path('teacher-addbook', views.teacher_addbook_view, name='teacher-addbook'),
    path('admin-viewbook', views.admin_viewbook_view, name='admin-viewbook'),
    path('teacher-viewbook', views.teacher_viewbook_view, name='teacher-viewbook'),
    path('student-viewbook', views.student_viewbook_view, name='student-viewbook'),
    path('issuebook', views.issuebook_view, name='issuebook'),
    path('teacher-issuebook', views.teacher_issuebook_view, name='teacher-issuebook'),
    path('viewissuedbook', views.viewissuedbook_view, name='viewissuedbook'),
    path('teacher-viewissuedbook', views.teacher_viewissuedbook_view, name='teacher-viewissuedbook'),
    path('student-viewissuedbook', views.student_viewissuedbook_view, name='student-viewissuedbook'),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent, name='viewissuedbookbystudent'),

    path('admin=library', views.admin_Library_view,name='admin-library'),
    path('student=library', views.student_Library_view,name='student-library'),
    path('teacher=library', views.teacher_Library_view,name='teacher-library')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
