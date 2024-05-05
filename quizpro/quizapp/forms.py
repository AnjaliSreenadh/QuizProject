# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# class UserCreationForm:
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
# 	def __init__(self, *args, **kwargs):
# 		super(SignUpForm, self).__init__(*args, **kwargs)
# 		self.fields['is_staff'].initial = True
#
#
#
# 	# class SignupForm(forms.ModelForm):
# # 	password=forms.CharField(widget=forms.PasswordInput())
# # 	class Meta:
# # 		model=User
# # 		fields=['username', 'email', 'password']
# 	# def __init__(self,*args, **kwargs):
# 	# 	super(SignupForm,self).__init__(*args, **kwargs)
# 	# 	self.fields['username'].widget.attrs['class']='form-control'
# 	# 	self.fields['username'].widget.attrs['placeholder']=''
# 	# 	self.fields['username'].label='User Name'
# 	# 	self.fields['username'].help_text=None
#
#
#
