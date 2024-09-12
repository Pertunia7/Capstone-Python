from django.shortcuts import render
from .models import Topic,Atricle
from . import forms

# Create your views here.

def send_input_data(request):

  form = forms.InputForm()
  
  if request.method == "POST":
      
      form = forms.InputForm(request.POST)
      
      if form.is_valid():
          print("form Valid")
           
  
  return render(request,'input.html',{'form':form})
def show_topics(request):

  topics = Topic.objects.all()
  
  return render(request,'index.html',{'topics':topics})


def showarticle(request):

    title = "My first article"
    author = "Pertunia"
    article_text = """
 Cras non arcu ut ipsum molestie posuere. Etiam feugiat nulla vitae quam pellentesque posuere. Mauris ut dolor quis lacus elementum malesuada ac non quam. Aenean sollicitudin, metus consequat laoreet faucibus, ex mauris suscipit enim, ac efficitur justo mi quis mauris. Integer maximus posuere ornare. Vivamus vestibulum ultrices risus, vitae rhoncus sem vestibulum sit amet. Nunc eu iaculis orci. Sed sed risus sit amet eros feugiat lobortis sed sed ante. In ornare neque nec libero fermentum mattis. Aliquam fermentum enim quam, sit amet aliquet lectus congue sit amet. Suspendisse sed sollicitudin purus. In iaculis vel sem et varius. Etiam sollicitudin ligula at posuere gravida. Interdum et malesuada fames ac ante ipsum primis in faucibus.

 Curabitur viverra porttitor eros ut porta. Aliquam pharetra consequat vestibulum. Etiam imperdiet leo ac faucibus dictum. Vestibulum ac luctus dui. Aenean aliquet faucibus sapien ut sagittis. Phasellus tempor, magna in vestibulum tristique, felis magna finibus ex, vitae venenatis erat nulla nec nunc. Nulla malesuada nisl quis imperdiet luctus. Morbi feugiat porta ligula, ut laoreet elit tempus a. Ut et mauris metus.

 Curabitur in hendrerit justo. Praesent hendrerit lacus fermentum sapien pretium, ac rhoncus magna suscipit. Aliquam eget ante vitae magna ornare porttitor quis faucibus arcu. In sed erat et tortor porta pellentesque. Phasellus eu congue magna. Cras laoreet interdum venenatis. Vivamus id lobortis erat. Nullam pharetra augue volutpat, finibus felis vitae, gravida quam. Integer semper iaculis metus, sollicitudin tristique purus tempor eu. Integer tempor sapien in egestas porta.

 Quisque faucibus efficitur ex, et ultrices mi rutrum eu. Curabitur eu pulvinar dolor, in dictum lectus. Nulla malesuada est mi, ac vulputate leo feugiat tincidunt. Curabitur vitae semper elit, sit amet eleifend neque. In vel lorem at tortor lacinia consequat ut at est. Sed semper vulputate mollis. Proin sodales pellentesque risus, et finibus arcu rhoncus in. Praesent rutrum ante et lacus consequat congue. Aenean ornare posuere nibh.
 """
    return render(request,'article/article.html',{'title':title,'author':author,'article_text':article_text})
