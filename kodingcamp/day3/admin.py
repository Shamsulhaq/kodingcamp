from django.contrib import admin
from .models import UserProfileBasic, PersonalProfile, OrganizationProfile, \
                    EventBasic, EventDetail, EventTrainer, EventParticipant, \
                    PersonalRecommendation, JobBasic, JobDetail, JobApplicant, \
                    Interest

all_models = [UserProfileBasic, PersonalProfile, OrganizationProfile,
              EventBasic, EventDetail, EventTrainer, EventParticipant,
              PersonalRecommendation, JobBasic, JobDetail, JobApplicant,
              Interest]


admin.site.register(all_models)
