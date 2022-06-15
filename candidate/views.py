from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,ListView,DetailView
from candidate.forms import CandidateProfileForm,CandidateProfileEditForm
from candidate.models import CandidateProfile
from django.urls import reverse_lazy
from django.contrib.auth import logout,authenticate,update_session_auth_hash
from employers.models import User,Jobs,Applications
from django.contrib import messages


#candidate home view
class CandidateHomeView(TemplateView):
    template_name = 'candidate/candidatehome.html'



#candidate profilecreation

class CandidateProfileCreate(CreateView):
    model=CandidateProfile
    form_class = CandidateProfileForm
    template_name = 'candidate/cand-add_profile.html'
    success_url = reverse_lazy('cand-home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class CandidateProfileDetailsView(TemplateView):
    template_name = 'candidate/candidate-profile_details.html'



#updating User model and Candidateprofilemodel

class CandidateProfileEdit(FormView):
    model=CandidateProfile
    template_name = 'candidate/cand-profile_edit.html'
    form_class = CandidateProfileEditForm
    def get(self,request,*args,**kwargs):
        profile=CandidateProfile.objects.get(user=request.user)
        form=self.form_class(instance=profile,initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'phone':request.user.phone,
            'email':request.user.email
        })
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        profile = CandidateProfile.objects.get(user=request.user)
        form=self.form_class(instance=profile,data=request.POST,files=request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data.pop('first_name')
            last_name = form.cleaned_data.pop('last_name')
            phone = form.cleaned_data.pop('phone')
            email = form.cleaned_data.pop('email')
            form.save()
            user=User.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            user.phone=phone
            user.email=email
            user.save()
            messages.success(request,'Your Profile Updated')
            return redirect('cand-profileview')
        else:
            messages.error(request,'Error Occured!please try again')
            return render(request,self.template_name,{'form':form})


#joblist
class CandidateJoblistView(ListView):
    model=Jobs
    template_name = 'candidate/joblist.html'
    context_object_name = "jobs"
    def get_queryset(self):
        return self.model.objects.filter(active_status=1).order_by('-created_date')

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     y = Applications.objects.filter(status='applied')
    #     # print(is_applied)
    #     data['x'] = y
    #     print(data)
    #     return data



class CandidateJobDetailsView(DetailView):
    model=Jobs
    context_object_name = 'job'
    template_name = 'candidate/cand-jobdetails.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        is_applied=Applications.objects.filter(applicant=self.request.user,job=self.object)
        context['is_applied']=is_applied
        return context


#candidate application submision
def apply_now(request,*args,**kwargs):
    user=request.user
    job=Jobs.objects.get(id=kwargs.get('id'))
    Applications.objects.create(applicant=user,job=job)
    messages.success(request,'Applied Successfully')
    return redirect('cand-joblist')


class AppliedApplicationListView(ListView):
    template_name = 'candidate/applied-jobs.html'
    model=Applications
    context_object_name = 'myapplicaions'
    def get_queryset(self):
        return self.model.objects.filter(applicant=self.request.user)


class PasswordChangeView(TemplateView):
    template_name = 'candidate/password-reset.html'
    def post(self,request,*args,**kwargs):
        oldpwd=request.POST.get('oldpswd')
        newpwd=request.POST.get('newpswd')
        confrmpwd=request.POST.get('confirmpswd')
        user=authenticate(username=request.user,password=oldpwd)
        if user:
            if newpwd==confrmpwd:
                usr=User.objects.get(username=request.user)
                usr.set_password(confrmpwd)
                usr.save()
                update_session_auth_hash(request,usr)
                # print(update_session_auth_hash)
                messages.success(request, 'New Password Created Successfully')
                return redirect('passwordreset')
            else:
                messages.error(request, 'New and Confirm password missmatch!')
                return redirect('passwordreset')
        else:
            messages.error(request, 'Incorrect Current Password ')
            return redirect('passwordreset')




def logoutview(request,*args,**kwargs):
    logout(request)
    return redirect('signin')




