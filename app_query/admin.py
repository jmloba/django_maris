from django.contrib import admin

# Register your models here.
from app_query.models import Customer,Product,LineItem, Order, Book,Store, Author, Posts, Teacher,Course,Student,Classroom, Task


class CustomerAdmin(admin.ModelAdmin):
  list_display=('first_name','last_name','address','city','postcode','email')
  ordering=('last_name',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class ProductAdmin(admin.ModelAdmin):  
  list_display=('name','price',)
  ordering=('name',)
  list_editable =('price',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()
class OrderAdmin(admin.ModelAdmin):  
  list_display=('order_date','shipped_date','delivered_date','coupon_code','customer','products',)
  ordering=('customer','order_date')
  list_editable =('coupon_code',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()
  
class LineItemAdmin(admin.ModelAdmin):  
  list_display=('order','product','quantity',)
  ordering=('order','product',)
  list_editable =('product','quantity')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  


class BookAdmin(admin.ModelAdmin):  
  list_display=('bookname','price',)
  ordering=('bookname',)
  list_editable =('price',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class StoreAdmin(admin.ModelAdmin):  
  list_display=('store_name','books',)
  ordering=('store_name','books',)
  list_editable =('books',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class AuthorAdmin(admin.ModelAdmin):  
  list_display=('name',)
  ordering=('name',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()  
class PostsAdmin(admin.ModelAdmin):  
  list_display=('posts','author',)
  ordering=('author',)
  list_editable =('author',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class TeacherAdmin(admin.ModelAdmin):  
  list_display=('name',)
  ordering=('name',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()   

class CourseAdmin(admin.ModelAdmin):  
  list_display=('course',)
  ordering=('course',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()   
class StudentAdmin(admin.ModelAdmin):  
  list_display=('studno','firstname','lastname','course')
  ordering=('studno',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class ClassroomAdmin(admin.ModelAdmin):  
  list_display=('name','teacher','status','get_students')
  ordering=('name',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()    

class TaskAdmin(admin.ModelAdmin):  
  list_display=('owner','name','start_time','end_time','created_at', 'updated_at')
  ordering=('name',)
  list_editable =('name','start_time','end_time',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()            

admin.site.register(Task, TaskAdmin)  
admin.site.register(Teacher, TeacherAdmin)  
admin.site.register(Course, CourseAdmin)  
admin.site.register(Student, StudentAdmin)  
admin.site.register(Classroom, ClassroomAdmin)  

admin.site.register(Customer, CustomerAdmin)  
admin.site.register(Product, )  
admin.site.register(Order, )  
admin.site.register(LineItem, )



admin.site.register(Book, )
admin.site.register(Store,)  
admin.site.register(Author,AuthorAdmin )
admin.site.register(Posts,PostsAdmin )  
# admin.site.register(LineItem, LineItemAdmin)  