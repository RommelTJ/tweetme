from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Tweet


class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=1)



class TweetListView(ListView):
    #template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #context["another_list"] = Tweet.objects.all()
        #print(context)
        return context