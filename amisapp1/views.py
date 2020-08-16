from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import userType_table,patientBookAppointment,queryForm,doctor_detail,dawa_category,dawa_add_product,medicin,lab_profile ,lab_reply   
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request,'index.html')
def registration(request):
    context = {}
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        utype = request.POST["utype"]
        password = request.POST["password"]
        usr = User.objects.create_user(username =email,email=email, password=password)
        usr.first_name = fname
        usr.last_name = lname
        if utype=="doctor":
            usr.superuser = True
           
        else:
            usr.is_active = True
        usr.save()
        if utype=="doctor": 
            type = doctor_detail(user=usr)
            type.save()
        if utype == "pharmacist":
            type = dawa_category(user=usr)
            type.save()
        if utype == "lab":
            type = lab_profile(user=usr)
            type.save()
        type = userType_table(user=usr, userType=utype,username=usr.username)
        type.save()
        context["status"] = "Registered Successfully"
        
    return  render(request,'registration.html',context)

def user_login(request):
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["pass"]

        user = authenticate(username=un,password=pwd)
        if user:
            login(request,user)
            data = userType_table.objects.get(user__id=request.user.id)
            print(data.userType)
            if data.userType == "lab":
                return HttpResponseRedirect("/labDashboard")
            elif data.userType == "doctor":
                return HttpResponseRedirect("/doctorDashboard")
            elif data.userType == "pharmacist":
                return HttpResponseRedirect("/pharmacistDashboard")
            else:
                return HttpResponseRedirect("/patientDashboard")        
        else:
            return render(request,"home.html",{"status":"Invalid Username or Password"})

    return render(request,"login.html")


def aboutus(request):
    return render(request,"about.html")

def doctors(request):
    return render(request,"doctors.html")

def check(request):
    return HttpResponse("About check")

def service(request):
    return render(request,"service.html")

def patientDashboard(request):
    return render(request,"patientDashboard.html")

def appointment(request):
    return render(request,"doctors.html")

def covid(request):
    return render(request,"covid.html")

def checkuplist(request):
    return render(request,"profile/checkuplist.html")

def appointmentlist(request):
    return render(request,"profile/appointmentlist.html")
def paymentstatus(request):
    return render(request,"profile/paymentstatus.html")

def labreport(request):
    return render(request,"profile/labreport.html")
def notification(request):
    return render(request,"profile/notification.html")

def learn(request):
    return render(request,"services/learn.html")


def expert(request):
    return render(request,"services/expert.html")

def shop(request):
    context = {}
    data = userType_table.objects.filter(userType="pharmacist")
    context["data"] = data
    print(data)
    return render(request,"services/pharma.html",context)


def tech(request):  
    context = {}
    data = lab_profile.objects.all()
    context["data"] = data
    
    
    
    







    return render(request,"services/lab.html",context)
def appoint(request):
    context = {}
    data2 = doctor_detail.objects.get(user__id=request.user.id)
    data = patientBookAppointment.objects.filter(status=0)
    context["data"] = data
    context["data2"] = data2
    if request.method == "POST":
        status = request.POST["status"]
        id = request.POST["id"]
        data = patientBookAppointment.objects.get(id=id)
        
        data.status = status
        data.save()
    return render(request,"dec-services/appoint.html",context)
def sechtime(request):
    return render(request,"dec-services/sech-time.html")

def invoice(request):
    return render(request,"dec-services/invoice.html")
def invoiceview(request):
    return render(request,"dec-services/invoiceview.html")
