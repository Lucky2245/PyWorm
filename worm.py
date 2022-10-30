import os
if os.path.exists("love.bat"):
  print("Open the file love.bat")
else:
  file_code = ""
  vbs = open("love.bat", "w")
  vbs.write(file_code)
  print("Open the file love.bat")
