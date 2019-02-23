from django import forms

from account.models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            'type',
            'dining_halls',
            'from_time',
            'to_time',
        ]

    def __init__(self, *args, request=None, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.request = request

    def save(self, commit=True):
        self.instance.user = self.request.user
        return super(ScheduleForm, self).save()
