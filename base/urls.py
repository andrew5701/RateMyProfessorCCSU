from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.conf import settings


urlpatterns = [
     path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
    path('', views.base, name="home"), #home url
    path('findProfessors/', views.find_professors, name="findProfessors"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('allProfessors/', views.all_professors, name="allProfessors"),
    path('myReviews/', views.my_reviews, name="myReviews"),
    path('profile/', views.profile, name="profile"),
    path('testForm/', views.test_form, name="testForm"),
    path('jasonHome/', views.jason_home, name="jasonHome"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('profpage/<int:professor_id>', views.professor_view, name='professorview'),
    path('add_review/<int:professor_id>/<int:user_id>', views.add_review, name='addreview'),
    path('update/<int:review_id>/<int:professor_id>', views.update, name='update'),
    path('delete/<int:review_id>', views.delete, name='delete'),
    path('departments/', views.departments, name='departments'),
    path('departmentProfessors/<int:department_id>', views.department_professors, name='departmentpr'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
