# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from time import sleep

#function is the same as sendSMS but adds a URL image to message
def sendMMS(self, sub):
    
    try:
        client = Client(sub.account_sid, sub.auth_token)
    except:
        return("messages not sent, check login info\n")
    
    for num in sub.numbers:

        self.updateOutput("Number of messages sent: " + str(sub.messageCount) + \
                          "\nNumber of messages not sent: " + str(len(sub.numsNotSent)))
    
        try:
            sentMessage = client.messages \
                            .create(
                                body=sub.message,
                                from_=sub.fromNum,  
                                media_url=sub.urls,
                                to=num
                            )
            sub.messageCount += 1
            sleep(0.5)
        except:
            sub.numsNotSent.append(num)

        self.progress.configure(value=(sub.messageCount+len(sub.numsNotSent)))

        if(not sub.running):
            sleep(1.0)
            break
        
    return("Number of messages sent: " + str(sub.messageCount) + \
            "\nNumber of messages not sent: " + str(len(sub.numsNotSent)))

    
