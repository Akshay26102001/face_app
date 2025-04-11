from django.shortcuts import render
from .models import PunchRecord
from .face_recognizer import recognize_face

def punch(request):
    if request.method == "POST":
        time = recognize_face()
        PunchRecord.objects.create(name="John Doe", punched_at=time)
        return render(request, 'punch.html', {'message': 'Punch recorded!'})

    return render(request, 'punch.html')
