import os
import subprocess
if os.path.exists("file.bat"):
  print("Run the batch file: file.bat")
else:
  file_code = "@echo off echo 'Your computer has been infected. Deleting the virus will result in your computer being destroyed. If you reset your computer your computer will be destroyed!' "
  bat = open("file.bat", "w")
  bat.write(file_code)
  print("Open the file: file.bat")
