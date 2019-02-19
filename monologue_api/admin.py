from django.contrib import admin

from monologue_api.models import Action, Emotion, Said


class ActionAdmin(admin.ModelAdmin):
    pass


class EmotionAdmin(admin.ModelAdmin):
    pass


class SaidAdmin(admin.ModelAdmin):
    pass


admin.site.register(Action, ActionAdmin)
admin.site.register(Emotion, EmotionAdmin)
admin.site.register(Said, SaidAdmin)
