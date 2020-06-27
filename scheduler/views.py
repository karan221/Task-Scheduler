from django.views import View
from django.http import JsonResponse, HttpResponse

from datetime import datetime
from . import task
import threading

class TaskSchedulerView(View):
    """
    Schedule a task
    """
    def get(self, request):
        # extract parameters from request
        datetime_str = request.GET.get('datetime', '')
        url = request.GET.get('url','')
        
        # check if parameters are valid
        is_valid_url = task.is_valid_url(url)
        is_valid_datetime = task.is_valid_datetime(datetime_str)

        data = {}
        try:
            # raise exceptions if parameters are invalid
            if not (is_valid_url and is_valid_datetime):
                if is_valid_datetime == False:
                    data["datetime"] = "invalid date"
                if is_valid_url == False:
                    data["url"] = "invalid url"
                raise ValueError('invalid data')

            date_time = datetime.strptime(datetime_str, "%d-%m-%YT%H:%M:%S")
            now = datetime.now()
            delay = (date_time-now).total_seconds()
            
            #create a new thread which sleeps until the task time
            task_thread = threading.Timer(delay, task.job, args=(url,))
            task_thread.start()
            data["status"] = "success"
            return JsonResponse(data=data, status=200)
        except ValueError:
            return JsonResponse(data=data, status=400)
        except:
            data["status"]="failed"
            return JsonResponse(data, status=500)


class PingView(View):
    """
    Ping the server to check if it's running.
    """
    def get(self, request):
        data = {
            "status" : "OK",
        }
        return JsonResponse(data)
