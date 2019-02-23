from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from account.forms.schedule import ScheduleForm
from account.models import Schedule


class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedule/schedule.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(ScheduleCreateView, self).get_form_kwargs()
        kwargs.update(request=self.request)
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            data = form.cleaned_data
            user: User = self.request.user
            self.object, _ = user.schedules.update_or_create(
                type=data.pop('type'),
                defaults=data
            )
        return HttpResponseRedirect(self.get_success_url())
