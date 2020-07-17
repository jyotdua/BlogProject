from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, employee
from .forms import PostForm, CommentForm, Userform, ProfileForm
from django.views.generic import (TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView)
from django.utils import timezone
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import Postserializer, Employeesserializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from django.contrib.auth.models import User
from  rest_framework import permissions
from .permissons import Is_Owner_Or_Read_Only
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    return Response({'employees': reverse('blogapp:employees')})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class employeeviewset(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = Employeesserializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, Is_Owner_Or_Read_Only)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



class PostList(APIView):
    renderer_classes = {TemplateHTMLRenderer}
    template_name = 'rest_framework/api.html'
    def get(self, request):

        post_list = Post.objects.all()
        serializer = Postserializer(post_list, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Postserializer(data=request.data)
        if serializer.is_valid():
            mydict={'serializer': serializer}
            print("x")
            serializer.save()

            return Response(serializer.data, mydict)

        return Response(serializer.errors, status=400)



class Employeelist(generics.ListCreateAPIView):
    permisson_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = employee.objects.all()
    serializer_class = Employeesserializer

class Employeedetail(generics.RetrieveUpdateDestroyAPIView):
    permisson_classes = (permissions.IsAuthenticatedOrReadOnly,Is_Owner_Or_Read_Only)
    queryset = employee.objects.all()
    serializer_class = Employeesserializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class AboutView(TemplateView):
    template_name = 'blogapp/about.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_detail.html'
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_detail.html'
    form_class = PostForm
    model = Post


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blogapp:post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')



def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogapp:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blogapp/comment_form.html', {'form': form})


def register(request):
    registered = False
    form = Userform
    profile_form = ProfileForm
    if request.method == 'POST':
        form = Userform(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.save()

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES('profile_pic')
                profile.save()
        else:
            print(form.errors, profile_form.errors)

    else:
        form = Userform()
        profile_form = ProfileForm()
    return render(request, 'blogapp/register_blood.html',
                  {'form': form, 'profile_form': profile_form, 'registered': registered})


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blogapp:post_detail', pk=comment.post.pk)


@login_required()
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blogapp:post_detail', pk=post_pk)


@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blogapp:post_detail', pk=pk)

# Create your views here.
