# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import smtplib 

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")
        # try: 
        #     #Create your SMTP session 
        #     smtp = smtplib.SMTP('smtp.gmail.com', 587) 

        # #Use TLS to add security 
        #     smtp.starttls() 

        #     #User Authentication 
        #     smtp.login("habivrobin3@gmail.com","ronjos4882")

        #     #Defining The Message 
        #     message = "Message_you_need_to_send" 

        #     #Sending the Email
        #     smtp.sendmail("habivrobin3@gmail.com", "josphatkips@gmail.com",message) 

        #     #Terminating the session 
        #     smtp.quit() 
        #     print ("Email sent successfully!") 

        # except Exception as ex: 
        #     print("Something went wrong....",ex)

        return []
