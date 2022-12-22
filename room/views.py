from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .models import  Room,Message
# from .forms import RoomForm

@login_required
def rooms(request):	
	# if request.method == 'POST':print(a)
	#     form = RoomForm(request.POST)
	#     if form.is_valid():
	# 		form.save() 
	# 		return redirect('rooms')  
	# else:
	# 	form = RoomForm()			
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }

    return render(request, 'room/rooms.html',context)

@login_required
def room(request,slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room = room)[0:25]
    context={
        'room':room,
        'messages':messages,
    }
    return render(request, 'room/room.html',context)
