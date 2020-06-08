import datetime

# subtracting dates
def sbtrctDts(dt1 : datetime.datetime, dt2: datetime.datetime) -> float:
    dt1 = dt1
    dt2 =  dt2

    if not(int(str((dt1 - dt2).days)) <= 0):
        diff = (dt1 - dt2)
    elif int(str((dt1 - dt2).days)) == 0 and int(str((dt1 - dt2).seconds)):
        diff = (dt1 - dt2)
    else:
        diff = (dt2 - dt1)

    # condition to be met

    #returns year difference
    if int(int(str(diff.days)) / 365) > 1:
        return f'{int(int(str(diff.days)) / 365)} yrs ago'

    #returns year when it is exactly one
    elif int(str(diff.days)) == 365:
        return f'{int(int(str(diff.days)) / 365)} yr ago'

    # returns month difference
    elif int(int(str(diff.days)) / 28) > 1:
        return f'{int(int(str(diff.days)) / 28)} mnths ago'

    # returns month difference if it is exactly one
    elif int(int(str(diff.days)) / 28) == 1:
        return f'{int(int(str(diff.days)) / 28)} mnth ago'

    # returns days difference
    elif int(str(diff.days)) > 0 and not(int(str(diff.days)) == 1):
        return f'{int(str(diff.days))} dys ago'

    # returns days difference when the difference is exactly one
    elif int(str(diff.days)) == 1:
        return f'{int(str(diff.days))} dy ago'

    # returns hour difference
    elif int(str(diff.seconds)) >= 3600:
        return f'{int(int(str(diff.seconds)) / 3600)} hrs ago'

    # returns minute difference
    elif int(str(diff.seconds)) >= 60:
        return f'{int(int(str(diff.seconds)) / 60)} mins ago'

    # return seconds difference
    else:
        return f'{int(str(diff.seconds))} sec ago'


def main():
    # test whether reverse also works and also years
    dt1 = sbtrctDts(datetime.date(2005,12,25),datetime.date(2000,11,2))
    print(dt1)

    dt2 = sbtrctDts(datetime.date(2000,11,2),datetime.date(2005,12,25))
    print(dt2)

    # test for returning months
    mth = sbtrctDts(datetime.date(2005,12,25),datetime.date(2005,10,25))
    print(mth)

    # test for returning days
    dys = sbtrctDts(datetime.date(2005,12,26),datetime.date(2005,12,23))
    print(dys)

    #test for returning hours
    hrs = sbtrctDts(datetime.datetime(2005,12,25,2,0,0,0),datetime.datetime(2005,12,25,1,0,0,0))
    print(hrs)

    #test for returning minutes
    min = sbtrctDts(datetime.datetime(2005,12,25,2,50,0,0),datetime.datetime(2005,12,25,2,0,0,0))
    print(min)

    # test for returning seconds
    sec = sbtrctDts(datetime.datetime(2005,12,25,2,0,10,0),datetime.datetime(2005,12,25,2,0,0,0))
    print(sec)

if __name__ == "__main__":
    main()
