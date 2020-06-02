from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm # forms.py에서 PostForm 가져오기

def detail(request, pk): # request와 pk도 인자로 받음
    post = get_object_or_404(Post, pk=pk) # 해당 객체가 있으면 가져오고 없으면 404에러, pk값은 pk
    return render(request, 'detail.html', {'post':post})


def main(request):
    posts = Post.objects
    return render(request, 'posts.html', {'posts':posts})
    
def create(request):
    if request.method == 'POST': # POST vs. GET 분기
        form = PostForm(request.POST) # 
        if form.is_valid(): # form 유효성 검증
            form.save() # 저장하고
            return redirect('main') # main페이지로 가기
    else:
        form = PostForm() # 빈 form 열기
    return render(request, 'create.html', {'form':form})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk) # 있으면 가져오고 없으면 404에러
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) # post 객체 가져오기
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post) # post 객체 가져와서 form 생성 
    return render(request, 'update.html', {'form':form})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('main')


    


