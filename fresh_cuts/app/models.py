from django.db import models

# Create your models here.

class Register(models.Model):
    Email = models.EmailField(unique=True)
    name = models.TextField()
    phonenumber = models.IntegerField()
    password = models.TextField()
    location= models.TextField()

    def _str_(self):
        return self.name

class Shopreg(models.Model):
    Email = models.EmailField(unique=True)
    name = models.TextField()
    phonenumber = models.IntegerField()
    password = models.TextField()
    location= models.TextField()
    # image = models.FileField()


    def _str_(self):
        return self.name
    
class Category(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    shop = models.ForeignKey(Shopreg,on_delete=models.CASCADE)
    name = models.TextField()
    discription = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.TextField()
    offerprice = models.IntegerField()
    image = models.FileField()

    def _str_(self):
        return self.name +' '+self.shop.name
    
class cart(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def _str_(self):
        return self.user.name +' '+self.product.name
    
    def total_price(self):
        return self.quantity * self.product.price
    
class Buy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_of_buying = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # New field for delivery status
    DELIVERY_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("In Transit", "In Transit"),
        ("Delivered", "Delivered"),
    ]
    delivery_status = models.CharField(
        max_length=20, choices=DELIVERY_STATUS_CHOICES, default="Pending"
    )

    # Optional: define a string representation for clarity in admin
    def __str__(self):
        return f"{self.product.name} - {self.delivery_status}"
    
class Product_quantity(models.Model):
    productid = models.IntegerField()
    shopid = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.productid
    

class Payment_status(models.Model):
        transactionid = models.IntegerField()
        amount = models.IntegerField()

class delivery(models.Model):
    rout = models.TextField()
    Email =  models.EmailField(unique=True)
    password = models.IntegerField()
    name = models.TextField()
    phonenumber = models.IntegerField()
    def __str__(self):
        return self.name

class delpro(models.Model):
    delivery=models.ForeignKey(delivery,on_delete=models.CASCADE)
    buy=models.ForeignKey(Buy,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    date=models.TextField(null=True) 



    

