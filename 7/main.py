def search_for_gold_bag(sub_bags, all_bags, print_path = False):
  if 'shiny gold' in sub_bags: return True
  children = []
  for bag in sub_bags:
    sub_bag_info = next((b for b in all_bags if b['type'] == bag), None)
    if print_path: print(sub_bag_info)
    if sub_bag_info:
      for key, item in sub_bag_info.items():
        if key != 'type' and key not in children and key:
          children.append(key)
  if len(sub_bags) > 0:
    return search_for_gold_bag(children, all_bags, print_path)


def bag_size(bag, all_bags):
  count = 0
  for key, sub_count in bag.items():
    if key != 'type':
      sub_bag = next((b for b in all_bags if b['type'] == key), None)
      if len(sub_bag) == 1:
        count += sub_count
      else:
        count += sub_count
        count += (bag_size(sub_bag, all_bags) * sub_count)
  return count
  

def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  bags = []
  for line in content:
    bag_data = {}

    line_data = line.split(' contain ')

    bag_type = line_data[0].replace(' bags', '')
    bag_data['type'] = bag_type

    bag_info = line_data[1].replace('bags', '')
    bag_info = bag_info.replace('bag', '')
    bag_info = bag_info.replace('.', '')
    bag_info = bag_info.split(', ')

    for info in bag_info:
      if info[0] != 'n':
        amount = int(info[0])
        amount_type = info[2:]
        bag_data[amount_type[:-1]] = amount
    bags.append(bag_data)

  total_can_contain_gold_bag = 0
  for bag in bags:
    initial_children = []
    for key, item in bag.items():
      if key != 'type' and key not in initial_children: initial_children.append(key)

    if 'shiny gold' in initial_children:
      total_can_contain_gold_bag += 1
    else:
      can_contain_gold_bag = search_for_gold_bag(initial_children, bags, bag['type'] == 'posh salmon')

      if can_contain_gold_bag:
        total_can_contain_gold_bag += 1

  #print(total_can_contain_gold_bag)

  shiny_gold = next((b for b in bags if b['type'] =='shiny gold'), None)
  print(bag_size(shiny_gold, bags))


if __name__ == '__main__':
  main()