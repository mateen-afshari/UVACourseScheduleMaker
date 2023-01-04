from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime

register = template.Library()

@register.filter(name='convertTime')
@stringfilter
def convertTime(value):
    if value != ("{"+"{"+"y:meetings}") and value != "":
        arr = value.split(".")
        firstTime = arr[0]+":"+arr[1]
        firstTime = datetime.strptime(firstTime, "%H:%M")
        return str(firstTime.strftime("%I:%M %p"))
    return value


@register.filter(name='sortMeeting')
def sortMeeting(value):
    for i in range(len(value)):
        if value[i]["meetings"] == []:
            value[i]["meetings"] = [{'days': '-', 'start_time': '', 'end_time': '', 'facility_description': '-'}]

    weekdays = ["MoTuWeThFrSa","MoTuWeThFr", "MoTuWeTh", "MoTuWeFr", "MoTuWe","MoWeTh","MoWeFr","MoTu", "MoWe", "MoTh", "MoFr","TuWeTh", "TuThFr", "TuWe","TuTh","TuFr", "WeTh","WeFr", "ThFr", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su", "-"]
    weekdaySet = set(weekdays)
    classType = ["LEC", "SEM", "DIS", "LAB", "IND", "SPS", "PRA", "WKS", "STO", "CLN", "DRL"]
    classTypeSet = set(classType)


    return sorted(value, key=lambda valdict: (classType.index(valdict["component"]) if (valdict["component"] in classTypeSet) else len(classType)-1, weekdays.index(valdict["meetings"][0]["days"]) if (valdict["meetings"][0]["days"] in weekdaySet) else len(weekdays)-1, valdict["meetings"][0]["start_time"]))

@register.filter(name='splitDays')
def splitDays(value):
    if str(value) == "-" or str(value) == "" or str(value) == " ":
        return value
    return str(value).split(" ")

@register.filter(name='splitTimes')
def splitTimes(value):
    if str(value) == "-" or str(value) == "" or str(value) == " ":
        return value
    return str(value).split("  ")
