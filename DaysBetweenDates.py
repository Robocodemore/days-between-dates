date1 = input('Enter first date (dd/mm): ')

date2 = input('Enter second date (dd/mm)')

date_date1 = date1.split('/')
date_date2 = date2.split('/')

date_date1[0] = int(date_date1[0])
date_date2[0] = int(date_date2[0])

date_date1[1] = int(date_date1[1])-1
date_date2[1] = int(date_date2[1])-1

days_in_months = [31, 28,31,30,31,30,31,31,30,31,30,31]

def daysBetweenDates(date1, date2, daysMonthsBetween, month1, month2):
  noOfDates = daysMonthsBetween[month1] - date1
  daysInMonthsBetween = 0
  for i in range(month1+1, month2):
    daysInMonthsBetween += daysMonthsBetween[i]

  return noOfDates + daysInMonthsBetween + date2

print(daysBetweenDates(date_date1[0], date_date2[0], days_in_months, date_date1[1], date_date2[1]))
