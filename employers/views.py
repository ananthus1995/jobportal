from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView,TemplateView

from django.urls import reverse_lazy
from employers.models import User,Jobs,CompanyProfile
# from django.contrib.auth.forms import User

from employers.forms import Jobforms,SignupForm, SigninForm, CompanyProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class EmployerHome(View):
    def get(self,request):
        return render(request,'emp-home.html')

class EmpAddJob(CreateView):
    model=Jobs
    form_class = Jobforms
    template_name = 'add-job.html'
    success_url = reverse_lazy('addjob')


    def form_valid(self, form):
        messages.success(self.request, 'new job created')
        form.instance.company = self.request.user
        return super().form_valid(form)


#listalljobs
class JobLisView(ListView):
    model=Jobs
    context_object_name = 'jobs'
    template_name = 'emp_job-list.html'
    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user)
    # def get(self,request):
    #     res=Jobs.objects.filter(company=request.user)
    #     return render(request,self.template_name,{'jobs':res})

#detailview

class JobDetailView(DetailView):
    model=Jobs
    template_name = 'emp-job_details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    #
    # def get(self,request,id):
    #     res=Jobs.objects.get(id=id)
    #     return render(request,'emp-job_details.html',{'job':res})





#editjob

class EditView(SuccessMessageMixin,UpdateView):
    model = Jobs
    form_class = Jobforms
    template_name = 'edit-emp_job.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('joblist')
    success_message ='Job Updated Successfully'




    # def get(self,request,id):
    #     res=Jobs.objects.get(id=id)
    #     form=Jobforms(instance=res)
    #     return render(request,'edit-emp_job.html',{'form':form})
    #
    # def post(self,request,id):
    #     res=Jobs.objects.get(id=id)
    #     form=Jobforms(request.POST,instance=res)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('joblist')
    #     else:
    #         return render(request,'edit-emp_job.html',{'form':form})


#deletejob
class DeleteJob(DeleteView,SuccessMessageMixin):
    pk_url_kwarg = 'id'
    model = Jobs
    template_name = 'emp-delete-job.html'
    success_url = reverse_lazy('joblist')



    # def get(self,request,id)

    # return HttpResponse("Data submitted successfully")

class Signup(CreateView):
    model=User
    template_name = 'usersignup.html'
    form_class = SignupForm
    success_url = reverse_lazy('signin')

class Signin(FormView):
    template_name = 'signin.html'
    form_class = SigninForm

    def post(self,request,*args,**kwargs):
        form=SigninForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.role=='employer':
                     return redirect('emp_home')
                elif request.user.role=='candidate':
                    return redirect('cand-joblist')
            else:
                return render(request,self.template_name,{'form':form,'errmsg':'Incorrect username or password'})
        else:
            return render(request,self.template_name,{'form':form,'errmsg':'Incorrect username or password'})
def logout_view(request,*args,**kwargs):
    logout(request)
    return redirect('signout')


#password change
class ChangePassword(TemplateView):
    template_name = 'verifypassword.html'

    def post(self,request,*args,**kwargs):
        password=request.POST.get('pwd')
        uname=request.user
        user=authenticate(request,username=uname,password=password)
        if user:
            return redirect('resetpwd')
        else:
            return render(request,self.template_name,{'ermsg':'Incorrect Password'})


class PasswordReset(TemplateView):
    template_name = 'reset_password.html'

    def post(self,request,*args,**kwargs):
        password1=request.POST.get('pwd1')
        confirm_pwd=request.POST.get('pwd2')
        if password1==confirm_pwd:
            usr=User.objects.get(username=request.user)
            usr.set_password(confirm_pwd)
            usr.save()
            return redirect('signin')
            # return render(request,self.template_name,{'success_msg':'Password Changed Successfully!'})
        else:
            return render(request,self.template_name,{'err_msg':'Password Missmatch'})


class CompanyProfileView(SuccessMessageMixin,CreateView):
    template_name= 'emp-add_companyprofile.html'
    form_class = CompanyProfileForm
    model=CompanyProfile
    success_url = reverse_lazy('emp_profileview')
    success_message = 'Profile Created'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

#employer profile
class EmpProfileView(TemplateView):
    template_name = 'emp-view_profile.html'



#editcompprofile
class EmpEditCompanyProfile(SuccessMessageMixin,UpdateView):
    model=CompanyProfile
    form_class = CompanyProfileForm
    pk_url_kwarg = 'id'
    template_name = 'emp-edit_companyprofile.html'
    success_url = reverse_lazy('emp_profileview')
    success_message = 'Profile Updated'



