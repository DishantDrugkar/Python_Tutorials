import os
import datetime
import shutil

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name, 'zip', source)

source = "/Users/dishantdrugkar/Documents/Programming/VS CODE/PYTHON DEVELOPMENT"
destination = "/Users/dishantdrugkar/Documents/Programming/VS CODE/PYTHON DEVELOPMENT/Python/Backups"
backup_files(source, destination)