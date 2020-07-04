from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views import View
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator


# Create your views here.
class LoginView(View):
    def get(self, request):
        # if the user is logged in, then do a redirect to the home page
        if auth.get_user(request).is_authenticated:
            return redirect('/')
        else:
            # Otherwise, form a context with the authorization form
            # and we return to this page context.
            # It works, for url - /admin/login/ and for /accounts/login/
            context = create_context_username_csrf(request)
            # get previous url
            next = self.request.GET.get('next', None)
            context['next'] = next
            return render(request, 'account/login.html', context=context)

    def post(self, request):
        # having received the authorization request
        form = AuthenticationForm(request, data=request.POST)

        # get previous url
        next = request.POST['next']
        # check the correct form, that there is a user and he entered the correct password
        if form.is_valid():
            # if successful authorizing user
            auth.login(request, form.get_user())

            # and if the user of the number of staff and went through url /admin/login/
            # then redirect the user to the admin panel
            if next == '/admin/login/' and request.user.is_staff:
                return redirect('users-profile')
            # otherwise do a redirect to the previous page,
            # in the case of a / accounts / login / will happen is another redirect to the home page
            # in the case of any other url, will return the user to the url
            if next == 'None':
                return redirect('users-profile')

            return redirect(next)
        # If not true, then the user will appear on the login page
        # and see an error message
        context = create_context_username_csrf(request)
        context['form'] = form
        context['next'] = next
        messages.warning(request, "Error login")
        return render(request, 'account/login.html', context=context)

def create_context_username_csrf(request):
    context = {}
    context.update(csrf(request))
    context['form'] = AuthenticationForm
    return context