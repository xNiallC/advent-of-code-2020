def execute_code(instruction, value):
  accumulator_modifier = 0
  index_modifier = 1
  if instruction == 'acc':
    accumulator_modifier = value
  elif instruction == 'jmp':
    index_modifier = value
  return index_modifier, accumulator_modifier

def fix_operator(instruction):
  if instruction['type'] == 'jmp':
    return { 'type': 'nop', 'value': instruction['value']}
  if instruction['type'] == 'nop':
    return { 'type': 'jmp', 'value': instruction['value']}
  return instruction

def test_execution(instructions):
  accumulator = 0
  iterator_index = 0
  instructions_completed = []

  while True:
    # If already done, break
    if iterator_index in instructions_completed:
      return { 'success': False, 'reason': 'LOOPING. Accumulator: ' + str(accumulator), 'accumulator': accumulator}
      break
    # Get current instruction
    try:
      curr_instruction = instructions[iterator_index]
    except:
      print(accumulator)
      if iterator_index == len(instructions):
        return { 'success': True, 'reason': 'Reached end! Accumulator: ' + str(accumulator), 'accumulator': accumulator}
      break

    # Track completed instructions
    instructions_completed.append(iterator_index)

    index_modifier, accumulator_modifier = execute_code(curr_instruction['type'], curr_instruction['value'])

    iterator_index += index_modifier
    accumulator += accumulator_modifier

def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]


  instructions = []
  for index, line in enumerate(content):
    line_content = line.split(' ')
    instruction = line_content[0]
    instruction_value = line_content[1]

    operator = instruction_value[0]
    instruction_value_number = int(instruction_value[1:])
    instruction_value_number = -instruction_value_number if operator == '-' else instruction_value_number
    instructions.append({
      'type': instruction,
      'value': instruction_value_number,
      'index': index
    })

  victory_values = []
  for index, instruction in enumerate(instructions):
    result = test_execution(instructions)
    if result['success'] == False:
      print('FAILED! Swapping... Accumulator: ' + str(result['accumulator']))
      updated_instructions = instructions[:]
      updated_instruction = fix_operator(instruction)
      updated_instructions[index] = updated_instruction
      new_result = test_execution(updated_instructions)
      if new_result['success'] == True:
        print('VICTORY! Accumulator: ' + str(new_result['accumulator']))
        print('swappedy dappedy + ' + str(index))
        victory_values.append(result['accumulator'])
        break
    if result['success'] == True:
      print('VICTORY! Accumulator: ' + str(result['accumulator']))
      victory_values.append(result['accumulator'])
      break


if __name__ == '__main__':
  main()