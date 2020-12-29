from selenium import webdriver
from selenium import common
from selenium.webdriver.common import keys
import time


class TwitterBot:

   
    usernameList = open('usernames.txt','r').read().splitlines()
    usernames = usernameList[0:-1]
    password = usernameList[-1]


    def __init__(self):
        self.is_logged_in = False



    def login(self,username,password):
        bot = self.browser
        bot.get('https://twitter.com/')
        time.sleep(4)

        try:
            email = bot.find_element_by_name('session[username_or_email]')
            password = bot.find_element_by_name('session[password]')
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            email = bot.find_element_by_name('session[username_or_email]')
            password = bot.find_element_by_name('session[password]')
        
        email.clear()
        password.clear()
        email.send_keys(username)
        password.send_keys(self.password)
        password.send_keys(keys.Keys.RETURN)
        time.sleep(10)
        self.is_logged_in = True


    def logout(self):
        if not self.is_logged_in:
            return 

        bot = self.browser
        bot.get('https://twitter.com/home')
        time.sleep(4)

        try:
            bot.find_element_by_xpath("//div[@data-testid='SideNav_AccountSwitcher_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath("//div[@data-testid='SideNav_AccountSwitcher_Button']").click()

        time.sleep(1)

        try:
            bot.find_element_by_xpath("//a[@data-testid='AccountSwitcher_Logout_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(2)
            bot.find_element_by_xpath("//a[@data-testid='AccountSwitcher_Logout_Button']").click()

        time.sleep(3)

        try:
            bot.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()

        time.sleep(3) 
        self.is_logged_in = False

    def run(self):
        
        for user in self.usernames:
            self.browser = webdriver.Firefox()
            self.login(user,self.password)
            time.sleep(5)
            print('LOGGED in as {}'.format(user))
            self.post_tweets()
            self.logout()
            self.browser = self.browser.quit()
            userInput = input("Restart the Router Then ... \n Press any Key to Continue....")
        print('Congrats....')




      
    def post_tweets(self):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.browser  
        tweets = open('tweets.txt','r').read().splitlines()
        for tweet in tweets:
            body = tweet
            try:
                bot.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
            except common.exceptions.NoSuchElementException:
                time.sleep(3)
                bot.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()

            time.sleep(4) 
        

            try:
                bot.find_element_by_xpath("//div[@role='textbox']").send_keys(body)
            except common.exceptions.NoSuchElementException:
                time.sleep(3)
                bot.find_element_by_xpath("//div[@role='textbox']").send_keys(body)

            time.sleep(4)
            bot.find_element_by_class_name("notranslate").send_keys(keys.Keys.ENTER)
            bot.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
            time.sleep(30)


def run():
    t = TwitterBot()
    t.run()

if __name__ == "__main__":
    run()