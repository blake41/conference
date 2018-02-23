import types
def only_strings(array):
  return_array = []
  for element in array:
    if type(element) == types.StringType:
      return_array.append(element)
  return return_array

print only_strings(["STONES", "LAKES", 7, "HELLO"])


def only_smart_kids(kids):
  return_array = []
  for element in kids:
    for k,v in element.items():
      if v > 56:
        return_array.append(v)
  return return_array

print only_smart_kids([{"blake": 72}, {"john": 56}, {"arnold": 87}])
