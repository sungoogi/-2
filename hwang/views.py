from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# 게시물 목록을 보여주는 뷰
def post_list(request):
    # 모든 게시물을 가져오면서, 각 게시물의 사용자 정보도 미리 가져옵니다.
    posts = Post.objects.select_related('user').all()
    # post_list.html 템플릿을 렌더링하고, posts 컨텍스트 변수를 전달합니다.
    return render(request, 'post_list.html', {'posts': posts})

# 로그인한 사용자만 접근할 수 있는 게시물 생성 뷰
@login_required
def post_create(request):
    if request.method == 'POST':  # 요청 메서드가 POST인 경우
        form = PostForm(request.POST)  # POST 데이터를 사용하여 폼을 생성합니다.
        if form.is_valid():  # 폼 데이터가 유효한 경우
            post = form.save(commit=False)  # 데이터베이스에 저장하지 않고 Post 객체를 반환합니다.
            post.user = request.user  # 현재 로그인된 사용자를 게시물 작성자로 설정합니다.
            post.save()  # 게시물을 데이터베이스에 저장합니다.
            return redirect('post_list')  # 게시물 목록 페이지로 리디렉션합니다.
    else:  # 요청 메서드가 GET인 경우
        form = PostForm()  # 빈 폼을 생성합니다.
    # post_create.html 템플릿을 렌더링하고, form 컨텍스트 변수를 전달합니다.
    return render(request, 'post_create.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})