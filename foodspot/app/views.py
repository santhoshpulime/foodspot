from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import order_status, order_code_for_user,bookeditem,restaurants_category, order_history,item_details,user_detail,restaurant_details,restaurantcategory
from .forms import  Restaurant_signup_form
from django.http import JsonResponse,HttpResponse
import random
import datetime

## home page
def home(request):

	if restaurant_details.objects.filter(restaurant_name=request.user).exists():
		return redirect('restaurant_home')
	user_location = user_detail.objects.filter(username=request.user).first()
	restaurants = restaurant_details.objects.filter(state=user_location.state,city=user_location.city)
	return render(request,'home.html',{'restaurants':restaurants})

##signup page for user
def signup_user(request):
	if user_detail.objects.filter(username=request.user).exists():
		return redirect('/')
	if request.method == 'POST':
		username = request.POST['username']
		city 	 = request.POST['city']
		state 	 = request.POST['state']
		address  = request.POST['address']
		password = request.POST['password']
		phnnumber= request.POST['phonenumber']		


		if city == '' :
			messages.info(request,'fill the above details')
			return redirect('signup_user')
		if state == '' :
			messages.info(request,'fill the above details')
			return redirect('signup_user')
		if address == '' :
			messages.info(request,'fill the above details')
			return redirect('signup_user')
		if username == '' :
			messages.info(request,'fill the above details')
			return redirect('signup_user')
		if password == '' :
			messages.info(request,'fill the above details')
			return redirect('signup_user')
		if phnnumber == '' :
			messages.info(request,'fill the above details')
			return redirect('signup_user')
		if len(phnnumber)!=10 :
			messages.info(request,'Enter correct phonenumber')
			return redirect('signup_user')
		if User.objects.filter(username=username):
			messages.info(request,'username already exists')
			print('already exists')
			return redirect('signup_user')
		
		else:
			userdata = user_detail.objects.create(username=username,city=city,state=state,address=address,password=password)
			userdata.save()
			
			usersave = User.objects.create_user(username=username,password=password)
			usersave.save()
			return redirect('login_user')
	



			
	return render(request,'signup_user.html')

##login page for user
def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		userdata = auth.authenticate(username=username,password=password)
		if userdata is not None:
			auth.login(request,userdata)
			return redirect('/')
		else:
			messages.info(request,'username and password does not match')
			return redirect('login_user')
	return render(request,'login_user.html')



##restaurant signup page
def restaurant_signup(request):
	form = Restaurant_signup_form()
	if request.method == 'POST':
		restaurant_name = request.POST['restaurant_name']
		city 	 = request.POST['city']
		state 	 = request.POST['state']
		address  = request.POST['address']
		password = request.POST['password']
		phnnumber= request.POST['phonenumber']
		email    = request.POST['email']		
		about_restaurant= request.POST['about']
		logo 	 = request.FILES['logo']



		if city == '' :
			messages.info(request,'fill the above details')
			return redirect('restaurant_signup')
		if state == '' :
			messages.info(request,'fill the above details')
			return redirect('restaurant_signup')
		if address == '' :
			messages.info(request,'fill the above details')
			return redirect('restaurant_signup')
		if restaurant_name == '' :
			messages.info(request,'fill the above details')
			return redirect('restaurant_signup')
		if password == '' :
			messages.info(request,'fill the above details')
			return redirect('restaurant_signup')
		if phnnumber == '' :
			messages.info(request,'fill the above details')
			return redirect('restaurant_signup')
		if len(phnnumber)!=10 :
			messages.info(request,'Enter correct phonenumber')
			return redirect('restaurant_signup')
		if email == '' :
			messages.info(request,'fill the above details')
			return redirect('restaurant_signup')
		if about_restaurant == '' :
			messages.info(request,'fill the above details')
			return redirect('restaurant_signup')

		else:
			data     = restaurant_details(
				restaurant_name=restaurant_name,
				password=password,
				city=city,
				state=state,
				address=address,
				phnnumber=phnnumber,
				email=email,
				logo=logo,
				about_restaurant=about_restaurant)
			
			data.save()
			usersave = User.objects.create_user(username=restaurant_name,password=password)
			usersave.save()		
			return redirect('restaurant_login')

	
	
	return render(request,'restaurant_signup.html',{'form':form})




##restaurant login page
def restaurant_login(request):
	if request.method == 'POST':
		username = request.POST['restaurantname']
		password = request.POST['password']
		userdata = auth.authenticate(username=username,password=password)
		if userdata is not None:
			auth.login(request,userdata)
			return redirect('restaurant_home')
		else:
			messages.info(request,'Restaurnt name and password does not match')
			return redirect('restaurant_login')
	return render(request,'restaurant_login.html')




##restaurant home page
def restaurant_home(request):
	itemorders = bookeditem.objects.all()

	return render(request,'restaurant_home.html',{'itemorders':itemorders})




