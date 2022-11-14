from django.shortcuts import render

from todo.models import Task, Tag


def index(request):
    """View function for the home page of the site."""

    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
        "num_visits": num_visits + 1,
    }

    return render(request, "todo/index.html", context=context)