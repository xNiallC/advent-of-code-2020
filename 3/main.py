def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  # Initial values/help
  tree = '#'
  blank_snow = ''

  routes = [
    { 'x': 1, 'y': 1 },
    # Default route
    { 'x': 3, 'y': 1 },
    { 'x': 5, 'y': 1 },
    { 'x': 7, 'y': 1 },
    { 'x': 1, 'y': 2 }
  ]

  routes_trees_hit = []

  for route in routes:
    trees_hit = 0
    current_x_value = 0
    for index, line in enumerate(content):
      current_environment = line
      # As the current line can be considering infinitely repeating
      # While our current X is longer than the current environment
      while current_x_value >= len(current_environment):
        # We just add to itself
        current_environment += current_environment

      # We don't need to do any checks on the first line
      # Fun stuff for printing nice
      #hit_tree = False
      if index != 0:
        # Ensures we are skipping lines correctly e.g. skip 2 lines, check if current modulo is 0
        if route['y'] == 1 or (index % route['y'] == 0):
          # Check where we are in the environment
          current_environment_position = current_environment[current_x_value]
          # If we are hitting a tree
          if current_environment_position == tree:
            # Increase the trees hit value
            #hit_tree = True
            trees_hit += 1
      # Increase our X index
      # Fun stuff:
      #new_current_environment = current_environment[:current_x_value] + ('O' if not hit_tree else 'X') + current_environment[current_x_value + 1:]
      #if route['x'] == 1 and route['y'] == 2:
      #  print(new_current_environment)
      #  print(hit_tree)
      #  print(trees_hit)
      #  print('----')

      if route['y'] == 1 or (index % route['y'] == 1):
        current_x_value += route['x']

    routes_trees_hit.append(trees_hit)

  total_trees_hit = 1
  for route_trees in routes_trees_hit:
    total_trees_hit = total_trees_hit * route_trees
  
  print(total_trees_hit)
  

if __name__ == '__main__':
  main()