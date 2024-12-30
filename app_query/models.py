from django.db import models

class Author(models.Model) :
    name = models.CharField(max_length=50) 
    def __str__(self):
        return self.name
    
class Posts(models.Model):
    posts = models.CharField(max_length=300) 
    author=models.ForeignKey(Author,on_delete=models.CASCADE)  
    def __str__(self):
        return f'{self.posts}'  


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False, unique=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name} '

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    price = models.IntegerField(null=False)
    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateField(null=False)
    shipped_date = models.DateField(null=True)
    delivered_date = models.DateField(null=True)
    coupon_code = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    products = models.ManyToManyField(Product, through='LineItem')
    def __str__(self) :
        return f'{self.order_date} {self.customer}'
    def get_products(self,obj):
        return "\n".join([p.name for p in self.name.all()])

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
    def __str__(self):
        return str(self.order)

class Book(models.Model)    :
    bookname = models.CharField(max_length=300)
    price = models.DecimalField(default = 0.0, max_digits=11, decimal_places=2)
    def __str__(self):
        return self.bookname
    
class Store(models.Model):
    store_name = models.CharField(max_length=300)    
    books = models.ManyToManyField('Book')
    
    def __str__(self) :
        return self.store_name
    # def get_books(self,obj):
    #     return "\n".join([b.bookname for b in self.bookname.all()])
class Teacher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Course(models.Model) :
    course = models.CharField(max_length=50)   
    def __str__(self):
        return self.course
    
class Student(models.Model):
    studno= models.CharField(max_length= 20, unique=True)
    firstname = models.CharField(max_length= 50)
    lastname = models.CharField(max_length= 50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null = True, blank=True)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'    
class Classroom(models.Model):
    name = models.CharField(max_length=300)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)

    student = models.ManyToManyField('Student')
    status = models.CharField(max_length=50)
    def __str__(self):
        return f'Classroom  {self.name} '    
    def get_students(self):
        return "\n".join([p.studno for p in self.student.all()])
    

class Task(models.Model):
    owner = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)
    task_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
        