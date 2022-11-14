from django.shortcuts import render
from django.views import generic

from todo.forms import TagSearchForm
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


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 7
    queryset = Tag.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        name = self.request.GET.get("name", "")

        context = super(TagListView, self).get_context_data(**kwargs)
        context["search_form"] = TagListView(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = TagSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset