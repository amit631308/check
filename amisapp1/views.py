from django.shortcuts import render
from django.contrib.auth.models import User
from .models import userType_table,patientBookAppointment,queryForm
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
        if utype=="doctor" or utype=="pharmacist"  or utype=="lab":
            usr.is_staff = True
        else:
            usr.is_active = True
        usr.save()

        type = userType_table(user=usr, userType=utype)
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
    return render(request,"services/pharma.html")


def tech(request):  
    return render(request,"services/lab.html")
def appoint(request):
    return render(request,"dec-services/appoint.html")
def sechtime(request):
    return render(request,"dec-services/sech-time.html")

def invoice(request):
    return render(request,"dec-services/invoice.html")
def invoiceview(request):
    return render(request,"dec-services/invoiceview.html")
def profilesetting(request):
    return render(request,"dec-services/profilesetting.html")

def chat(request):
    return render(request,"dec-services/chat.html")

def firstpharmastore(request):
    return render(request,"pharma/firstpharmastore.html")



def formservice(request):
    context = {}
    data = userType_table.objects.get(user__id=request.user.id)
    data1 = User.objects.get(id=request.user.id)
    context["data"] = data
    context["data1"] = data1
    if request.method == "POST":
        name = request.POST["fname"]
        address = request.POST["faddress"]
        pin = request.POST["pin"]
        gender = request.POST["gender"]
        purpose = request.POST["purpose"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        print(name,email,purpose)
        usr = queryForm(name=name,address=address,pin=pin,gender=gender,purpose=purpose,email=email,phone=phone)
        usr.save()
        context["status"] = "query submitted succesfull!"
        return render(request,"profile.html",context)


    return render(request,"services/serviceform.html",context)



def doctorDashboard(request):
    return render(request,"doctorDashboard.html")

def labDashboard(request):
    return render(request,"labDashboard.html")

def pharmacistDashboard(request):
    return render(request,"pharamacistDashboard.html")

def addproduct(request):
    return render(request,"pharma/add-product.html")

def products(request):
    return render(request,"pharma/products.html")

def outstock(request):
    return render(request,"pharma/outstock.html")

def purchase(request):
    return render(request,"pharma/purchase.html")

def cat(request):
    return render(request,"pharma/categories.html")

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
        data = patientBookAppointment(name=name,doctor=doctor_name,problems=problems,phone=phone,date=date,massage=massege)
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
        

        context["status"] = "Changes Saved Successfully"
        context["user"] = usr

    return render(request,"profile.html",context)