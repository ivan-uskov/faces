from django.views.generic.base import View
from django.http import HttpResponse

import os
import facemorpher
from moviepy.editor import *
from squasher.utils import move_uploaded_file, tmp_file


class SquashPageView(View):

    def post(self, request):
        try:
            src_name = move_uploaded_file(request.FILES, 'src_image')
            dst_name = move_uploaded_file(request.FILES, 'dst_image')
            result_video_path = tmp_file('avi')
            result_gif_path = tmp_file('gif')

            facemorpher.morpher([src_name, dst_name], out_video=result_video_path, num_frames=30)

            os.unlink(src_name)
            os.unlink(dst_name)

            VideoFileClip(result_video_path).write_gif(result_gif_path)

            response = HttpResponse(open(result_gif_path).read(), content_type='image/gif')
            response['Content-Disposition'] = 'attachment; filename="result.gif"'
            os.unlink(result_video_path)
            os.unlink(result_gif_path)
        except:
            response = HttpResponse('Invalid images', content_type='text/plain')

        return response
