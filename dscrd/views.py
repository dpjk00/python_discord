from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Channel, Topic, Message, User3
from .forms import ChannelForm

def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error occured during registration')
    return render(request, 'base/login_register.html', {'form': form})

def login_page(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password are wrong')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    channels = Channel.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q))
    topics = Topic.objects.all()

    joined_channels = Channel.objects.all()

    channel_count = channels.count()
    context = {
        'channels': channels, 
        'topics': topics, 
        'channel_count': channel_count,
        'joined_channels': joined_channels,
    }
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def channel(request, pk):
    channel = Channel.objects.get(id=pk)
    channels = Channel.objects.all()
    room_messages = channel.message_set.all()
    members = channel.members.all()

    if request.method == 'GET':
        channel.members.add(request.user)

    if request.method == 'POST':
        user_message = Message.objects.create(
            user = request.user,
            channel=channel,
            message = request.POST.get('message')
        )
        channel.members.add(request.user)
        return redirect('channel', pk=channel.id)

    context = {'channel': channel, 'channels': channels, 'room_messages': room_messages, 'members': members}
    return render(request, 'base/channel.html', context)

@login_required(login_url='login')
def create_channel(request):
    form = ChannelForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Channel.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    channels = Channel.objects.all()
    context = {'form': form, 'channels': channels, 'topics': topics}
    return render(request, 'base/channel_form.html', context)

@login_required(login_url='login')
def update_channel(request, pk):
    channel = Channel.objects.get(id=pk)
    form = ChannelForm(instance=channel)
    topics = Topic.objects.all()

    if request.user != channel.host:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        form = ChannelForm(request.POST, instance=channel)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/channel_form.html', context)

@login_required(login_url='login')
def delete_channel(request, pk):
    channel = Channel.objects.get(id=pk)

    if request.user != channel.host:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        channel.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {"obj": channel})

@login_required(login_url='login')
def delete_message(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        message.delete()
        return redirect('request.META.HTTP_REFERER')
    return render(request, 'base/delete.html', {"obj": message})