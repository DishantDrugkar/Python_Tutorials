import os
import datetime
import shutil

def backup_files(source, destination):
    today = datetime.date.today()
    backup_files_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_files_name.replace('.tar.gz', ' '), 'gztar', source)


source = "/Users/dishantdrugkar/Documents/Programming/VS CODE/PYTHON DEVELOPMENT"
destination = "/Users/dishantdrugkar/Documents/Programming/VS CODE/PYTHON DEVELOPMENT/Python/Backups"
backup_files(source, destination)