from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Post, OurWorks, WorkDone
from .forms import ContactUs

posts = [
    {
        'author': 'Felix KKK',
        'title': 'Feedback 1',
        'content': 'Happiness and freedom come from knowing what to care about--and most importantly, what not to care about. ',
        'date_posted': '27/12/2020'
    },
    {
        'author': 'Steven Teck',
        'title': 'Feedback 2',
        'content': 'Resilience, happiness and freedom come from knowing what to care aboute readers the wisdom to be able to do just that',
        'date_posted': '27/12/2020'
    },
    {
        'author': 'Jack Nicoleson',
        'title': 'Feedback 3',
        'content': 'I dont know what else to say. It had everything we wanted and was better designed than anything we could have accomplished on our own. ',
        'date_posted': '27/12/2020'
    },
    {
        'author': 'Jack Nicoleson',
        'title': 'Feedback 3',
        'content': 'I dont know what else to say. It had everything we wanted and was better designed than anything we could have accomplished on our own. ',
        'date_posted': '27/12/2020'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all(),
        'ourwork': OurWorks.objects.all(),
        'workdone': WorkDone.objects.all(),
    }
    return render(request, 'home/home.html', context)


class HomeReviewListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class HomeReviewDetailView(DetailView):
    model = Post
    template_name = 'users/review_detail_form.html'


class HomeReviewCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'users/review_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HomeReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'users/review_update_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def contact(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            contact_name = request.POST['contact_name']
            contact_email = request.POST['contact_email']
            contact_phone = request.POST['contact_phone']
            contact_message = request.POST['contact_message']

            # Send eMail
            send_mail(
                'Enquiries from ' + contact_name + ' Mobile: ' + contact_phone,
                contact_message,
                contact_email,
                ['fknortey@gmail.com', 'decklonnyarko@gmail.com']
            )
            return HttpResponseRedirect(request.path_info, {'msg': contact_name})
        else:
            return redirect('Home')
    else:
        return redirect('Homexxx')

