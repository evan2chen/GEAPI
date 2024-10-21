import os

from groq import Groq

client = Groq(
    api_key="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",
)



#GEA_Chat Object: since each chat is confined in one GEA_Chat object
# we can have multiple chats running at once if we have multiple objects

#usage:
#   bot = GEA_Chat()
#   bot.explain("Fundamental Theorem of Calculus")
#   bot.chat("how can I use this in my daily life as a gooner?")


#all code blocks are commented. submit $feedback if anything is unclear
 
class GEA_Chat:
    #explainer_type and model are for future updates. 
    #for now GEA_Chat() can be called with no parameters 
    def __init__(self, type:str = None, model:str = None):
        self.session_token = None
        self.explainer_type = type
        self.model = model

#========================================================
# statuc functions: 1

    def static_explain(message: str):
        chat_completion = client.chat.completions.create(
            messages=[
            {   
                "role": "system",

                #content will depend on self.explainer_type
                #for now it will be hard coded.
                "content": 
                """
                You will be prompted with a subject or a concept, like "Bayes Theorem" or "Sunk Cost Fallacy". 
                Your job is to explain this concept in an intuitive way and 
                provide at least one example of its application. 
                Use mathematical expressions if and only if it is imperative to or improves your explanation.
                If the prompt is not an academic-related concept, 
                or if the concept being prompted is unclear or too broad, 
                respond with: "Better question please"
                All your responses will be at most 300 words long.
                Follow-up questions may be asked.
                """
            },
                
            {
                "role": "user",
                "content": message
            }],
            model="llama3-8b-8192",
        )
        
        return chat_completion.choices[0].message.content
#=========================================================
# public functions: 2 

    # $explain <message>
    # starts a NEW SESSION and returns the 
    # gpt response in the new session's context
    def explain(self, message:str): #a sender variable will be implemented soon 

        self.__end_session()
        self.__create_session()

        return self.chat(message)


    # $chat <message>
    #returns the gpt response with the current session's context
    # if there is no active session, it returns an error message.
    def chat(self, message:str):

        #check if session exists
        # if self.session_token is None:
        #     return "No active chat. Use $explain <message> to start a new session."


        #we can do some filtering here for bad input in messages

        #send the chat request
        chat_completion = client.chat.completions.create(
            user= self.session_token,
            messages=[{
                "role": "user",
                "content": message
            }],
            model="llama3-8b-8192",
        )

        return chat_completion.choices[0].message.content
    
#========================================================================
#private helper functions: 2

    #creates a new session with system prompt configuration.
    def __create_session(self):
        client.chat.completions.create(
            user= self.session_token,
            messages=[{
                "role": "system",

                #content will depend on self.explainer_type
                #for now it will be hard coded.
                "content": 
                """
                You will be prompted with a subject or a concept, like "Bayes Theorem" or "Sunk Cost Fallacy". 
                Your job is to explain this concept in an intuitive way and 
                provide at least one example of its application. 
                Use mathematical expressions if and only if it is imperative to or improves your explanation.
                If the prompt is not an academic-related concept, 
                or if the concept being prompted is unclear or too broad, 
                respond with: "Better question please"
                All your responses will be at most 300 words long.
                Follow-up questions may be asked.
                """
            }],

            #model will depend on self.model
            #for now it will be hard coded
            model="llama3-8b-8192",
        )

    #ends the current session
    def __end_session(self):
        if self.session_token is not None:
            client.session.end(self.session_token)
            # self.session_token = None
    



