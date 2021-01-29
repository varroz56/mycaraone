from django.shortcuts import render

# A view to show user profile page
class UserProfileView(request):
    userprofile = request.user.userprofile

    context = {
        'userprofile': userprofile,
    }
    return render(request, 'profiles/myprofile.html', context)
