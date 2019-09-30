from datetime import datetime
from app.scripts.parse_positions import output_positions
from apscheduler.schedulers.blocking import BlockingScheduler


def time_task(interval, task, args):
    scheduler = BlockingScheduler()
    scheduler.add_job(func=task, args=(args,), trigger='interval', seconds=interval, next_run_time=datetime.now(), id='position_task')
    try:
        scheduler.start()
    except:
        pass


if __name__ == "__main__":
    id = 97
    position_time_task(5, output_positions, id)