from django.shortcuts import render
from images.models import Image
from django.views.generic import ListView
from images.forms import AddImage, ResizeImage
from PIL import Image as PIL_Im
from django.shortcuts import redirect

class ImageList(ListView):
    model = Image
    template_name = "images/image_list.html"


def add_image(request):
    if request.method == 'POST':
        if request.POST.get('img') == '' and request.POST.get('img_url') == ''\
                or request.POST.get('img') != '' and request.POST.get('img_url') != '':
            form = AddImage()
            return render(request, 'images/add_image.html', {'form': form, 'fill': True})

        form = AddImage(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            print(data)
            return redirect('resize image', data.id)
    else:
        form = AddImage()
    return render(request, 'images/add_image.html', {'form': form})


def resize_image(request, image_id):
    im = Image.objects.get(id=image_id)
    if request.method == 'POST':
        form = ResizeImage(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            width = data.get('width')
            height = data.get('height')
            im.rszdimg = res_img(im.img.path, width, height)
            im.save()


    else:
        form = ResizeImage()
    return render(request, 'images/resize_image.html',
                  {'form': form, 'image': im, 'name': im.rszdimg.name.split('/')[1]})


def res_img(path, width, height):
    resized = PIL_Im.open(path)
    if not width:
        width = resized.size[0]
    if not height:
        height = resized.size[1]
    resized = resized.resize((width, height))
    file_name = str(path.split('\\')[-1])
    file_path = 'media/resized_pictures/' + file_name
    resized.save(file_path)
    return 'resized_pictures/' + file_name
