import os
if os.path.exists("love.bat"):
  print("Open the file love.bat")
else:
  file_code = ""
  bat = open("love.bat", "w")
  bat.write(file_code)
  print("Open the file love.bat")
