import datetime

class Measurement():
    measurementTime = datetime
    measurementValue = 0.0
    measurementType = ''

    def __init__(self,time,mtype,value):
        self.measurementTime = time
        self.measurementType = mtype
        self.measurementValue = value
    
    # auf 5-Minuten Raster gerundeten datetime-String erhalten
    def get_rounded_datetime(self):
        new_minute = (self.measurementTime.minute // 5 + 1) * 5
        new_datetime = self.measurementTime
        tdSeconds = datetime.timedelta(seconds=self.measurementTime.second)
        tdMinutes = datetime.timedelta(minutes=new_minute - self.measurementTime.minute)
        new_datetime -= tdSeconds
        new_datetime += tdMinutes
        return str(new_datetime)

    # aktuelles datetime-Objekt auf 5-Minuten Raster runden
    def round_datetime(self):
        new_minute = (self.measurementTime.minute // 5 + 1) * 5
        self.measurementTime -= datetime.timedelta(seconds=self.measurementTime.second)
        self.measurementTime = self.measurementTime + datetime.timedelta(minutes=new_minute - self.measurementTime.minute)

    # Bereich des aktuellen datetime-Objekts bestimmen und erhalten
    def set_interval(self):
        self.interval = {
            "start": self.measurementTime - datetime.timedelta(minutes=5),
            "end": self.measurementTime
        }

def get_interval_from_string(datetimeString):
    tempDtObject = datetime.datetime.strptime(datetimeString,'%Y-%m-%d %H:%M:%S')
    interval = {
        "start": tempDtObject - datetime.timedelta(minutes=5),
        "end": tempDtObject
    }
    return interval