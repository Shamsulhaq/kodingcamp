from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField


class UserProfileBasic(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=13)
    address = models.TextField()
    date_joined = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=45)
    gravatar = models.CharField(max_length=100)
    guid = models.CharField(max_length=40)


class PersonalProfile(models.Model):
    user_profile_basic_id = models.OneToOneField(UserProfileBasic, null=True,
                                                 on_delete=models.SET_NULL)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10)
    is_trainer = models.BooleanField()
    education = JSONField()
    experience = JSONField()
    is_student = models.BooleanField()
    current_organization = models.TextField()
    official_contact = models.TextField()


class OrganizationProfile(models.Model):
    user_profile_basic_id = models.OneToOneField(UserProfileBasic, null=True,
                                                 on_delete=models.SET_NULL)
    is_training_institute = models.BooleanField()
    industry_type = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    founded_on = models.DateField()
    company_size = models.CharField(max_length=50)
    description = models.TextField()
    additional_contact = JSONField()
    is_approved = models.BooleanField(default=False)


class EventBasic(models.Model):
    organization_id = models.ForeignKey('UserProfileBasic', null=True,
                                        on_delete=models.SET_NULL)
    start_date = models.DateField()                                   
    end_date = models.DateField()
    registration_deadline = models.DateField()
    title = models.TextField()
    description = models.TextField()
    banner = models.CharField(max_length=200)
    audience_level = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    venue_coordinate = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    max_audience = models.IntegerField(default=0)
    registration_fee = models.FloatField()
    currency = models.CharField(max_length=10)
    guid = models.CharField(max_length=40)


class EventDetail(models.Model):
    event_id = models.OneToOneField(EventBasic, null=True,
                                    on_delete=models.SET_NULL)
    open_for_all = models.BooleanField()
    screening_process = models.TextField()
    registration_process = models.TextField()
    payment_process = models.TextField()
    additional_fee = models.FloatField()
    review = models.TextField()
    screening_confirmation_mail = models.TextField()
    registration_confirmation_mail = models.TextField()
    payment_confirmation_mail = models.TextField()


class EventTrainer(models.Model):
    event_id = models.ForeignKey('EventBasic', null=True,
                                 on_delete=models.SET_NULL)
    trainer_id = models.ForeignKey('UserProfileBasic', null=True,
                                   on_delete=models.SET_NULL)
    rating = models.FloatField()
    status = models.CharField(max_length=45)


class EventParticipant(models.Model):
    event_id = models.ForeignKey('EventBasic', null=True,
                                 on_delete=models.SET_NULL)
    participant = models.ForeignKey('UserProfileBasic', null=True,
                                   on_delete=models.SET_NULL)
    selection_passed = models.BooleanField(default=False)
    registration_complete = models.BooleanField(default=False)
    payment_confirmed = models.BooleanField(default=False)
    review = models.TextField()
    status = models.CharField(max_length=45)
    confirmation_text = models.TextField()


class PersonalRecommendation(models.Model):
    trainer_id = models.ForeignKey('UserProfileBasic', null=True,
                                   on_delete=models.SET_NULL,
                                   related_name='+')
    profile_id = models.ForeignKey('UserProfileBasic', null=True,
                                   on_delete=models.SET_NULL,
                                   related_name='+')
    event_id = models.ForeignKey('EventBasic', null=True,
                                 on_delete=models.SET_NULL)
    remarks = models.TextField()
    status = models.CharField(max_length=45)


class JobBasic(models.Model):
    title = models.TextField()
    organization_id = models.ForeignKey('UserProfileBasic', null=True,
                                        on_delete=models.SET_NULL,
                                        related_name='jobs')
    salary_range = models.CharField(max_length=50)
    is_parttime = models.BooleanField(default=False)
    deadline = models.DateField()
    position = models.CharField(max_length=50)
    stack = models.TextField()
    guid = models.CharField(max_length=40)


class JobDetail(models.Model):
    job_post_id = models.OneToOneField(JobBasic, null=True,
                                       on_delete=models.SET_NULL)
    description = models.TextField()
    apply_instructions = models.TextField()
    screening_details = models.TextField()


class JobApplicant(models.Model):
    job_post_id = models.ForeignKey('JobBasic', null=True,
                                    on_delete=models.SET_NULL)
    selection_passed = models.BooleanField(default=False)
    call_for_interview = models.BooleanField(default=False)
    screening_details = models.TextField()


class Interest(models.Model):
    guid = models.CharField(max_length=40)
    interest = models.CharField(max_length=10)


    
    
    
    

    


