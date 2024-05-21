
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(str_input: str) -> str:
    return str_input[-1] if len(str_input) > 1 else ''

nums_sorted = sorted(nums, key=last_char, reverse=True)

