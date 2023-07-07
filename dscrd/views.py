from django.shortcuts import render
from .models import Channel

# channels = [
#     {'id': 1, 'name': 'Channel 1 django'},
#     {'id': 2, 'name': 'Channel 2 superchannel'},
#     {'id': 3, 'name': 'Channel 3 django'},
# ]

def home(request):
    channels = Channel.objects.all()
    context = {'channels': channels}
    return render(request, 'base/home.html', context)

def channel(request, pk):
    channel = Channel.objects.get(id=pk)
    context = {'channel': channel}
    return render(request, 'base/channel.html', context)

