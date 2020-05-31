
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


from .models import Meeting, Meeting_Item


class IndexView(generic.ListView):
    template_name = 'meeting/index.html'
    context_object_name = 'latest_meeting_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Meeting.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Meeting
    template_name = 'meeting/detail.html'


class ResultsView(generic.DetailView):
    model = Meeting
    template_name = 'meeting/results.html'

# ...
# def detail(request, meeting_id):
#     meeting = get_object_or_404(Meeting, pk=question_id)
#     return render(request, 'meeting/detail.html', {'meeting': meeting})

# def results(request, meeting_id):
#     question = get_object_or_404(Meeting, pk=meeting_id)
#     return HttpResponse(response % meeting_id)
# ...
# def vote(request, meeting_id):
#     question = get_object_or_404(Meeting, pk=question_id)
#     try:
#         selected_choice = meeting.meeting_item_set.get(pk=request.POST['meeting_item'])
#     except (KeyError, Meeting_Item.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'meeting/detail.html', {
#             'meeting': meeting,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('meeting:results', args=(meeting.id,)))


def index(request):
    latest_meeting_list = Meeting.objects.order_by('-pub_date')[:5]
    context = {'latest_meeting_list': latest_meeting_list}
    return render(request, 'meeting/index.html', context)

# Leave the rest of the views (detail, results, vote) unchanged