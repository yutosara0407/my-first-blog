from django.views import generic
from .forms import SearchForm, UpLoadMemberImageForm
from .models import Member, MemberImage

class IndexView(generic.ListView):
    model = Member

    # def get_context_data(self):
    #     """テンプレートへ渡す辞書の作成"""
    #     context = super().get_context_data()
    #     context['form']=SearchForm(self.request.GET) #もとの辞書にformを追加
    #     return context

    # def get_queryset(self):
    #     """テンプレートへ渡すmember_listを作成"""
    #     form = SearchForm(self.request.GET)
    #     form.is_valid() #これをしないとcleaned_dataができない

    #     #全メンバーを取得
    #     queryset = super().get_queryset()

    #     #サークルの選択があればサークルで絞り込み(filter)
    #     circle = form.cleaned_data['circle']
    #     if circle:
    #         queryset = queryset.filter(circle=circle)

class AboutView(generic.TemplateView):
    template_name = 'myapp/about.html'

class InfoView(generic.TemplateView):
    template_name = 'myapp/info.html'


def edit_member_image(request):
    if request.method != 'POST':
        form = UpLoadMemberImageForm()
    else:
        form = UpLoadMemberImageForm(request.POST, request.FILES)
        if form.is_valid():
            member_image = form.cleaned_data['member_image']
            user_profile = UserProfile()
            user_profile.member_image = member_image
            user_profile.save()
    
    context = {
        'form': form
    }
    return render(request, 'myapp/templates/member_list.html', context)