def get_intersection(group):
  if len(group) > 0:
    return list(set(group[0]).intersection(*group))
  else: return []

def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  all_groups_total = 0

  curr_group_answers = []

  curr_group = []
  for index, line in enumerate(content):
    if line != '':
      line_answers = [answer for answer in line]
      curr_group.append(line_answers)
    else:
      list_intersection = get_intersection(curr_group)
      curr_group = []
      all_groups_total += len(list_intersection)
  all_groups_total += len(get_intersection(curr_group))

  print(all_groups_total)

if __name__ == '__main__':
  main()