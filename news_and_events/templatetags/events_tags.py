from django import template
from django.shortcuts import render_to_response
from django.db.models import Q
from news_and_events.models import Event
from contacts_and_people.models import Entity
from cms.models import Page
from datetime import datetime

register = template.Library()
    
@register.inclusion_tag('event_date_and_time.html', takes_context = True)
def event_date_and_time(context, event = None, date_time_info = None):
    date_and_time_heading = []
    date_and_time = []
    if not event:
        event = context.get('event')
    if not event.series:
        dates = event.get_dates()
        if dates and (date_time_info != "no_dates" or event.parent.series or not event.parent.single_day_event):
            date_and_time_heading.append("date")
            date_and_time.append(dates)
        times = event.get_times()
        if times and date_time_info != "no_times":
            date_and_time_heading.append("time")
            date_and_time.append(times)
    return {
        'event': event,
        'date_and_time_heading': date_and_time_heading,
        'date_and_time': date_and_time,
    }