##add food item restaurant
def restaurant_addproduct(request):
	if request.method == 'POST':
		restaurant_user=request.user
		category_item = request.POST['category']
		category_item_img = request.FILES['category_img']
		data = restaurants_category(restaurant_user=restaurant_user,category_item=category_item,category_item_img=category_item_img,user_id=request.user.id)
		data.save()
		print(restaurants_category.id)
	
		return redirect('restaurant_addproduct')
	

	return render(request,'restaurant_addproduct.html')

##showing categories to restaurant user using ajax -- ajax
def show_category(request):
	if request.method == 'POST':
		category_items = restaurants_category.objects.filter(restaurant_user=request.user)
		print(category_items)
		return JsonResponse({'category_items':list(category_items.values())})


##deleting category in category list -- ajax
def delete_category(request):
	if request.method == 'POST':
		id = request.POST.get('btn')
		pi = restaurants_category.objects.get(pk=id)
		pi.delete()
		print('product deleted')
		return JsonResponse({'status':1})
	else:
		return JsonResponse({'status':0})



##add product or item through ajax -- ajax
def add_item(request):
	
	if request.method == 'POST':
		restaurant_name = request.user
		item_name       = request.POST.get('item_name')
		item_cost       = request.POST.get('item_cost')
		item_category       = request.POST.get('item_category')
		about_item   	= request.POST.get('about_item')
		datasave        = item_details(
			restaurant_user=restaurant_name,
			itemname=item_name,
			itemcost=item_cost,
			itemcategory=item_category,
			aboutitem=about_item,
			user_id=request.user.id)
		datasave.save()

		return JsonResponse({'status':'saved'})

	return JsonResponse({'status':'add_item_def'})

##show items to restaurant -- ajax
def show_items_to_restaurant(request):
	if request.method == 'POST':
		btn = request.POST.get('btn')
		items = item_details.objects.filter(
			user_id=request.user.id,
			itemcategory = btn
			)
		print(items)
		return JsonResponse({'status':'showing..','items':list(items.values())})
	return JsonResponse({'status':'show_items_to_restaurant'})



##showing restaurant details page to user
def user_to_restaurant_details(request,id):
	rid = restaurant_details.objects.get(id=id)


	category_items = restaurants_category.objects.filter(restaurant_user=rid.restaurant_name)
	return render(request,'user_to_restaurant_details.html',
		{
		'restaurant_name':rid.restaurant_name,
		'restaurant_categories':category_items,
		'rid':rid
		})


##showing restaurant category items like drinks,pizzas to user 
def user_to_restaurant_category_details_ajax(request):
	if request.method == 'POST':
		r = request.POST.get('rid_id')
		
		rid = restaurant_details.objects.get(id=r)
		


		category_items = restaurants_category.objects.filter(restaurant_user=rid.restaurant_name)
		return JsonResponse({'restaurant_categories':list(category_items.values())})























#####################################bookitems view




def bookitems(request,id):
	cid = restaurants_category.objects.get(id=id)
	print(cid.restaurant_user)
	print(cid.category_item)
	items = item_details.objects.filter(restaurant_user=cid.restaurant_user,itemcategory=cid.category_item)
	if order_code_for_user.objects.filter(username=request.user).exists():
		print('existed')

		return render(request,'bookitems.html',{'order_code':'existed','cid':cid,
		'name':cid.restaurant_user,
		'items':items,})
	else:
		print('no sorry')
		return render(request,'bookitems.html',{'order_code':'notexisted','cid':cid,
		'name':cid.restaurant_user,
		'items':items,})

	return render(request,'bookitems.html',{
		'cid':cid,
		'name':cid.restaurant_user,
		'items':items,
		
		})




def bookitems_ajax(request):
	c_id = request.POST.get('cid')
	cid = restaurants_category.objects.get(id=c_id)

	items = item_details.objects.filter(restaurant_user=cid.restaurant_user,itemcategory=cid.category_item)

	return JsonResponse({'status':"ok",'items':list(items.values())})

def excecute_order(request) :
	if request.method == 'POST':
		btnid = request.POST.get('btnid')
		print(btnid)
		item	 = item_details.objects.get(id=btnid)
		item_filter = item_details.objects.filter(id=btnid)
		#data = bookeditem(username=request.user,user_id=request.user.id,item_id=item.id,item_name=item.itemname,item_cost=item.itemcost,itemcategory=item.itemcategory,aboutitem=item.aboutitem)
		#data.save()
		print(item_filter)
	return JsonResponse({'status':'ok','item_filter':list(item_filter.values())})



