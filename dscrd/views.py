from django.shortcuts import render, redirect
from .models import Channel
from .forms import ChannelForm

def home(request):
    channels = Channel.objects.all()
    context = {'channels': channels}
    return render(request, 'base/home.html', context)

def channel(request, pk):
    channel = Channel.objects.get(id=pk)
    context = {'channel': channel}
    return render(request, 'base/channel.html', context)

def create_channel(request):
    form = ChannelForm()
    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/channel_form.html', context)

def update_channel(request, pk):
    channel = Channel.objects.get(id=pk)
    form = ChannelForm(instance=channel)
    
    if request.method == 'POST':
        form = ChannelForm(request.POST, instance=channel)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/channel_form.html', context)

def delete_channel(request, pk):
    channel = Channel.objects.get(id=pk)
    if request.method == 'POST':
        channel.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {"obj": channel})