def profilesetting(request):
    context = {}
    check = doctor_detail.objects.filter(user__id=request.user.id)
  
    if len(check)>0:
        data = doctor_detail.objects.get(user__id=request.user.id)
        context["data"]=data 
    
    if request.method == "POST":
        phone = request.POST["phone"]
        gender = request.POST["gender"]
        dob = request.POST["dob"]
        about = request.POST["about"]
        clinic_name = request.POST["clinic_name"]
        clinic_address = request.POST["clinic_address"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        city = request.POST["city"]
        state = request.POST["state"]
        country = request.POST["country"]
        pin = request.POST["pin"]
        services = request.POST["services"]
        specialist = request.POST["specialist"]

        data.phone = phone
        data.gender = gender
        data.dob = dob
        data.about = about
        data.clinicInfo = clinic_name
        data.clinicAddress = clinic_address
        data.address1 = address1
        data.address2 = address2
        data.city = city
        data.state = state
        data.pin = pin
        data.service = services
        data.specialization = specialist
        data.save()
      

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()
        context["status"] = "Changs  Successfully"
    return render(request,"dec-services/profilesetting.html",context)

def chat(request):
    context = {}
    data2 = doctor_detail.objects.get(user__id=request.user.id)
    context["data2"] = data2
    

    return render(request,"dec-services/chat.html",context)

def firstpharmastore(request):
    context = {}
    id = request.GET["id"]
    user = User.objects.get(email=id)
    context["user"]=user
    products = dawa_add_product.objects.filter(user=user)
    context["products"]=products
    pin = userType_table.objects.get(user=user)
    print(pin.postal)

    if request.method == "POST":
        
        quantity = request.POST["quantity1"]
        name1 = request.POST["name1"]
        category = request.POST["category1"]
        price = request.POST["price1"]
        patient_name = request.user.first_name
        shop = request.GET["id"]
        user = userType_table.objects.get(user__id=request.user.id)
        data = medicin(name=name1,category=category,price=price,Patient_name=patient_name,shop_name = shop,phone=user.phone,address=user.address,quantity=quantity)
        data.save()
        context["status"] ="Ordered Successfull!"
        
        
    return render(request,"pharma/firstpharmastore.html",context)



def formservice(request):
    context = {}
    data = userType_table.objects.get(user__id=request.user.id)
    data1 = User.objects.get(id=request.user.id)
    context["data"] = data
    context["data1"] = data1
    if "pid" in request.GET:
        pid = request.GET["pid"]
        
        user = lab_profile.objects.get(id=pid)
        context["user"] = user
    if request.method == "POST":
        name = request.POST["fname"]
        address = request.POST["faddress"]
        pin = request.POST["pin"]
        gender = request.POST["gender"]
        purpose = request.POST["purpose"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        user = request.POST["user"]
        print(name,email,purpose)
        usr = queryForm(name=name,address=address,pin=pin,gender=gender,purpose=purpose,email=email,phone=phone,user=user)
        usr.save()
        context["status"] = "query submitted succesfull!"
        return render(request,"profile.html",context)


    return render(request,"services/serviceform.html",context)



def doctorDashboard(request):
    context = {}
    data = patientBookAppointment.objects.filter(status=1)
    context["data"] = data
    data2 = doctor_detail.objects.get(user__id=request.user.id)
    context["data2"] = data2
    return render(request,"doctorDashboard.html",context)

def labDashboard(request):
    context = {}
    data = queryForm.objects.filter(user=request.user.username)
    context["data"] = data
    print(data)
    return render(request,"labDashboard.html",context)

def pharmacistDashboard(request):
    context = {}
    data2 = User.objects.get(id=request.user.id)
    context["data2"] = data2
    data = medicin.objects.filter(shop_name=request.user.username)
    context["data"] = data
    print(data)
    return render(request,"pharamacistDashboard.html",context)

def addproduct(request):
    context = {}
    data2 = User.objects.get(id=request.user.id)
    context["data2"] = data2
    products_category = dawa_category.objects.filter(user=request.user.username)
    context["products_category"]=products_category  
    print(products_category)
    if request.method == "POST":
        data = User.objects.get(id=request.user.id)
        user = data.username
        product_name = request.POST["product_name"]
        category = request.POST["category"]
        price = request.POST["price"]
        quantity = request.POST["quantity"]
        discount = request.POST["discount"]
        descriptions = request.POST["descriptions"]
        data2 = dawa_add_product(user=user,product_name=product_name,category=category,price=price,quantity=quantity,discount=discount,descriptions=descriptions)
        data2.save()
        context["status"] = "Prduct addes Successfull!"
        if "image" in request.FILES:
            img = request.FILES["image"]
            data2.image = img
            data2.save()
    return render(request,"pharma/add-product.html",context)

def products(request):
    context = {}
    products_data = dawa_add_product.objects.filter(user=request.user.username)
    print(products_data )
    context["products_data"]=products_data
    return render(request,"pharma/products.html",context)

def outstock(request):
    return render(request,"pharma/outstock.html")

def purchase(request):
    return render(request,"pharma/purchase.html")

def cat(request):
    context = {}
    products_data = dawa_add_product.objects.filter(user=request.user.username)
    context["products_data"]=products_data
    products_category = dawa_category.objects.filter(user=request.user.username)
    context["products_category"]=products_category  
    print(products_category)
    if request.method == "POST":
        category = request.POST["category"]
        user = User.objects.get(id=request.user.id)
        # data = dawa_category.objects.get(user__id=request.user.id)  
        # usr = User.objects.get(id=request.user.id)
        # data1 = dawa_category(category=category)
        # data.category =  category
        set_user = user.username
        data1 = dawa_category(user = set_user,category=category)
        data1.save()
        
    return render(request,"pharma/categories.html",context)

def report(request):
    return render(request,"pharma/invoice-report.html")

def transaction(request):
    return render(request,"pharma/transactions-list.html")

def order(request):
    return render(request,"pharma/order.html")

def editproduct(request):
    return render(request,"pharma/editproduct.html")

def dawaprofile(request):
    return render(request,"pharma/profile.html")



@login_required
def user_logout(request):
    logout(request)
    res =  HttpResponseRedirect("/user_login")
    res.delete_cookie("user_id")
    res.delete_cookie("date_login")
    return res


def patientAppointmentBook(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name'] 
        doctor_name = request.POST['doctor_name'] 
        problems = request.POST['problems'] 
        phone = request.POST['phone'] 
        date = request.POST['date'] 
        time = request.POST['time'] 
        massege = request.POST['massege'] 
        pic = userType_table.objects.get(user__id=request.user.id)
        profile_pic = pic.profile_pic
        address = pic.address
        email = pic.user
        
        data = patientBookAppointment(name=name,doctor=doctor_name,problems=problems,phone=phone,date=date,massage=massege,time=time,profile_pic = profile_pic,address=address,email=email)
        data.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()

       
        context["status"] = "Appointment Book Successfully"
        return render(request,"patientDashboard.html",context)

@login_required
def profile(request):
    context = {}
    check = userType_table.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = userType_table.objects.get(user__id=request.user.id)
        context["data"]=data 

    if request.method=="POST":
         
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        blood = request.POST["bloodgroup"]
        age = request.POST["age"]
        ct = request.POST["city"]
        country = request.POST["country"]
        postal = request.POST["postalcode"]
        abt = request.POST["about"]
        uname = request.POST["uname"]
        address = request.POST["address"]

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()

        
        data.age = age
        data.city = ct
        data.about = abt
        data.bloodgroup = blood
        data.country = country
        data.username = uname
        data.postal = postal
        data.address = address
        data.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()
        

        context["status"] = "Changes Saved Successfully"
        context["user"] = usr

    return render(request,"profile.html",context)


def delete_product(request):
    context = {}
    
    pid = request.GET["pid"]
    prd = get_object_or_404(dawa_add_product, id=pid)
    context["product"] = prd
    prd.delete()
    context["status"] = str(prd.product_name)+" removed Successfully!!!"
    return HttpResponseRedirect("/products")

    return HttpResponse("deleted")
    

# def medic_order(request):

#     context = {}
#     # pid = request.GET["pid"]
#     # print(pid)
#     # shop_user = dawa_add_product.objects.get(id=pid)
#     # print(shop_user.product_name)
#     # data = patientAppointmentBook(name="nasme")
#     # data = order(name)
#     # data.save()
#     # return HttpResponseRedirect("/products")
#     if "pid" in request.GET:
#         pid = request.GET["pid"]
#         shop_user = dawa_add_product.objects.get(id=pid)
#         print(shop_user.product_name)
#         data = order(name="jak")

#     #     if "action" in request.GET:
#     #         prd.delete()
#     #         context["status"] = str(prd.product_name)+" removed Successfully!!!"
#     return HttpResponse("hello")

def labprof(request):
    return render(request,"labfac/labprof.html")

def ordtable(request):
    return render(request,"labfac/ordtable.html")

def repform(request):
    context = {}
    if "pid" in request.GET:
        user = request.GET["pid"]
        data = queryForm.objects.get(id=user)
        context["data"] = data
    if request.method == "POST":
        user = request.POST["email"]
        phone = request.POST["phone"]
        status = request.POST["status"]
        massage = request.POST["massage"]
        
        data = lab_reply(user=user,phone=phone,status=status,massage=massage)
        data.save()

        if "file" in request.FILES:
            files = request.FILES["file"]
            data.file = files
            data.save()
    return render(request,"labfac/repform.html",context)
    