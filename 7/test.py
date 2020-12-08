def search_for_gold_bag(bag, all_bags):
  for key, value in bag.items():
    if key == 'shiny gold': return True
    if key != 'type':
      sub_bag_info = next((b for b in all_bags if b['type'] == key), None)
      return search_for_gold_bag(sub_bag_info, all_bags)

def main():
    lst = open('2e_input.txt', 'r').read().splitlines()
    llst = []
    for line in lst:
    a,b = line.split(' contain ')
    l = [a, b]
    llst.append(l)



    #find shiny gold bags



    def Day7_1st(st = 'shiny gold', llst = llst):
    el = []
    #print(st)
    for bag in llst:
    #print(st)
    if st in bag[1]:
    el.append(bag[0])
    recbag = bag[0]
    #print(recbag)
    el += Day7_1st(recbag, llst)
    return(el)



    resv = Day7_1st('goud', vb)

    resvb = list(dict.fromkeys(resv))

    print(len(resvb))




if __name__ == '__main__':
  main()