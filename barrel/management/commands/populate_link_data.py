__author__ = 'rogersjeffrey'
from django.core.management.base import BaseCommand
from barrel.models import LinkData,Link
import bitly
import json
class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self,urls):

        for url in urls:
          print url
          social_response=bitly.social({"url":url})

          social_score=float(str(social_response['data']['social_scores'][url]))
          click_data=bitly.click_rate({"url":url})

          cumulative_clicks=0.0
          for clicks in click_data['data']['link_clicks']:

              cumulative_clicks=cumulative_clicks+float(str(clicks['clicks']))
          link_data = LinkData(social_score=str(social_score),url=url,click_rate=str(cumulative_clicks))
          link_data.save()


    def handle(self, *args, **options):
        response_search = bitly.search({"query": "","location":""})
        link_objects=Link.objects.all()
        urls=[]
        for link_obj in link_objects:
            urls.append(link_obj.url)

        self._create_tags(urls)