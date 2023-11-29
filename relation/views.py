from django.shortcuts import render
from django.http import HttpResponseRedirect

from relation.models import Mod, Comment


def index(request):
    mods = Mod.objects.all()
    return render(request, "relation/index.html", {"mods": mods})


def show(request, id):
    mod = Mod.objects.get(id=id)
    return render(request, "relation/show.html", {"mod": mod})


def create(request, id):
    mod = Mod.objects.get(id=id)
    comment = Comment()
    comment.text_of_comment = request.POST.get("comment")
    comment.save()
    mod.comments.add(comment)

    return HttpResponseRedirect(f"/relation/{id}")


def comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    mod_id = comment.mod.id
    comment.delete()

    return HttpResponseRedirect(f"/relation/{mod_id}")
