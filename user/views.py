from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,View
from django.contrib import messages
from user.models import Profile
from django.views.generic.edit import UpdateView
from user.customforms import ProfileModelForm
# Create your views here.

class UserLoginView(TemplateView):
    template_name = 'user/login.html'
    title = 'login'
    success_url = reverse_lazy('todos:home')
    def get(self,request):
        form = AuthenticationForm()
        return render(request,self.template_name,{'title':self.title.capitalize(),'forms':form})
    
    def post(self,request):
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(self.success_url)
        messages.error(request,'Invalid username or password')
        return render(request,self.template_name,{'title':self.title.capitalize(),'forms':form})

class RegisterUserView(View):
    template_name = 'user/register.html'
    title = 'SignUp'
    def get(self,request):
        form = UserCreationForm()
        return render(request,self.template_name,{'title':self.title,'form':form})
    
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse_lazy('todos:home'))
        return render(request,self.template_name,{'title':self.title,'form':form})

class LogoutView(LoginRequiredMixin,View):
    def get(self,request):    
        logout(request)
        messages.info(request,'You have been logged out successfully!')
        return redirect('users:login')


class ProfileView(LoginRequiredMixin,View):
    template_name = 'user/profile.html'
    title = 'Profile'
    def get(self,request):
        profile_count = Profile.objects.filter(user_id=request.user).count()
        if profile_count != 0:
            profile = Profile.objects.get(user_id=request.user.id)
            return render(request,self.template_name,{'title':self.title,'profile':profile})
        messages.warning(request,'Please Create your Profile')
        profile = ProfileModelForm()
        template = 'user/profile_create.html'
        return render(request,template,{'title':self.title,'form':profile})
    
    def post(self,request):
        form = ProfileModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            messages.info(request,'Profile updated successfully')
            return redirect('users:profile')
        messages.error(request,'something went wrong!')
        return render(request,self.template_name,{'title':self.title,'form':form})

class ProfileEditView(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = [
            'profile_image',
            'first_name',
            'last_name',
            'gender',
            'address',
            'city',
            'pincode',
        ]
    template_name = 'user/profile_update.html'
    success_url = reverse_lazy('users:profile')