def totalcost_display_for_item(request):
	btnid = request.POST.get('btnid')
	itemquantity = request.POST.get('itemquantity')
	item	 = item_details.objects.get(id=btnid)
	if itemquantity=='':
		itecmquantity='1'
		cost = int(itemquantity)*int(item.itemcost)
	
	else:
		cost = int(itemquantity)*int(item.itemcost)

		print(cost)

	return JsonResponse({'status':'ok','cost':cost})


###################show orders to restaurant

def show_orders_ajax(request):
	
	orders =  bookeditem.objects.all().order_by('username')

	data = order_code_for_user.objects.get(username=request.user)

	finalbill= request.POST.get('totalbill')
	addcost = bookeditem.objects.filter(code=data.code)
	for i in addcost:
		print(i.code,i.item_name)
		add_data = bookeditem(id=i.id,
			username=i.username,
			user_id=request.user.id,
			item_id=i.item_id,
			item_name=i.item_name,
			item_cost=i.item_cost,
			itemcategory=i.itemcategory,
			aboutitem=i.aboutitem,
			something=i.something,
			totalcost=i.totalcost,
			code=i.code,
			finalbill=finalbill,
			DateTimeField=datetime.datetime.now(),
			accepted='order sent to restaurant')
		add_data.save()
	data.delete()


	return JsonResponse({'itemorders':list(orders.values()),'bill':'finalbill'})










############################add to cart 



def addtocart(request):
	btnid = request.POST.get('btnid')
	itemquantity = request.POST.get('itemquantity')
	item	 = item_details.objects.get(id=btnid)
	if itemquantity=='':
		itemquantity='1'
		cost = int(itemquantity)*int(item.itemcost)
	
	else:
		cost = int(itemquantity)*int(item.itemcost)

		print(cost)

	##getting code 
	usercode = order_code_for_user.objects.get(username=request.user)
	print(usercode.code)
	data = bookeditem(username=request.user,
		user_id=request.user.id,
		item_id=item.id,
		item_name=item.itemname,
		item_cost=item.itemcost,
		itemcategory=item.itemcategory,
		aboutitem=item.aboutitem,
		something=itemquantity,
		totalcost=cost,
		code = usercode.code
		)

	data.save()

	history = order_history(username=request.user,
		user_id=request.user.id,
		item_id=item.id,
		item_name=item.itemname,
		item_cost=item.itemcost,
		itemcategory=item.itemcategory,
		aboutitem=item.aboutitem,
		something=itemquantity,
		totalcost=cost,
		code=usercode.code)
	history.save()

	print('data saved')




	return JsonResponse({'status':'ok'})


def cart(request):
	orders = bookeditem.objects.filter(username=request.user)
	
	

	return render(request,'cart.html')


##############cart ajax
def cart_ajax(request):
	order_code = order_code_for_user.objects.get(username=request.user)
	orders = bookeditem.objects.filter(username=request.user,code=order_code.code)
	a = []
	total=0
	for i in orders:
		a.append(i.totalcost)
	print('list=',a)

	for l in range(0,len(a)):
		
		total = total+int(a[l])

	finalbill = total+20
	user_name = User.objects.get(username=request.user)
	print(user_name.username)

	return JsonResponse({
		'orders':list(orders.values()),
		'total':finalbill,
		'username':user_name.username
		})
###############delete item in restaurant page

def deleteitem(request):
	btn = request.POST.get('btn')
	item = item_details.objects.get(id=btn)
	item.delete()
	return JsonResponse({'status':'deleted'})

#########delete booked item
def deletebookeditem(request):
	btn = request.POST.get('btn')
	item = bookeditem.objects.get(id=btn)
	item.delete()
	return JsonResponse({'status':'deleted'})


def history(request):
	orders = bookeditem.objects.filter(username=request.user).order_by('code')

	return render(request,'orders_history.html',{'orders':orders})









###############################  creating order code

def ordercode(request):
	random_code = random.randint(1,10000)
	data = order_code_for_user(username=request.user,code=random_code)
	data.save()
	return JsonResponse({'status':'code saved'})













#########################showing orders to restaurant
def show_orders_to_restaurant(request):
	orders = bookeditem.objects.filter(accepted='order sent to restaurant').order_by('code')
	return JsonResponse({'itemorders':list(orders.values())})



#################################order confirmed by restaurant
def confirmorder_restaurant_ajax(request):

	btn = request.POST.get('btn')
	i = bookeditem.objects.get(id=btn)
	add_data = bookeditem(id=i.id,
			username=i.username,
			user_id=request.user.id,
			item_id=i.item_id,
			item_name=i.item_name,
			item_cost=i.item_cost,
			itemcategory=i.itemcategory,
			aboutitem=i.aboutitem,
			something=i.something,
			totalcost=i.totalcost,
			code=i.code,
			finalbill=i.finalbill,
			DateTimeField=datetime.datetime.now(),
			accepted='order sent to restaurant',
			confirmorder_by_restaurant='order confirmed')
	add_data.save()
	

	history = order_history(id=i.id,
			username=i.username,
			user_id=request.user.id,
			item_id=i.item_id,
			item_name=i.item_name,
			item_cost=i.item_cost,
			itemcategory=i.itemcategory,
			aboutitem=i.aboutitem,
			something=i.something,
			totalcost=i.totalcost,
			code=i.code,
			finalbill=i.finalbill,
			DateTimeField=datetime.datetime.now(),
			accepted='order sent to restaurant',
			confirmorder_by_restaurant='order confirmed')
	history.save()

	return JsonResponse({'status':'ok'})






	#################################ordered item not available by user
