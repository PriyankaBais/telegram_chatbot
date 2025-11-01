from config import *
import telebot
import openai


chatStr=''

def ChatModel(prompt):
    global chatStr
    openai.api_key=OPENAI_KEY
    chatStr += f"Death: {prompt}\nJarvis: "
    response = openai.completions.create(
        model="davinci-002",
        prompt="",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    print(response)
    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']


bot=telebot.TeleBot(BOT_API)


@bot.message_handler(['start'])
def start(message):
    # if message.from_user.id in myid:
        bot.reply_to(message, "welcome to priya bais telegram death bot")
    #else:
        print("someone other try to access our bot:", message.text)

   
@bot.message_handler(['how_are_you'])
def how_are_you(message):
    # if message.from_user.id in myid:
        bot.reply_to(message, "i am fine ")
    # else:
        print("someone other try to access our bot:", message.text)




@bot.message_handler()
def chat(message):
    if message.from_user.id in myid:
        try:
            reply=ChatModel(message.text)
            bot.reply_to(message, reply)
        except Exception as e:
            print(e)
            bot.reply_to(message,e)
        else:
            print("someone other try to access our bot")



print("bot started....")
bot.polling()