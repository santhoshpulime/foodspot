from django.db import models
from django.contrib.auth.models import User,auth




class user_detail(models.Model):
	username = models.TextField()
	password = models.TextField()
	state    = models.TextField()
	city	 = models.TextField()
	address  = models.TextField()
	phnnumber= models.TextField()

class restaurant_details(models.Model):
	restaurant_name = models.TextField()
	password = models.TextField()
	state    = models.TextField()
	city	 = models.TextField()
	address  = models.TextField()
	phnnumber= models.TextField()
	email    = models.TextField()	
	logo     = models.ImageField(upload_to='images/',blank=True)
	about_restaurant = models.TextField()
	date = models.DateTimeField(auto_now_add=True)




class restaurantcategory(models.Model):
	restaurant_user = models.ForeignKey(User,on_delete=models.CASCADE)
	category_item = models.TextField()
	category_item_img = models.ImageField(upload_to='images/',blank=True)
	date = models.DateTimeField(auto_now_add=True)
	user_id 		= models.TextField()
	

class item_details(models.Model):
	restaurant_user = models.TextField()
	itemname        = models.TextField()
	itemcost        = models.TextField()
	itemcategory    = models.TextField()
	aboutitem       = models.TextField()
	user_id 		= models.TextField()




class restaurants_category(models.Model):
	restaurant_user = models.TextField()
	category_item = models.TextField()
	category_item_img = models.ImageField(upload_to='images/',blank=True)
	date = models.DateTimeField(auto_now_add=True)
	user_id 		= models.TextField()


class bookeditem(models.Model):
	username = models.TextField()
	user_id  = models.TextField(blank=True)
	item_id  = models.TextField(blank=True)
	item_name=models.TextField(blank=True)
	item_cost=models.TextField(blank=True)
	itemcategory=models.TextField(blank=True)
	aboutitem=models.TextField(blank=True)
	DateTimeField=models.DateTimeField(auto_now_add=True)
	something=models.TextField(blank=True)
	totalcost =models.TextField(blank=True)
	code = models.TextField(blank=True)
	finalbill = models.TextField(blank=True)
	accepted = models.TextField(blank=True)
	confirmorder_by_restaurant = models.TextField(blank=True)
	item_not_yet = models.TextField(blank=True)
	order_rejected = models.TextField(blank=True)

class order_history(models.Model):
	username = models.TextField()
	user_id  = models.TextField(blank=True)
	item_id  = models.TextField(blank=True)
	item_name=models.TextField(blank=True)
	item_cost=models.TextField(blank=True)
	itemcategory=models.TextField(blank=True)
	aboutitem=models.TextField(blank=True)
	DateTimeField=models.DateTimeField(auto_now_add=True)
	something=models.TextField(blank=True)
	totalcost =models.TextField(blank=True)
	code = models.TextField(blank=True)
	finalbill = models.TextField(blank=True)
	accepted = models.TextField(blank=True)
	confirmorder_by_restaurant = models.TextField(blank=True)
	item_not_yet = models.TextField(blank=True)
	order_rejected = models.TextField(blank=True)

class order_code_for_user(models.Model):
	username = models.TextField(blank=True)
	code = models.TextField(blank=True)
	additional = models.TextField(blank=True)

class order_status(models.Model):

	confirmorder_by_restaurant = models.TextField(blank=True)
	item_not_yet = models.TextField(blank=True)
	order_rejected = models.TextField(blank=True)
	item_id = models.TextField(blank=True)



class restaurant_status(models.Model):
	restaurant_id = models.TextField(blank=True)
	restaurant_name = models.TextField(blank=True)
	status = models.TextField(blank=True)