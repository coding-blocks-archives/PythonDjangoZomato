from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
  TemplateView,
  DetailView,
  CreateView
)
from django.contrib.auth.decorators import login_required

from main import models, forms

# Create your views here.
class Index(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, *args, **kwargs):
    restaurants = models.Restaurant.objects.all()
    return {
      "restaurants": restaurants
    }

class Restaurant(DetailView):
  model = models.Restaurant
  template_name = 'restaurant.html'

class AddReview(CreateView):
  model = models.Review
  template_name = 'add_review.html'
  fields = ['title', 'body', 'stars']

  def get_success_url(self):
    return '/restaurant/{}'.format(self.kwargs['pk'])

  def form_valid(self, form):
    restaurant = models.Restaurant.objects.get(pk = self.kwargs['pk'])

    review = form.save(commit = False)
    review.user = self.request.user
    review.restaurant = restaurant
    review.save()

    return HttpResponseRedirect(self.get_success_url())

@login_required
def add_review(request, pk):
  form = forms.ReviewModelForm()

  if request.method == "POST":
    form = forms.ReviewModelForm(request.POST)
    if form.is_valid():
      restaurant = models.Restaurant.objects.get(pk = pk)
      # review = models.Review.create(
      #   user = request.user,
      #   restaurant = restaurant,
      #   title = request.POST['title'],
      #   body = request.POST['body'],
      #   stars = request.POST['stars']
      # )
      # review = models.Review.create(
      #   user = request.user,
      #   restaurant = restaurant,
      #   title = form.cleaned_data['title'],
      #   body = form.cleaned_data['body'],
      #   stars = form.cleaned_data['stars']
      # )
      review = form.save(commit = False)
      review.user = request.user
      review.restaurant = restaurant
      review.save()
      return HttpResponseRedirect('/')

  context = {
    "form": form
  }
  return render(request, 'add_review.html', context)
