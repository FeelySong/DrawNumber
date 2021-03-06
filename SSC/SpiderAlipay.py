# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import mechanize
import cookielib
from bs4 import BeautifulSoup
from random import randint
from time import sleep

def screen_login():
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    # setting
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    # br.set_debug_http(True)
    # User-Agent (this is cheating, ok?)
    br.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:33.0) Gecko/20100101 Firefox/33.0 ")]
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    # Open the login page
    r=br.open('https://auth.alipay.com/login/homeB.htm?redirectType=parent')
    html = r.read().decode('gb2312')
    br.select_form(nr=0) # Find the login form
    print br.form
    br['logonId'] = 'Your registered User name' # Set the form values
    br['password_input'] = 'Your registered User password'
    br.submit() # Submit the form

    return(br)

# read data
def get_urls(total_page_num):
    urls = []
    profiles = []
    web_url = 'http://members.lovingfromadistance.com/forumdisplay.php?18-Closing-the-Distance/page'
    for page_num in range(1, total_page_num + 1):
        browser = br.open( web_url + str(page_num) )
        # '''sleep'''
        sleep(0.01*randint(1,7))
        print page_num
        # browser = br.open('http://members.lovingfromadistance.com/forumdisplay.php?18-Closing-the-Distance/page1')
        # parse data
        soup = BeautifulSoup(browser)
        titles = soup.find_all('a', {'class', 'title'})
        users = soup.find_all('a', {'class', 'siteicon_profile'})
        for i in range(len(titles)):
            title = titles[i]['href']
            user = users[i]['href']
            title = 'http://members.lovingfromadistance.com/' + title
            profiles.append(user)
            urls.append(title)
            print title
    return urls, profiles

br = screen_login()
   

# thread_and_user = get_urls(41)
#
# thread_urls = thread_and_user[0]
# user_profiles_all = thread_and_user[1]