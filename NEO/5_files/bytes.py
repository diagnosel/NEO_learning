import shutil
import os
if os.path.exists('5_files'):
    shutil.make_archive('example', 'zip', root_dir='./5_files')
else:
    print("Directory '5_files' does not exist.")

for num in [127, 255, 156]:
  print(hex(num))
  
#Щоб дізнатися, якому елементу 
# в UTF-8 відповідає символ, є функція ord (від order).
a_value = ord('A') 
print(a_value)

#Зворотна операція, коли потрібно дізнатися, 
# який символ закодований числом, наприклад 100, 
# є функція chr (скорочено від character):
print(chr(128))

print(b'Hello world!'.decode('utf-16'))