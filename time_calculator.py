import re

def add_time(time_now, time_add, day='None'):

    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday']

# extract time now as int
    try:
        time = re.findall('[0-9]+',time_now)
        ampm = re.findall('[A-P]+',time_now)
        hr_now = int(time[0])
        min_now = int(time[1])
        ampm = str(ampm[0])

#extract adding time as int
        time2 = re.findall('[0-9]+',time_add)
        hr_add = int(time2[0])
        min_add = int(time2[1])
    except:  #Error
        print('Error: input valid time')
        exit()


#Calculate minutes
    if min_now + min_add >= 60:
        min = (min_now + min_add) % 60
        hr_add = hr_add + (min_now + min_add) // 60
    else:
        min = min_now + min_add

#Calculate hours
    if ((hr_now + hr_add) // 12) % 2 == 0:  #no change am/pm
        hr = (hr_now + hr_add) % 12
        if hr == 0:
            hr = 12
        day_add = (hr_now + hr_add) // 24

    elif ((hr_now + hr_add) // 12) % 2 == 1: # change am/pm
        hr = (hr_now + hr_add) % 12
        if hr == 0:
            hr = 12
        day_add = (hr_now + hr_add) // 24
        if ampm == 'AM':
            ampm = 'PM'
        elif ampm == 'PM':
            ampm = 'AM'
            day_add = day_add+1
        else:       #Error
            print('Error: input \'AM\' or \'PM\'')
            exit()

# day later
    if day_add == 0:
        day_change = ''
    elif day_add == 1:
        day_change = '(next day)'
    else:
        day_change = '(%d days later)'%day_add

#day (Mon~Sun)
    if day != 'None':
        day = day[0].upper() + day[1:].lower()
        try:    #Error
            p = day_list.index(day)
        except:
            print("Error: input correct day")
            exit()
        p = (p + day_add)%7
        dayf = day_list[p]



# Print
    if day == 'None':
        print("Calculate: \"%s\", \"%s\"" %(time_now, time_add))
        print('-> %d:%02d %s %s'%(hr, min, ampm, day_change))
    else:
        print("Calculate: \"%s\", \"%s\", \"%s\"" %(time_now, time_add, dayf))
        print('-> %d:%02d %s, %s %s'%(hr, min, ampm, dayf, day_change))
