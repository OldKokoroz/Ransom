import subprocess
import time
import qrcode

try:

    print("====================================================================")
    time.sleep(1)
    while True:
        value_of_qr = str(input("\nThing to direct from the Qr : "))
        if value_of_qr:
            break
        else:    
            print("\n       Invalid Input")

    time.sleep(0.5)
    while True:
        save_name = str(input("\nName to save the QR as : "))
        if save_name:    
            break
        else:    
            print("\n       Invalid Input")

    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_M, 
        box_size=100, 
        border=4)

    qr.add_data(value_of_qr)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{save_name}.jpeg")
    
    where_qr = subprocess.check_output("pwd", shell=True, text=True)
   
    print(f"""\nCreation : {save_name} \n\n        Location : {where_qr} """)

    time.sleep(1)
    print("QR Created | Process Successful ✔\n")

    print("====================================================================")

except KeyboardInterrupt:
    print("Exiting the Program...")
    exit()
    
