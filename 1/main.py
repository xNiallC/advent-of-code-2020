def find_values_to_2020(entries):
  for entry in entries:
    value = int(entry)
    for second_entry in entries:
      second_value = int(second_entry)
      for third_entry in entries:
        third_value = int(third_entry)
        if (value + second_value + third_value == 2020):
          return [value, second_value, third_value]

def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  values = find_values_to_2020(content)

  total = values[0] * values[1] * values[2]

  print(total)

if __name__ == '__main__':
  main()