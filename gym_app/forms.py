from django import forms
from gym_app.models import *
from django.db.models import Q




class EnquryAddForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        exclude = ['added_by','follow_up_status']

        widgets = {
            'date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'place' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'memebership_plan': forms.Select(attrs={'class':'form-control'}),
            'expected_join_date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'note' : forms.Textarea(attrs={'class':'form-control','rows':3}),
        }

class EnquryFollowupEditForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        exclude = ['added_by']

        widgets = {
            'date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'place' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'memebership_plan': forms.Select(attrs={'class':'form-control'}),
            'expected_join_date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'follow_up_status': forms.Select(attrs={'class':'form-control'}),
            'note' : forms.Textarea(attrs={'class':'form-control','rows':3}),
        }





class EquipmentAddForm(forms.ModelForm):
    class Meta:
        model = Equipements
        fields = '__all__'
        exclude = ['added_by']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Product name'}),
            'img' : forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Photo'}),
            'desc' : forms.Textarea(attrs={'class':'form-control','placeholder':'Product description','rows':'2'}),
            'count' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the count'}),

        }

class MemberEditForm(forms.ModelForm):
    disease = forms.BooleanField(required=False)
    gst = forms.BooleanField(required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = ExtendedUserModel
        fields = "__all__"
        exclude = ['email_sent_status','added_by','role','user','pending_amount','gst_amount','attendance_id','membership_expiry_status','email_sent_status_pending_payment']
        widgets = {
                    'full_name': forms.TextInput(attrs={'class':'form-control'}),
                    'age' : forms.NumberInput(attrs={'class':'form-control'}),
                    'phone' :forms.NumberInput(attrs={'class':'form-control'}),
                    'profile_pic' : forms.ClearableFileInput(attrs={'class':'form-control'}),
                    'dob' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'height' :  forms.NumberInput(attrs={'class':'form-control'}),
                    'weight' :  forms.NumberInput(attrs={'class':'form-control'}),
                    'address' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
                    'gender' : forms.Select(attrs={'class':'form-control'}),
                    'preferred_time_slot' : forms.Select(attrs={'class':'form-control'}),
                    'disease_details' : forms.TextInput(attrs={'class':'form-control'}),
                    'additional_info' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
                    'blood_group': forms.Select(attrs={'class':'form-control'}),
                    'status' : forms.Select(attrs={'class':'form-control'}),
                    'id_prooff': forms.Select(attrs={'class':'form-control'}),
                    'id_proof_imagee' : forms.ClearableFileInput(attrs={'class':'form-control'}),
                    'fitness_goal': forms.Select(attrs={'class':'form-control'}),
                    'membership_plan': forms.Select(attrs={'class':'form-control'}),
                    'join_date': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'expiry_date': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'payment_mode': forms.Select(attrs={'class':'form-control'}),
                    'discount' :  forms.NumberInput(attrs={'class':'form-control'}),
                    'admission_date': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'balance_due_date': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'total_paid_amount' : forms.NumberInput(attrs={'class':'form-control'}),
                    'add_on_plan' : forms.TextInput(attrs={'class':'form-control','placeholder':'Add on plan name'}),
                    # 'add_on_plan_price' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Add on plan price'}),
                    


                    
                    # 'email' :forms.TextInput(attrs={'class':'form-control'}),
        }
    
class TrainerEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = ExtendedUserModel
        fields = ['id_prooff','id_proof_imagee','certificate_photo','profile_pic','full_name','age','phone','dob','address','gender','preferred_time_slot','trainer_work_experience','status']
        # exclude = ['add_on_plan','admission_date','discount', 'user','added_by','role','height','weight','blood_group','id_prooff','id_proof_imagee','disease','gst','disease_details','additional_info','fitness_goal','membership_plan','join_date','expiry_date','amount_paid','pending_amount','total_paid_amount','gst_amount']
        widgets = {
                    'full_name': forms.TextInput(attrs={'class':'form-control'}),
                    'age' : forms.NumberInput(attrs={'class':'form-control'}),
                    'phone' :forms.NumberInput(attrs={'class':'form-control'}),
                    'dob' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'address' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
                    'gender' : forms.Select(attrs={'class':'form-control'}),
                    'preferred_time_slot' : forms.Select(attrs={'class':'form-control'}),            
                    'trainer_work_experience' : forms.TextInput(attrs={'class': 'form-control'}),
                    'profile_pic' : forms.ClearableFileInput(attrs={'class':'form-control'}),
                    'certificate_photo': forms.ClearableFileInput(attrs={'class':'form-control'}),
                    'id_prooff' : forms.Select(attrs={'class':'form-control'}),
                    'id_proof_imagee' : forms.ClearableFileInput(attrs={'class':'form-control'}),
                    'status' : forms.Select(attrs={'class':'form-control'})      

        }



class ReceptionistEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ExtendedUserModel
        fields = ['full_name','phone','status','id_prooff','id_proof_imagee']
        widgets = {
                    'full_name': forms.TextInput(attrs={'class':'form-control'}),
                    'phone' :forms.NumberInput(attrs={'class':'form-control'}),
                    'id_prooff' : forms.Select(attrs={'class':'form-control'}),
                    'id_proof_imagee' : forms.ClearableFileInput(attrs={'class':'form-control'}),
                    'status' : forms.Select(attrs={'class':'form-control'}),


        }








class PendingPaymentEditForm(forms.ModelForm):

    class Meta:
        model = ExtendedUserModel

        fields = [ 'amount_paid' ]
        
        widgets = {
            
            
            'amount_paid' : forms.NumberInput(attrs={'class':'form-control'}),

        }
    def save(self, commit=True):
        instance = super(PendingPaymentEditForm, self).save(commit=False)

        if commit:
            if instance.amount_paid:
                instance.total_paid_amount += instance.amount_paid
                instance.save()

        return instance
    





# class MemberEditForm(forms.ModelForm):
#     disease = forms.BooleanField(required=False)

#     class Meta:
#         model = ExtendedUserModel
#         fields = "__all__"
#         exclude = [ 'user' , 'added_by', 'role']
#         widgets = {
#                     'full_name': forms.TextInput(attrs={'class':'form-control'}),
#                     'age' : forms.NumberInput(attrs={'class':'form-control'}),
#                     'phone' :forms.NumberInput(attrs={'class':'form-control'}),
#                     'dob' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
#                     'height' :  forms.NumberInput(attrs={'class':'form-control'}),
#                     'weight' :  forms.NumberInput(attrs={'class':'form-control'}),
#                     'address' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
#                     'gender' : forms.Select(attrs={'class':'form-control'}),
#                     'preferred_time_slot' : forms.Select(attrs={'class':'form-control'}),
#                     'disease_details' : forms.TextInput(attrs={'class':'form-control'}),
#                     'additional_info' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
#                     'blood_group': forms.Select(attrs={'class':'form-control'}),
#                     'status' : forms.Select(attrs={'class':'form-control'})
#                     # 'email' :forms.TextInput(attrs={'class':'form-control'}),
#         }




class AssignTrainerForm(forms.ModelForm):
    trainer = forms.ModelChoiceField(queryset=ExtendedUserModel.objects.none(), required=False)

    class Meta:
        model = AssignTrainer

        fields = "__all__"
        exclude = ['member','exp_date','pending_amount','total_paid_amount']
        widgets = {
            
            'membership_plan':forms.Select(attrs={'class':'form-control'}),
            # 'trainer' : forms.Select(attrs={'class':'form-control','required':'True'}),
            'join_date':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'Iinitaial_amount' : forms.NumberInput(attrs={'class':'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        added_by = kwargs.pop('added_by')
        busines_usr = kwargs.pop('busines_usr')

        super(AssignTrainerForm, self).__init__(*args, **kwargs)
        self.fields['trainer'].queryset = ExtendedUserModel.objects.filter(role__name='Fitness Trainer', added_by__user=added_by)
        self.fields['membership_plan'].queryset = MembershipPlan.objects.filter(added_by=busines_usr)


        
# class AttendancesForm(forms.ModelForm):
#     member = forms.ModelChoiceField(queryset=ExtendedUserModel.objects.none())
#     class Meta:
#         model = Attendances
#         fields = '__all__'
#         exclude = ['attendance_date','status']
#         widgets = {
#             'status' : forms.Select(attrs={'class':'form-control'})

    
#         }
#     def __init__(self, *args, **kwargs):
#         added_by = kwargs.pop('added_by')
#         super(AttendancesForm, self).__init__(*args, **kwargs)
#         self.fields['member'].queryset = ExtendedUserModel.objects.filter(role__name='Fitness Trainer', added_by__user=added_by,status__name = 'Active')


# class AttendancesEditForm(forms.ModelForm):
#     class Meta:
#         model = Attendances
#         fields = ['status']
#         widgets = {
#             'attendance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }
    


# class MemberAttendancesForm(forms.ModelForm):
#     member = forms.ModelChoiceField(queryset=ExtendedUserModel.objects.none())
#     class Meta:
#         model = Attendances
#         fields = '__all__'
#         exclude = ['attendance_date']
#         widgets = {
#             'status' : forms.Select(attrs={'class':'form-control'})
#         }
#     def __init__(self, *args, **kwargs):
#         added_by = kwargs.pop('added_by')
#         super(MemberAttendancesForm, self).__init__(*args, **kwargs)
#         self.fields['member'].queryset = ExtendedUserModel.objects.filter(role__name='Customer', added_by__user=added_by,status__name = 'Active')


class TrainerProfileAddform(forms.ModelForm):
    certifications = forms.ModelMultipleChoiceField(queryset=Certifications.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    specializations = forms.ModelMultipleChoiceField(queryset=Specializations.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = TrainerProfile
        fields = ['certifications','specializations','year_of_experience','education_background',]
        widgets = {
            'year_of_experience' : forms.NumberInput(attrs={'class':'form-control'}),
            'education_background' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
        }


class MemberProfileAddForm(forms.ModelForm):

    class Meta:
        model = MemberProfile
        fields = "__all__"
        exclude = [ 'cextended_user' ] 

        widgets = {
            'goal':forms.Select(attrs={'class':'form-control'}),
            'activity_level':forms.Select(attrs={'class':'form-control'}),

           

        }


class DietPlanAddFormBAdmin(forms.ModelForm):
    member = forms.ModelChoiceField(queryset=AssignTrainer.objects.none(),widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomizedPlan
        fields = "__all__"
        exclude = [ 'trainer' ,  'bmr','calorie_intake_goal','created_at']
        widgets = {                 
                    'start_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'meal_options' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
                    'end_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'calorie_intake' : forms.TextInput(attrs={'class':'form-control'}),
                    'goal' : forms.TextInput(attrs={'class':'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        added_by = kwargs.pop('added_by')
        super(DietPlanAddForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = AssignTrainer.objects.filter(trainer__user__username=added_by)




class DietPlanAddFormBAdmin(forms.ModelForm):
    class Meta:
        model = CustomizedPlan
        fields = ['admin_member','start_date','meal_options','end_date','goal','calorie_intake']
        widgets = {
                    'admin_member' : forms.Select(attrs={'class':'form-control'}),
                    'start_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'meal_options' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
                    'end_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'goal' : forms.TextInput(attrs={'class':'form-control'}),
                    'calorie_intake' : forms.TextInput(attrs={'class':'form-control'}),


        }
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Get the request object from kwargs
        super(DietPlanAddFormBAdmin, self).__init__(*args, **kwargs)
        # Update the queryset for the member field
        self.fields['admin_member'].queryset = ExtendedUserModel.objects.filter(role__name='Customer', added_by__user__username=request.user.username)




class DietPlanAddFormBAdminEdit(forms.ModelForm):
    class Meta:
        model = CustomizedPlan
        fields = ['admin_member','start_date','meal_options','end_date']
        widgets = {
            'admin_member' : forms.Select(attrs={'class':'form-control'}),
            'start_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'meal_options' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
            'end_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
        }
    # def __init__(self, *args, **kwargs):
    #     request = kwargs.pop('request', None)  # Get the request object from kwargs
    #     super(DietPlanAddFormBAdminEdit, self).__init__(*args, **kwargs)
    #     # Update the queryset for the member field
    #     self.fields['admin_member'].queryset = ExtendedUserModel.objects.filter(role__name='Customer',)





class DietPlanAddForm(forms.ModelForm):
    member = forms.ModelChoiceField(queryset=AssignTrainer.objects.none(),widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomizedPlan
        fields = "__all__"
        exclude = [ 'trainer','added_by_admin','admin_member','calorie_intake_goal','created_at']
        widgets = {                 
                    'start_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'meal_options' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
                    'end_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                    'calorie_intake' : forms.TextInput(attrs={'class':'form-control'}),
                    'goal' : forms.TextInput(attrs={'class':'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        added_by = kwargs.pop('added_by')
        super(DietPlanAddForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = AssignTrainer.objects.filter(trainer__user__username=added_by)





class DietPlanTrainerEditForm(forms.ModelForm):
    class Meta:
        model = CustomizedPlan
        fields = "__all__"
        exclude = [ 'trainer' ,  'bmr','calorie_intake_goal','created_at','status','member','calorie_intake','goal']
        widgets = {
            'start_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'meal_options' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':3}),
            'end_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
        }
class DietPlanEditForm(forms.ModelForm):

    class Meta:
        model = CustomizedPlan
        fields = ['status']
        exclude = [ 'trainer' ,  'bmr','calorie_intake_goal','created_at', 'start_date','meal_options','end_date','calorie_intake', 'goal']
        widgets = {              

            'status' : forms.Select(attrs={'class': 'form-control'}),


        }

class ScheduleAddFormBA_Admin(forms.ModelForm):
    admin_member = forms.ModelChoiceField(queryset=ExtendedUserModel.objects.none(),widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Schedule
        fields = ['schedule_date','admin_member','workout_type','note']
        widgets = { 
            'note' : forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'workout_type' : forms.TextInput(attrs={'class': 'form-control'}),
            'schedule_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            # 'note' : forms.TextInput(attrs={'form-control'})
        }
    def __init__(self, *args, **kwargs):
        added_by = kwargs.pop('added_by')
        super(ScheduleAddFormBA_Admin, self).__init__(*args, **kwargs)
        self.fields['admin_member'].queryset = ExtendedUserModel.objects.filter(added_by__user=added_by,role__name = 'Customer')










class ScheduleForm(forms.ModelForm):
    members = forms.ModelChoiceField(queryset=ExtendedUserModel.objects.none(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Schedule
        fields = ['schedule_date','members','workout_type','note']
        widgets = { 
            'note' : forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'workout_type' : forms.TextInput(attrs={'class': 'form-control'}),
            'schedule_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            # 'note' : forms.TextInput(attrs={'form-control'})
        }

    def __init__(self, *args, **kwargs):
        added_by = kwargs.pop('added_by')
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset   =AssignTrainer.objects.filter(trainer__user__username=added_by)

  
class ScheduleTrainerEditForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['schedule_date','workout_type','note']

        widgets = {
            'workout_type' : forms.TextInput(attrs={'class': 'form-control'}),
            'schedule_date' : forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'note' : forms.Textarea(attrs={'class': 'form-control','rows':3}),
        }



class ScheduleEditForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['status']
        exclude = ['trainer','day', 'time_slot_field', 'schedule_date','members','workout_type']

        widgets = {
            'status' : forms.Select(attrs={'class': 'form-control'}),

        }



class CommonDietPlanForm(forms.ModelForm):
    class Meta:
        model = CommonDietPlan
        fields = "__all__"
        exclude = ['added_by','added_by_admin']

        widgets = {
            'goal' : forms.Select(attrs={'class':'form-control'}),
            'day' : forms.Select(attrs={'class': 'form-control'}),
            'breakfast' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':2}),
            'snack_mrng': forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':2}),
            'lunch' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':2}),
            'snack' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':2}),
            'dinner': forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':2}),
            'optional_beverages' : forms.Textarea(attrs={'class':'form-control','placeholder':'Note','rows':2}),
        }

class PendingPaymentForm(forms.ModelForm):
    class Meta:
        model = ExtendedUserModel
        fields = ['amount_paid']
        widgets = {
            'amount_paid': forms.NumberInput(attrs={'class':'form-control'})
        }






class SlotAddForm(forms.ModelForm):
    class Meta:
        model = SlotBooking
        fields = ['slot_date','from_timing','to_timingg']
        widgets = {
            'slot_date' :forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'from_timing' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'to_timingg' : forms.TimeInput(attrs={'class': 'form-control','type':'time'})
        }



class SlotAddFormBussinessAdmin(forms.ModelForm):
    class Meta:
        model = SlotBooking
        fields = "__all__"
        exclude = ['slot_count']
        widgets = {
            'added_by' : forms.Select(attrs={'class':'form-control'}),
            'slot_date' :forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'from_timing' : forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'to_timingg' : forms.TimeInput(attrs={'class': 'form-control','type':'time'})
        }
    def __init__(self, *args, **kwargs):
        added_by = kwargs.pop('added_by')
        super(SlotAddFormBussinessAdmin, self).__init__(*args, **kwargs)
        self.fields['added_by'].queryset = ExtendedUserModel.objects.filter(role__name='Customer', added_by__user=added_by,status__name = 'Active')



class SalaryAddForm(forms.ModelForm):
    class Meta:
        model = Salary_management
        fields = '__all__'
        exlude = ['balance']
        widgets = {
            'salary_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'trainer': forms.Select(attrs={'class':'form-control'}),
            'salary' : forms.NumberInput(attrs={'class':'form-control'}),
            'personal_training_amount' : forms.NumberInput(attrs={'class':'form-control','required':'False'}),            
            'insentive': forms.NumberInput(attrs={'class':'form-control','required':'False'}),
            'advance_paid': forms.NumberInput(attrs={'class':'form-control','required':'False'}),
            'paid': forms.NumberInput(attrs={'class':'form-control','required':'False'}),
            'absent': forms.NumberInput(attrs={'class':'form-control','required':'False'})
        }
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Get the request object from kwargs
        super(SalaryAddForm, self).__init__(*args, **kwargs)
        # Update the queryset for the member field
        self.fields['trainer'].queryset = ExtendedUserModel.objects.filter(Q(role__name = 'Fitness Trainer') | Q(role__name = 'Receptionist') | Q(role__name = 'Other Staff'))



    




class SlotCountAddForm(forms.ModelForm):
    class Meta:
        model = Slot_Count
        fields = ['countt']
        widgets = {
            'countt' : forms.NumberInput(attrs={'class':'form-control'})
        }


class MembershipPlanAddForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = ['name','duration','session','price']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'duration' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'session' : forms.TextInput(attrs={'class':'form-control','placeholder':'Session details'}),

        }

class GoalAddForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }
