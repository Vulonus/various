from measurement import Measurement, get_interval_from_string
import datetime

def prepare_sampling(file):
    # INPUT: list of tuples
    print('prepare sampling')
    unsampledMeasures = list()
    print('sampling file: {}'.format(file))
    with open(file, 'r') as f:
        for row in f.readlines():
            # 2017-01-03T10:04:45
            liste = row.split(',')
            datetime_object = datetime.datetime.strptime(liste[0], '%Y-%m-%dT%H:%M:%S')
            unsampledMeasures.append(Measurement(datetime_object, liste[1], liste[2].replace('\n','')))
    print('Starting Sampling!')
    startSampling(unsampledMeasures)

def startSampling(unsampledMeasures):
    typedMeasurementList = list()
    sampledMeasures = list()
    deleteEntries = list()
    firstType = unsampledMeasures[0].measurementType
    for measure in unsampledMeasures:
        # typsichere Liste erstellen, Einträge aus alter Liste löschen.
         if measure.measurementType == firstType:
            typedMeasurementList.append(measure)
            deleteEntries.append(measure)
    unsampledMeasures = [measures for measures in unsampledMeasures if measures not in  deleteEntries]

    # samplen des ersten Typs
    sample(typedMeasurementList,sampledMeasures)

    # rekursiver Aufruf, bis alle Einträge gesampled sind und Liste leer ist.
    if unsampledMeasures:
        startSampling(unsampledMeasures)
    else:
        print('sampling complete!')


def sample(typedMeasurementList,sampledMeasures):
    deleteEntries= list()
    # Bereich des ersten elements bestimmen
    firstInterval = get_interval_from_string(typedMeasurementList[0].get_rounded_datetime())
    lastIntervalEntry = False
    for measure in typedMeasurementList:
        # Bereich muss übereinstimmen
        if get_interval_from_string(measure.get_rounded_datetime()) == firstInterval:
            # Zeitlich spätesten Eintrag im Bereich speichern und dabei alle Einträge im Bereich löschen
            if not lastIntervalEntry:
                lastIntervalEntry = measure
            elif lastIntervalEntry.measurementTime < measure.measurementTime:
                lastIntervalEntry = measure
            deleteEntries.append(measure)
    
    # neue liste erstellen, welche nur Einträge außerhalb des aktuellen Rasters enthält
    typedMeasurementList = [measures for measures in typedMeasurementList if measures not in  deleteEntries]

    # Datum-Zeit zur korrekten Ausgabe runden
    lastIntervalEntry.round_datetime()

    # Zeitlich spätesten Eintrag im Bereich in Liste speichern
    sampledMeasures.append(lastIntervalEntry)

    # rekursiver Aufruf, bis jeder Bereich des Typs gesampled wurde 
    if typedMeasurementList:
        sample(typedMeasurementList,sampledMeasures)
    else:
        # Liste nach Zeitbereichen sortieren (Frühester zuerst) und ausgeben. Sicherheitshalber liste leeren
        sampledMeasures.sort(key=lambda measure: measure.measurementTime)
        for measure in sampledMeasures:
            print('{}, {}, {}'.format(measure.measurementTime,measure.measurementType, measure.measurementValue))
        sampledMeasures.clear()
