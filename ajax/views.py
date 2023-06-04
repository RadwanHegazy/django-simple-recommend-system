from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app.models import Video, Recommend_Video
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json



def search_by_recommend (main_video,videos) :
    
    main_text = str(main_video).split(' ')
    wanted_videos = []

    for video in videos :

        scoore = 0
        hight_scoore = len(main_text)

        video_text = str(video.genre).split(' ')
        for word in video_text :
            if word in main_text :
                scoore = scoore + 1 


        video_scoore = (scoore / hight_scoore) * 100
        if video_scoore > 50 :
            wanted_videos.append({'id':video.id,'video':video.video.url})


    return wanted_videos





@csrf_exempt
def like (request) :

    user = request.user
    video_id = request.POST['id']
    video = Video.objects.get( id = video_id )

    # get genre of video
    genre = video.genre

    Recommend_Video.objects.get_or_create( user = user )
    recommended = Recommend_Video.objects.get( user = user )
    recommended.user_recommend += genre
    recommended.save()

    return HttpResponse('ok')

def videos (request) :
    
    if Recommend_Video.objects.filter(user = request.user).exists() :
        data = Recommend_Video.objects.get( user = request.user )
        wanted_data = data.user_recommend
        data = search_by_recommend(wanted_data, Video.objects.all().order_by('?'))
    else :
        data_ = Video.objects.all().order_by('?')
        data = []
        for i in data_ :
            data.append(
                {
                    'id':i.id,
                    'video':i.video.url
                }
            )


    return JsonResponse(data=data,safe=False)
    
