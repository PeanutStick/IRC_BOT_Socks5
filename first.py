import zirc, ssl, random ,asyncio ,os ,time, random
from datetime import datetime
from threading import Thread

class Bot(zirc.Client):
    def __init__(self):
        global nbbase
        win = 0
        self.connection = zirc.Socket(socket_class=zirc.Proxy(host="localhost", port=9150, protocol=zirc.SOCKS5))
        self.config = zirc.IRCConfig(host="cfkophpyl5dg3mdb7s6b5fsxvr36zuhvkpxiriurbkm7jbbyqs53goyd.onion",
            port=6667,
            nickname="Dolores",
            ident="bot",
            realname="test bot",
            channels=["#lobby"])
        self.connect(self.config)
        self.start()
    def do_welcome(self, connection, nick):
        nick = event.source.nick
        #irc.reply(event, "I'm always eVil Megatron ;"+format(nick))
        logger.info(u'Sending welcome message to {}'+format(nick))
        connection.privmsg(self.channel, u'{}: Check out our Meetup page for upcoming events: {}. Please be respectful of our members. See our code of conduct: http://pythonsd.org/pages/code-of-conduct.html'+format(nick, self.MEETUP_PAGE))
    def sshrep(line):
        print('ok')
        print('line')
        
    def on_privmsg(self, event, irc, win):
        nick = event.source.nick
        print(event)
        if " ".join(event.arguments).startswith("sTaY eViL"):
            irc.reply(event, "I'm always eVil Megatron ;")
            
        if " ".join(event.arguments).startswith("$peanut"):
            irc.reply(event, format(nick)+" ... no I'm Dolores")
            
        if " ".join(event.arguments).startswith("$time"):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            #we can have some information on you with that ...
    
            irc.reply(event, format(current_time))
            #print(nick)
            
        if " ".join(event.arguments).startswith("$ping"):
            irc.reply(event, format(nick)+"...no I don't play with you ")
            #print(nick)
            
        if " ".join(event.arguments).startswith("$help"):
            print("".join(event.arguments))
            irc.reply(event,",1 #COMMANDE# ")
            irc.reply(event,",1 $ping ")
            irc.reply(event,"4,1 try the bot ")
            irc.reply(event,",1 $peanut ")
            irc.reply(event,"4,1 say something nice! ")
            irc.reply(event,",1 $time ")
            irc.reply(event,"4,1 Give the time ")
            irc.reply(event,",1 coffee ")
            irc.reply(event,"4,1 Giveyou a coffee ")

        if "coffee" in str(event):
            irc.reply(event," ,--.")
            irc.reply(event,"C|<3|")
            irc.reply(event," `==' ")
        if "//www.youtu" in str(event):
            url = "".join(event.arguments)
            print(url)
            import scrap2
            scrap2.youtube(url)
            print(scrap2.val)
            for line in scrap2.val.splitlines() :
                irc.reply(event,"9,1"+line)
        #SSH don't work for the moment
        if " ".join(event.arguments).startswith("$ssh"):
            ssh = "".join(event.arguments)
            print("ok")
            print(ssh)
            ssh_conf = ssh.split()
            if len(ssh_conf) == 5:
                irc.reply(event,"9,1 #we try to connect... ")
                user = ssh_conf[1]
                passwd = ssh_conf[2]
                host = ssh_conf[3]
                port = ssh_conf[4]
                import sshviator
                sshviator.ssh_tor(user,passwd,host,port)
                #print(sshviator.line)
                irc.reply(event,"current IP @ : "+sshviator.external_ip1)
                irc.reply(event,sshviator.linessh)
##                irc.reply(event,"User :"+user)
##                irc.reply(event,"Password :"+passwd)
##                irc.reply(event,"IP :"+host)
##                irc.reply(event,"Port :"+port)
##                irc.reply(event,"current IP @ : "+sshviator.external_ip1)
                
            else:
                irc.reply(event,"9,1 #ssh username passwd ip port ")
                print("nop")
            #irc.reply(event, scrap2.val)
        if "love" in str(event):
            a = random.choice([format(nick)+"... no one  ", format(nick)+" maybe me... maybe.   ", format(nick)+" your mother  ",format(nick)+"I love you so much <3  ",format(nick)+" Jaxx love everyone  ",format(nick)+" let's take a shower together, I will show you... (‿ˠ‿) "])
            print(a)
            time.sleep(3)
            irc.reply(event, a)

Bot()
