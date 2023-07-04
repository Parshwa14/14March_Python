from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.core.mail import send_mail
from random import *

# Create your views here.


def dashboard(request):

    scount = Student.objects.all().count()
    tcount = Teacher.objects.all().count()
    ccount = Clubs.objects.all().count()
    bcount = Library.objects.all().count()
    context = {
                "scount":scount,
                "tcount":tcount,
                "ccount":ccount,
                "bcount":bcount,
            }
    return render(request,"imsapp/base.html",context)

        

def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        scount = Student.objects.all().count()
        tcount = Teacher.objects.all().count()
        ccount = Clubs.objects.all().count()
        bcount = Library.objects.all().count()
        if uid.role == "Teacher":
            tid = Teacher.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "tid":tid,
                "scount":scount,
                "tcount":tcount,
                "ccount":ccount,
                "bcount":bcount,
            }
            return render(request,"imsapp/index.html",context)

        else:
            sid = Student.objects.get(user_id = uid)
            context={
                "uid":uid,
                "sid":sid,
                "scount":scount,
                "tcount":tcount,
                "ccount":ccount,
                "bcount":bcount,


                }
            return render(request,"imsapp/s_index.html",context)
    else:
        return render(request,"imsapp/login.html")




def register(request):
    if request.POST:
        role = request.POST['role']
        email = request.POST['email']
        plist = ["asdDAA","OKNilm","knnIFN","ad54aa4w","aIyB22"]
        passwrd = request.POST['email'][2:5]+choice(plist)
        uid = User.objects.create(email=email,role = role,password = passwrd)
       
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        
        if request.POST['role'] == Student:
            my_user = Student.objects.create(user_id = uid,firstname=firstname,lastname=lastname)

            my_user.save()
            msg1 = "Registered Successfully, For Password check your mail"
            
            send_mail("Initial Password", "Your automatically generated password is "+ passwrd, "bhavsarparshwa@gmail.com",[email])
            context={
                "msg1":msg1,
            }
            return redirect('login')
                  
        else:
            my_user = Teacher.objects.create(user_id=uid,firstname=firstname,lastname=lastname)

            my_user.save()
            msg1 = "Registered Successfully, For Password check your mail"
            
            send_mail("Initial Passsword", "Your automatically generated password is "+ passwrd, "bhavsarparshwa@gmail.com",[email])
            context={
                "msg1":msg1,
            }
            return redirect('login')    
        
    return render(request,"imsapp/register.html")




def clubs(request):   
    alclub = Clubs.objects.all()
    
    return render(request,"imsapp/clubs.html",{"alclub":alclub})




