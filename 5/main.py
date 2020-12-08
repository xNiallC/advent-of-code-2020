import math

def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  # 128 Rows on plane, 0-127
  rows = 127
  columns = 7

  highest_seat = 0
  all_seats = []

  for seat_code in content:
    row = 0
    column = 0

    row_upper_bound = rows
    row_lower_bound = 0

    column_upper_bound = columns
    column_lower_bound = 0

    seat_id = 0

    for letter in seat_code:
      if letter == 'F' or letter == 'B':
        half_row = math.floor(row_upper_bound / 2)
        diff = math.ceil((row_upper_bound - row_lower_bound) / 2)
        if (row_upper_bound - row_lower_bound) == 1:
          if letter == 'F':
            row = row_lower_bound
          else:
            row = row_upper_bound
        if letter == 'F':
          row_upper_bound = (row_upper_bound - diff)
        else:
          row_lower_bound = (row_lower_bound + diff)
      if letter == 'R' or letter == 'L':
        half_column = math.floor(column_upper_bound / 2)
        diff = math.ceil((column_upper_bound - column_lower_bound) / 2)
        if (column_upper_bound - column_lower_bound) == 1:
          if letter == 'L':
            column = column_lower_bound
          else:
            column = column_upper_bound
        if letter == 'L':
          column_upper_bound = (column_upper_bound - diff)
        else:
          column_lower_bound = (column_lower_bound + diff)
    seat_id = ((row * 8) + column)     
    if seat_id > highest_seat:
      highest_seat = seat_id
    all_seats.append(seat_id)

  all_seats.sort()
  for index, seat in enumerate(all_seats):
    curr_seat = seat
    prev_seat = all_seats[index - 1] if index > 0 else None
    next_seat = all_seats[index + 1] if (index != (len(all_seats) - 1)) else None
    if prev_seat and next_seat:

      if (next_seat - prev_seat) > 2: print(curr_seat)




if __name__ == '__main__':
  main()