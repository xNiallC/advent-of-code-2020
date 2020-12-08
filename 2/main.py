def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  valid_passwords = []
  # Part 1
  for line in content:
    words = line.split()
    # e.g. 1-3
    amount_of_characters = words[0].split('-')

    # 1
    lower_bound = int(amount_of_characters[0])
    # 3
    upper_bound = int(amount_of_characters[1])

    # e.g. w
    desired_character = words[1][0]

    # e.g. cwwc
    password = words[2]

    desired_character_appearances_in_password = password.count(desired_character)

    if (desired_character_appearances_in_password >= lower_bound) and (desired_character_appearances_in_password <= upper_bound):
      valid_passwords.append(password)

  print(len(valid_passwords))

  valid_passwords_2 = []
  # Part 2
  for line in content:
    words = line.split()
    # e.g. 1-3
    character_positions = words[0].split('-')

    # Remove 1 to account for lack of index zero
    # 1
    lower_bound = int(character_positions[0]) - 1
    # 3
    upper_bound = int(character_positions[1]) - 1

    # e.g. w
    desired_character = words[1][0]

    # e.g. cwwc
    password = words[2]

    print(line)
    print(lower_bound)
    print(upper_bound)

    is_at_lower_bound = password[lower_bound] == desired_character
    is_at_upper_bound = password[upper_bound] == desired_character

    if (is_at_lower_bound and not is_at_upper_bound) or (is_at_upper_bound and not is_at_lower_bound):
      valid_passwords_2.append(password)

  print(len(valid_passwords_2))

if __name__ == '__main__':
  main()