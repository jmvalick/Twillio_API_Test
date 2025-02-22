# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from time import sleep

#sends SMS messages
def sendSMS(self, sub):
    
    #try to use login credentials
    try:
        client = Client(sub.account_sid, sub.auth_token)
    except:
        return("messages not sent, check login info\n")

    #for each number send a message
    for num in sub.numbers:

        self.updateOutput("Number of messages sent: " + str(sub.messageCount) + \
                          "\nNumber of messages not sent: " + str(len(sub.numsNotSent)))
        
        try:
            sentMessage = client.messages \
                            .create(
                                body=sub.message,
                                from_=sub.fromNum,
                                to=num
                            )
            sub.messageCount += 1
            sleep(0.5) #delay between each send
        except:
            sub.numsNotSent.append(num)

        #update progress bar
        self.progress.configure(value=(sub.messageCount+len(sub.numsNotSent)))

        #if canceled break loop
        if(not sub.running):
            sleep(1.0)
            break

    return("Number of messages sent: " + str(sub.messageCount) + \
           "\nNumber of messages not sent: " + str(len(sub.numsNotSent)))
    
   