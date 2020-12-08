import re

def is_valid(key, value):
  if key == 'byr':
    return (len(value) == 4) and (1920 <= int(value) <= 2002)
  if key == 'iyr':
    return (len(value) == 4) and (2010 <= int(value) <= 2020)
  if key == 'eyr':
    return (len(value) == 4) and (2020 <= int(value) <= 2030)
  if key == 'hgt':
    if ('cm' not in value) and ('in' not in value): return False
    measurement_system = value[-2:]
    num_value = int(value[:-2])
    if measurement_system == 'cm':
      return (150 <= num_value <= 193)
    if measurement_system == 'in':
      return (59 <= num_value <= 76)
  if key == 'hcl':
    return (len(value) == 7) and (True if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value) else False)
  if key == 'ecl':
    return (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
  if key == 'pid':
    return len(value) == 9

def main():
  mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  optional_fields = ['cid']

  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  # Sorting the content into passports
  passports = []
  current_passport = {}
  for line in content:
    # If its not a blank newline, its part of the current passport
    if line != '':
      # Get the various key value pairs from the line
      line_details = line.split()
      for key_value_pair in line_details:
        # Seperate the key value pairs into variables
        key_value = key_value_pair.split(':')
        key = key_value[0]
        value = key_value[1]
        # Assign to current passport
        current_passport[key] = value
    # If we reached a newline, we are done with current passport, so add to list
    else:
      passports.append(current_passport)
      current_passport = {}
  # Handle final passport
  passports.append(current_passport)
  
  num = 0
  for passport in passports:
    passport_keys = passport.keys()
    allowed = True
    keys_allowed = []
    for field in mandatory_fields:
      if field not in passport_keys:
        allowed = False
    for key in passport_keys:
      value = passport[key]
      if key == 'cid': keys_allowed.append(True)
      else: keys_allowed.append(is_valid(key, value))
    for allowed_status in keys_allowed:
      if allowed_status == False:
        allowed = False
    if allowed:
      num += 1
  
  print(num)




if __name__ == '__main__':
  main()