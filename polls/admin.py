from django.contrib import admin
from .models import Information
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    # if there is not an exist field we can provide to a function for example user_info we don't have this model
    list_display = ('user', 'user_info','phone','city','website')

    def user_info(self,obj):
        return obj.description
    #and also we can write shor description of user_info to InFo
    user_info.short_description = 'INFO'
    #we can also sort our field
    def get_queryset(self, request):
        queryset=super(ProfileAdmin,self).get_queryset(request)
        # asending order
        # queryset=queryset.order_by('phone')

        #desending order
        # queryset=queryset.order_by('-phone')

        #with other field
        queryset=queryset.order_by('-phone','city')

        return queryset
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Information)
