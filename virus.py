import os
if os.path.exists("file.vbs"):
  print("Run the batch file: file.vbs")
else:
  file_code = "x=msgbox('Warning: if you shutdown your computer or delete this program your computer will be destroyed!', 0, 'You Fell For It!')"
  vbs = open("file.vbs", "w")
  vbs.write(file_code)
  print("Open the file: file.vbs")
