from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import ListView, CreateView
from django.core.mail import send_mail
from .forms import TicketForm
from .models import Event, Ticket


class HomeEvents(ListView):
    model = Event
    template_name = 'tickets/index.html'
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Event.objects.all()


class CreateTicket(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/reserve_ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            event = get_object_or_404(Event, pk=self.kwargs['pk'])
            context = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'type': form.cleaned_data['type'],
                'event': event
            }
            html_message = render_to_string('tickets/email_template.html', context)
            plain_message = strip_tags(html_message)
            send_mail(f'Резервирование билета на мероприятие {event.title}',
                      plain_message,
                      'omka2061',
                      [context['email']],
                      fail_silently=False, html_message=html_message)
            return redirect('/success/')
        return render(request, self.template_name, {'form': form})


def about(request):
    return render(request, 'tickets/about.html', {})


def success(request):
    return render(request, 'tickets/success.html', {})
