import csv
import webbrowser
import schedule, time, datetime
import os

def csv_dict_list(variables_file):
    """Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs"""
    reader = csv.DictReader(open(variables_file))
    dict_list = []
    for row in reader:
        dict_list.append(row)
    return dict_list

def open_zoom(thisClass):
    """Opens a new window if already not opened,or opens in a new tab if Chrome is already opened in your PC."""
    webbrowser.get('chrome').open(thisClass['link'])
    print("***Class of", thisClass['teacher'], "teacher has been started at ", thisClass['start_time'], "***")

def close_zoom(thisClass):
    """kills zoom process"""
    os.system("TASKKILL /F /IM zoom.exe")
    print("***Class of", thisClass['teacher'], "teacher has been ended at ", thisClass['end_time'], "***")

def schedule_class(weekday):
    """Checks for any matching weekday and schedules all the classes"""
    routine = csv_dict_list('routine.csv')
    for perEntry in routine:
        schedule.every().monday.at('4:36:00').do(open_zoom, url = 'https://www.google.com')
        break
        # if perEntry["weekday"] == weekday:
        #     getattr(schedule.every(), weekday).at(perEntry['start_time']).do(open_zoom, thisClass = perEntry)
        #     getattr(schedule.every(), weekday).at(perEntry['end_time']).do(close_zoom, thisClass = perEntry)
            # schedule.every().friday.at('13:05').do(open_url, url = 'https://www.google.com')

#index to weekdays
weekDays = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")

#initializing url opening in chrome
chromeLocation = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromeLocation))

#gets todays weekday
todays_weekday = weekDays[datetime.datetime.today().weekday()]
print('Automating classes for', todays_weekday)
schedule_class(todays_weekday)

#keeps running and does the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(30)