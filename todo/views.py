from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3
    queryset = Task.objects.all().prefetch_related("tags")


class TagListView(generic.ListView):
    model = Tag


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task_list")
    template_name = "todo/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task_list")
    template_name = "todo/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag_list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag_list")
    template_name = "todo/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")