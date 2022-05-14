from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.postgres.search import TrigramDistance
# Create your views here.


def index(request):

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
            print(ip)
        return ip
    ip = get_ip(request)
    u = User(user=ip)
    print(ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exist")
    elif len(result) > 1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")
    counts = User.objects.all().count()
    print("total user is", counts)
    context = {
        "mobile": mobile.objects.filter(status="p",).order_by("-publication_blog")[:10],
        "labtop": labtop.objects.filter(status="p",).order_by("-publication_blog")[:10],
        "post": post.objects.filter(status="p").order_by("-publish")[:10],
        "category": category.objects.filter(status=True),
        "category_obshen": category_obshen.objects.filter(status=True),
        "count": counts
    }
    return render(request, "blog/tech-index.html", context)


def index2(request):
    context = {
        "mobile": mobile.objects.filter(status="p",).order_by("-publication_blog")[11:20],
        "labtop": labtop.objects.filter(status="p",).order_by("-publication_blog")[11:20],
        "post": post.objects.filter(status="p").order_by("-publish")[11:20],
        "category": category.objects.filter(status=True),
    }
    return render(request, "blog/tech-index2.html", context)


def posts(request):
    context = {
        "mobile": mobile.objects.filter(status="p",).order_by("-publication_blog"),
        "labtop": labtop.objects.filter(status="p",).order_by("-publication_blog"),
        "post": post.objects.filter(status="p").order_by("-publish"),
        "category": category.objects.filter(status=True),
    }
    return render(request, "blog/tech-index.html", context)


def post_detail(request, slug, id):
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
            print(ip)
        return ip
    ip = get_ip(request)
    u = User(user=ip)
    print(ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exist")
    elif len(result) > 1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")
    counts = User.objects.all().count()
    print("total user is", counts)
    context = {
        "post": get_object_or_404(post, slug=slug, status="p"),
        "comment": comment.objects.filter(post_key_id=id, is_reply=False),
        "category_obshen": category_obshen.objects.filter(status=True),
        "category": category.objects.filter(status=True),
        "count": counts
    }
    return render(request, "blog/tech-single.html", context)


def mobile_detail(request, slug, prcs_id, speaker_id, cameras_id, material_id, memory_id):
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
            print(ip)
        return ip

    ip = get_ip(request)
    u = User(user=ip)
    print(ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exist")
    elif len(result) > 1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")
    counts = User.objects.all().count()
    print("total user is", counts)
    moboss = get_object_or_404(mobile, slug=slug, status='p')
    processors = get_object_or_404(processor, id=prcs_id)
    speakers = get_object_or_404(speaker, id=speaker_id)
    camer = get_object_or_404(camera, id=cameras_id)
    material = get_object_or_404(mobile_body, id=material_id)
    memor = get_object_or_404(memory, id=memory_id)
    context = {
        'mobo': moboss,
        'processor': processors,
        'speaker': speakers,
        'camera': camer,
        'material': material,
        'memory': memor,
        "count": counts,
        "category": category.objects.filter(status=True),
    }
    return render(request, 'blog/index.html', context)


def labtop_detail(requests, slug, lobtop_speaker_id, labtop_processor_id, connections_id):

    labtops = get_object_or_404(labtop, slug=slug, status="p")
    connections_ids = get_object_or_404(connections_labtop, id=connections_id)
    speaker_detail = get_object_or_404(speaker, id=lobtop_speaker_id)
    processors = get_object_or_404(processor, id=labtop_processor_id)

    context = {
        "connections_ids": connections_ids,
        "processors": processors,
        "speak": speaker_detail,
        "labtop": labtops,
        "category": category.objects.filter(status=True),
        "category": category.objects.filter(status=True),
    }
    return render(requests, "blog/index2.html", context)


def category_post(request, slug):
    categor = get_object_or_404(category, slug=slug, status=True)
    print(categor)
    posts = categor.post.all()
    labtop = categor.categorys.all()
    mobo = categor.category.all()
    print(posts)

    context = {
        "categor": posts,
        "labtop": labtop,
        "mobo": mobo,
        "category_obshen": category_obshen.objects.filter(status=True),
        "category": category.objects.filter(status=True),
    }
    return render(request, "blog/tech-category-01.html", context)


def category_obshens(request, slug):
    categor = get_object_or_404(category_obshen, slug=slug, status=True)
    print(categor)
    posts = categor.category.all()
    labtop = categor.category_obshe.all()
    mobo = categor.category_obshens.all()
    print(posts)

    context = {
        "categor": posts,
        "labtop": labtop,
        "mobo": mobo,
        "category_obshen": category_obshen.objects.filter(status=True),
        "category": category.objects.filter(status=True),
    }
    return render(request, "blog/tech-category-00.html", context)


def search(request):
    if request.method == 'POST':
        searchs = request.POST['search']
        if searchs:
            if mobile.objects.filter(mobile_name=searchs).exists():
                mobo = get_object_or_404(mobile, mobile_name=searchs)
                context = {
                    "mob": mobo,
                    "category_obshen": category_obshen.objects.filter(status=True),
                }
                return render(request, 'blog/search-mobile.html', context)
            elif post.objects.filter(title=searchs).exists():
                pos = get_object_or_404(post, title=searchs)
                context = {

                    "post": pos,
                    "category_obshen": category_obshen.objects.filter(status=True),
                }
                return render(request, 'blog/search.html', context)
            elif labtop.objects.filter(labtop_name=searchs).exists():
                lab = get_object_or_404(labtop, labtop_name=searchs)
                context = {

                    "labtops": lab,
                    "category_obshen": category_obshen.objects.filter(status=True),
                }
                return render(request, 'blog/search-labtop.html', context)
    else:
        return render(request, 'blog/tech-index.html', {})


def comments(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        commentss = comment_form(request.POST)
        if commentss.is_valid():
            data = commentss.cleaned_data
            comment.objects.create(email=data['email'], desc=data['desc'], post_key_id=id)
            return redirect(url)
            messages.success(request, 'Comment left successfully', 'dark')


def reply(request, id, comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        reply = reply_form(request.POST)
        if reply.is_valid():
            date = reply.cleaned_data
            comment.objects.create(email=date['email'], desc=date['desc'], post_key_id=id, reply_id=comment_id, is_reply = True)
            messages.success(request, 'thanks for reply', 'primary')
            return redirect(url)



# def search2(request):
#     if request.method == 'POST':
#         test = request.POST['search']
#         pos = post.objects.annotate(distance=TrigramWordDistance(test, 'title'),).filter(distance__lte=0.7).order_by('distance')
#         print(pos)
#         context = {
#
#             "post": pos,
#             "category_obshen": category_obshen.objects.filter(status=True),
#         }
#         return render(request, 'blog/search.html', context)
#
#     else:
#         return render(request, 'blog/tech-index.html', {})
