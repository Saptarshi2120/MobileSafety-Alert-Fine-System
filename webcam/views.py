from django.shortcuts import render
from django.http import StreamingHttpResponse
from . import camera


def home(request):
    if request.method == "POST":
        return render(request, "index.html")
    else:
        return render(request, "index.html")


def __gen(camera: camera.webcam):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


def video(request):
    return StreamingHttpResponse(
        __gen(camera.webcam()), content_type="multipart/x-mixed-replace; boundary=frame"
    )
