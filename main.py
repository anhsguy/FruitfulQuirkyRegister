def hour_to_minutes(hours):
  if not isinstance(hours, (int,float)):  
    # raise TypeError('Hours must be a number')
    return 'hour should be int or float'
  return hours * 60  