def item_not_yet_ajax(request):

	btn = request.POST.get('btn')
	i = bookeditem.objects.get(id=btn)
	add_data = bookeditem(id=i.id,
			username=i.username,
			user_id=request.user.id,
			item_id=i.item_id,
			item_name=i.item_name,
			item_cost=i.item_cost,
			itemcategory=i.itemcategory,
			aboutitem=i.aboutitem,
			something=i.something,
			totalcost=i.totalcost,
			code=i.code,
			finalbill=i.finalbill,
			DateTimeField=datetime.datetime.now(),
			accepted='order sent to restaurant',
			confirmorder_by_restaurant='item not available')
	add_data.save()
	

	history = order_history(id=i.id,
			username=i.username,
			user_id=request.user.id,
			item_id=i.item_id,
			item_name=i.item_name,
			item_cost=i.item_cost,
			itemcategory=i.itemcategory,
			aboutitem=i.aboutitem,
			something=i.something,
			totalcost=i.totalcost,
			code=i.code,
			finalbill=i.finalbill,
			DateTimeField=datetime.datetime.now(),
			accepted='order sent to restaurant',
			confirmorder_by_restaurant='item not available')
	history.save()
	return JsonResponse({'status':'ok'})



def order_rejected_ajax(request):

	btn = request.POST.get('btn')
	i = bookeditem.objects.get(id=btn)
	add_data = bookeditem(id=i.id,
			username=i.username,
			user_id=request.user.id,
			item_id=i.item_id,
			item_name=i.item_name,
			item_cost=i.item_cost,
			itemcategory=i.itemcategory,
			aboutitem=i.aboutitem,
			something=i.something,
			totalcost=i.totalcost,
			code=i.code,
			finalbill=i.finalbill,
			DateTimeField=datetime.datetime.now(),
			accepted='order sent to restaurant',
			confirmorder_by_restaurant='sorry your order rejected')
	add_data.save()
	

	history = order_history(id=i.id,
			username=i.username,
			user_id=request.user.id,
			item_id=i.item_id,
			item_name=i.item_name,
			item_cost=i.item_cost,
			itemcategory=i.itemcategory,
			aboutitem=i.aboutitem,
			something=i.something,
			totalcost=i.totalcost,
			code=i.code,
			finalbill=i.finalbill,
			DateTimeField=datetime.datetime.now(),
			accepted='order sent to restaurant',
			confirmorder_by_restaurant='item not available')
	history.save()
	return JsonResponse({'status':'ok'})






	################## search item 



def searchitem(request):
	search = request.POST.get('search')
	search_data = bookeditem.objects.filter(accepted='order sent to restaurant',code__contains=search).order_by('code')
	return JsonResponse({'itemorders':list(search_data.values())})

 

#################### profile page of restaurant

def restaurant_profile(request):

	username = request.user
	restaurant = restaurant_details.objects.get(restaurant_name=username)
	if request.method == 'POST':
		state = request.POST['state']
		city  = request.POST['city']
		address = request.POST['address']
		phonenumber = request.POST['phonenumber']
		email  = request.POST['email']
		aboutrestaurant = request.POST['about_restaurant']
		data = restaurant_details(id=restaurant.id,restaurant_name=restaurant.restaurant_name,password=restaurant.password,state=state,
			city=city,
			address=address,
			phnnumber=phonenumber,
			email=email,
			about_restaurant=aboutrestaurant,
			logo=restaurant.logo,
			date=datetime.datetime.now()
			)
		data.save()
		print('saved')
	return render(request,'restaurant_profile.html',{'r_data':restaurant})



def userprofile(request):
	username = request.user
	user_details = user_detail.objects.get(username=username)
	uid = user_detail.objects.get(username=username)
	if request.method == 'POST':
		state = request.POST['state']
		city = request.POST['city']
		address = request.POST['address']
		phn = request.POST['phonenumber']
		data = user_detail(id=user_details.id,username=user_details.username,password=user_details.password,state=state,city=city,
			address=address,phnnumber=phn)
		data.save()

	return render(request,'userprofile.html',{'user_details':user_details})



def restaurant_status(request):
	return JsonResponse({'status':'ok'})