from django import template
from django.shortcuts import render_to_response
from news_and_events.models import NewsArticle
from contacts_and_people.models import Entity
# from entity_tags import entity_for_page, work_out_entity
from cms.models import Page
from datetime import datetime
from django.template.defaultfilters import date
from arkestra_utilities.output_libraries.dates import nice_date

register = template.Library()

@register.inclusion_tag('newslist.html', takes_context = True)
def news(context, format = "all_info", max_items = 20, entity = None):
    """
    Publishes a date-ordered list of news items
    """
    if not entity:
        entity = work_out_entity(context, entity)
    return {
        'entity': entity,
        'news': entity.newsarticle_set.filter(date__lte = datetime.now())[0: max_items],
        'format': format,
        }    

@register.inclusion_tag('newslist.html', takes_context=True)
def news_for_this_page(context, max_items):    
    request=context['request']
    page = request.current_page
    entity = entity_for_page(page)
    if entity:
        return {
            'news': entity.newsarticle_set.all()[0: max_items],
            }
    else:    
        return { 'news': "No news is good news",}
