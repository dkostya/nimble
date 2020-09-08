from apscheduler.schedulers.background import BackgroundScheduler
from workers import dataUpdate

def start():
    scheduller = BackgroundScheduler()

    # Update Source status and bitrate
    scheduller.add_job(dataUpdate.monitoring_source, 'interval', seconds=5)
    scheduller.add_job(dataUpdate.monitoring_outgoing, 'interval', seconds=5)
    scheduller.add_job(dataUpdate.server_status, 'interval', seconds=10)

    scheduller.start()
