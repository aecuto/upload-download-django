import threading
import time

import schedule

from django.core.management import call_command

def run_continuously(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run


def background_job():
    call_command("remove_expired_files")

schedule.every(2).minutes.do(background_job)
# schedule.every().second.do(background_job)

