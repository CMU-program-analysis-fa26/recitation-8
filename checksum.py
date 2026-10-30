def checksum(s):
  v = 0x1506
  for char in s:
    v = (v * 33) + ord(char)
  return v

s = input("Enter a string: ")
print("Checksum:", hex(checksum(s)))