def login(request):
    
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        if uid.role == "Teacher":
            tid = Teacher.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "tid":tid,
            }
            return render(request,"imsapp/index.html",context)
        else:
            sid = Student.objects.get(user_id=uid)
            context={
                "uid":uid,
                "sid":sid,
            }
            return render(request,"imsapp/s_index.html",context)
            
    else:                                       
        if request.POST:
            print("=====> Login form submitted!")
            p_email = request.POST['email']
            p_password = request.POST['password']
            print("=======",p_email)
            print("========",p_password)
            try:
                print("====>>> ")
                print(User.objects.all())
                uid = User.objects.get(email = p_email)
                
                if uid.password == p_password:
                    
                    if uid.role == "Teacher":
                        tid = Teacher.objects.get(user_id = uid)
                        print("=======>First name = ",tid.firstname)
                        
                        request.session ['email'] = uid.email
                        
                        
                        context = {
                            "uid":uid,
                            "tid":tid,
                        }
                        return render(request,"imsapp/index.html",context)
                    else:
                        sid = Student.objects.get(user_id = uid)
                        request.session ['email'] = uid.email
                        context={
                            "uid":uid,
                            "sid":sid,
                        }
                        return render(request,"imsapp/s_index.html",context)
                        
                else:
                    msg = "INVALID PASSWORD"
                    context ={
                        "msg" : msg,
                    }
                    return render(request,"imsapp/login.html",context)
                    
                        
            except Exception as e:
                print("=================>",e)
                msg = "Invalid email or password"
                context = {
                    "msg" : msg
                }
                return render(request,"imsapp/login.html",context)
        else:
            print("=====> Login page refreshed")
            return render(request,"imsapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,"imsapp/base.html")
    else:
        return render(request,"imsapp/base.html")


def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        if uid.role == "Teacher":
            tid = Teacher.objects.get(user_id=uid)
            context = {
                "uid":uid,
                "tid":tid,
            }
            return render(request,"imsapp/profile.html",context)
    
        else:
            sid = Student.objects.get(user_id=uid)
            context = {
                    "uid":uid,
                    "sid":sid,
                }
            return render(request,"imsapp/s_profile.html",context)    

def library(request):
    blist = Library.objects.all()
    return render(request,"imsapp/library.html",{"blist":blist})

def events(request):
    elist = Events.objects.all()
    return render(request,"imsapp/events.html",{"elist":elist})


def change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        cpassword = request.POST['currentpassword']
        npassword = request.POST['newpassword']
        
        if uid.password == cpassword:
            uid.password = npassword
            uid.save()  # new password updated 
            del request.session['email']
            return render(request,"imsapp/login.html")
        
        else:
            msg = "Both the passwords are different"
            context ={
                        "msg" : msg,
                    }

            return render(request,"imsapp/profile.html",context)


        
    else:
        return render(request,"imsapp/base.html")
    
    
    
    
def update_teacher_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        
        if uid.role == "Teacher":
            tid = Teacher.objects.get(user_id = uid)
            if request.POST:
                tid.firstname = request.POST["firstname"]
                tid.lastname = request.POST["lastname"]
                
                
                if "mypicture" in request.FILES:
                    tid.pic = request.FILES['pic']
                    tid.save()  # details updated
                    context = {
                    'uid' : uid,
                    'tid' : tid
                    
                    }
                    return render(request,"imsapp/profile.html",context)
        else:
            pass
    else:
        return render(request,"imsapp/login.html")
    return render(request,"imsapp/login.html")

def update_student_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        
        if uid.role == "Student":
            sid = Student.objects.get(user_id = uid)
            if request.POST:
                sid.firstname = request.POST["firstname"]
                sid.lastname = request.POST["lastname"]
                sid.address = request.POST["address"]
                
                
                if "mypicture" in request.FILES:
                    sid.pic = request.FILES['pic']
                    sid.save()  # details updated
                    context = {
                    'uid' : uid,
                    'sid' : sid
                    
                    }
                    return render(request,"imsapp/s_profile.html",context)
        else:
            pass
    else:
        return render(request,"imsapp/login.html")
    return render(request,"imsapp/login.html")


def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        if uid.role == "Teacher":
            tid = Teacher.objects.get(user_id = uid)
            context={
                "uid":uid,
                "tid":tid,
            }
            
            return render(request,"imsapp/profile.html",context)
        
def s_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        if uid.role == "Student":
            sid = Student.objects.get(user_id = uid)
            context={
                "uid":uid,
                "sid":sid,
            }
            return render(request,"imsapp/s_profile.html",context)

def student(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        
        if uid.role == "Teacher":
            tid = Teacher.objects.get(user_id = uid)
            sall = Student.objects.all()
            context = {
                'uid': uid,
                'tid': tid,
                'sall':sall,
            }
            return render(request,"imsapp/student.html",context)    
        
        
def teacher(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        if uid.role == "Teacher":
            tid = Teacher.objects.get(user_id=uid)
            tall = Teacher.objects.all().exclude(user_id=uid)
            context={
                'uid':uid,
                'tid':tid,
                'tall':tall,
            }
            return render(request,"imsapp/teacher.html",context)    
        
        
def s_student(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        
        if uid.role=="Student":
            sid = Student.objects.get(user_id = uid)
            sall = Student.objects.all().exclude(user_id = uid)
            context = {
                'uid':uid,
                'sid':sid,
                'sall':sall
            }
            return render(request,"imsapp/s_student.html",context)
    else:
          
        return render(request,"imsapp/s_student.html",context)

        
def s_teacher(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        
        if uid.role == "Student":
            sid = Student.objects.get(user_id = uid)
            tall = Teacher.objects.all()
            context = {
                'uid': uid,
                'sid':sid,
                'tall':tall,
            }
            return render(request,"imsapp/s_teacher.html",context)    
        


def campus(request):
    return render(request,"imsapp/campus.html")



def forgotpassword(request):
    
    if request.POST: 
        email = request.POST['email']
        otp = randint(11111,99999)

        try:
            uid = User.objects.get(email = email)
            uid.otp = otp
            uid.save()
            send_mail("Forgot Password","Your otp is "+str(otp),"bhavsarparshwa@gmail.com",[email])
            context = {
                'email' : email
            }

            return render(request,"imsapp/resetpassword.html",context)
        except:
            context = {
                "emsg" : "Invalid email address"
            }
            return render(request,"imsapp/forgotpassword.html")

    return render(request,"imsapp/forgotpassword.html")


def resetpassword(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
       
        uid = User.objects.get(email = email)
        if str(otp) == otp:
            if newpassword == confirmpassword:
                uid.password = newpassword
                uid.save()
                context = {
                    "email" : email,
                    "smsg" : "Password successfully changed"
                }
                return render(request,"imsapp/login.html",context)
            else:
                emsg = "Invalid password"
                context = {
                    "email" : email,
                    "emsg" : emsg
                }
                return render(request,"imsapp/resetpassword.html",context)
        else:
            emsg = "Invalid Otp"
            context = {
                    "email" : email,
                    "emsg" : emsg
            }
            return render(request,"jobzilla_app/resetpassword.html",context)