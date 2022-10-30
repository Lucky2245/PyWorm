import os
if os.path.exists("love.vbs"):
  print("Open the file love.vbs")
else:
  file_code = ""
  vbs = open("love.vbs", "w")
  vbs.write(file_code)
  print("Open the file love.vbs")
