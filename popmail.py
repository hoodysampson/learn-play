import poplib,getpass,sys
import base64

mailserver='pop.139.com'
mailuser='15901993013@139.com'
mailpswd=getpass.getpass('Password for %s?' % mailuser)

print('Connecting....')
server=poplib.POP3(mailserver)
server.user(mailuser)
server.pass_(mailpswd)

try:
    print(str(server.getwelcome(),'utf-8'))
    msgCount,mboxSize=server.stat()
    print('There are', msgCount, 'mail messages, size ', mboxSize)
    msginfo=server.list()
    for i in range(msgCount):
        msgnum=i+1
        msgsize=msginfo[1][i].split()[1]
        resp,hdrlines,octets=server.top(msgnum,0)
        print('-'*80)
        print('[%d: octets=%d, size=%s'%(msgnum,octets,msgsize))
        # with open('encode.txt', 'wb') as file:
        for line in hdrlines:
                # file.writelines(bytes(line))
            print(line.decode('gb2312')) #decoding the content later
        if input('Print?') in ['y','Y']:
            with open('encode.txt','wb') as file:
                for line in server.retr(msgnum)[1]:
                    file.write(line)
                    print(line)
                    # print(line.decode('gb2312'))
        if input('Delete?') in ['y','Y']:
            print('deleting')
            server.dele(msgnum)
        else:
            print('skipping')
finally:
    server.quit()
input('Bye.')
