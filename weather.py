# -*- coding: utf8 -*-
#!/usr/bin/python
local_encoding = 'cp850'
deg = u'\xb0'.encode(local_encoding)

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class weather:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://weather.com")
        self.city_and_state = ""
        self.current_temp = 0
        self.feels_like = 0
        self.high = 0
        self.low = 0
        self.todays_wind = ""
        self.sunrise = ""
        self.sundown = ""
        # Consider leaving out
        self.uv_index = 0
        self.humidity = 0
        self.dew_point = 0
        self.pressure = 0
        self.visibility = 0
        # End leave out

    def get_element_by_xpath(self, xpath):
        return self.browser.find_element_by_xpath(xpath).text

    def get_weather(self, city_and_state):
        self.city_and_state = city_and_state
        search_bar_xpath =   "/html[@class='js applicationcache geolocation history postmessage svg websockets promises fetch localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl cssgradients multiplebgs opacity no-csspositionsticky rgba inlinesvg hsla supports svgclippaths smil no-touchevents fontface generatedcontent textshadow indexeddb indexeddb-deletedatabase cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions no-touch']/body[@class='html front not-logged-in no-sidebars i18n-en-US page-panels ']/div[@class='berlin clearfix']/div[@id='wx-hero-wrap']/header[@id='wx-header-wrap']/div[@class='panel-pane content module-padding width-100 float-left column data-eq-pane-xl']/div[@class='pane-content ']/div[@class='mini-panel today glomo-header']/div[@class='sub-header']/div[@class='region search-region']/div[@class='glomo_search width-100 float-left panel-pane content column module-padding data-eq-pane']/section[@class='unified-search ng-hide']/div[@class='input-rebase']/form/input[@class='input--search']"
        current_temp_xpath = "/html[@class='js applicationcache geolocation history postmessage svg websockets promises fetch localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl cssgradients multiplebgs opacity no-csspositionsticky rgba inlinesvg hsla supports svgclippaths smil no-touchevents fontface generatedcontent textshadow indexeddb indexeddb-deletedatabase cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions no-touch']/body[@class='html not-front not-logged-in no-sidebars page-weather page-weather-today page-weather-today-l page-weather-today-l-template i18n-en-US section-weather page-panels ']/div[@class='berlin clearfix']/div[@id='wx-hero-wrap']/div[@id='wx-hero-content']/div[@class='hero-flex center-col']/section[@class='region hero_left']/div[@class='today_nowcard width-100 float-left panel-pane content column module-padding data-eq-pane-sm']/section[@id='js-nowcard']/div[@class='today_nowcard-main panel [[ ui.textClass ]]']/div[@class='today_nowcard-section today_nowcard-condition']/div[@class='today_nowcard-temp']/span/span[@class='dir-ltr']"
        feels_like_xpath =   "/html[@class='js applicationcache geolocation history postmessage svg websockets promises fetch localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl cssgradients multiplebgs opacity no-csspositionsticky rgba inlinesvg hsla supports svgclippaths smil no-touchevents fontface generatedcontent textshadow indexeddb indexeddb-deletedatabase cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions no-touch']/body[@class='html not-front not-logged-in no-sidebars page-weather page-weather-today page-weather-today-l page-weather-today-l-template i18n-en-US section-weather page-panels ']/div[@class='berlin clearfix']/div[@id='wx-hero-wrap']/div[@id='wx-hero-content']/div[@class='hero-flex center-col']/section[@class='region hero_left']/div[@class='today_nowcard width-100 float-left panel-pane content column module-padding data-eq-pane-sm']/section[@id='js-nowcard']/div[@class='today_nowcard-main panel [[ ui.textClass ]]']/div[@class='today_nowcard-section today_nowcard-condition']/div[@class='today_nowcard-feels']/span[@class='deg-feels']/span[@class='dir-ltr']"
        high_xpath =         "/html[@class='js applicationcache geolocation history postmessage svg websockets promises fetch localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl cssgradients multiplebgs opacity no-csspositionsticky rgba inlinesvg hsla supports svgclippaths smil no-touchevents fontface generatedcontent textshadow indexeddb indexeddb-deletedatabase cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions no-touch']/body[@class='html not-front not-logged-in no-sidebars page-weather page-weather-today page-weather-today-l page-weather-today-l-template i18n-en-US section-weather page-panels ']/div[@class='berlin clearfix']/div[@id='wx-hero-wrap']/div[@id='wx-hero-content']/div[@class='hero-flex center-col']/section[@class='region hero_left']/div[@class='today_nowcard width-100 float-left panel-pane content column module-padding data-eq-pane-sm']/section[@id='js-nowcard']/div[@class='today_nowcard-main panel [[ ui.textClass ]]']/div[@class='today_nowcard-section today_nowcard-condition']/div[@class='today_nowcard-hilo']/span[@class='deg-hilo-nowcard'][1]/span[@class='dir-ltr']"
        low_xpath =          "/html[@class='js applicationcache geolocation history postmessage svg websockets promises fetch localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl cssgradients multiplebgs opacity no-csspositionsticky rgba inlinesvg hsla supports svgclippaths smil no-touchevents fontface generatedcontent textshadow indexeddb indexeddb-deletedatabase cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions no-touch']/body[@class='html not-front not-logged-in no-sidebars page-weather page-weather-today page-weather-today-l page-weather-today-l-template i18n-en-US section-weather page-panels ']/div[@class='berlin clearfix']/div[@id='wx-hero-wrap']/div[@id='wx-hero-content']/div[@class='hero-flex center-col']/section[@class='region hero_left']/div[@class='today_nowcard width-100 float-left panel-pane content column module-padding data-eq-pane-sm']/section[@id='js-nowcard']/div[@class='today_nowcard-main panel [[ ui.textClass ]]']/div[@class='today_nowcard-section today_nowcard-condition']/div[@class='today_nowcard-hilo']/span[@class='deg-hilo-nowcard'][2]/span[@class='dir-ltr']"
        todays_wind_xpath =  "/html[@class='js applicationcache geolocation history postmessage svg websockets promises fetch localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl cssgradients multiplebgs opacity no-csspositionsticky rgba inlinesvg hsla supports svgclippaths smil no-touchevents fontface generatedcontent textshadow indexeddb indexeddb-deletedatabase cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions no-touch']/body[@class='html not-front not-logged-in no-sidebars page-weather page-weather-today page-weather-today-l page-weather-today-l-template i18n-en-US section-weather page-panels ']/div[@class='berlin clearfix']/div[@class='center-col wx-mid-wrap']/main[@id='wx-main']/div[@class='today_looking_ahead width-100 float-left panel-pane content column module-padding data-eq-pane-sm']/section[@class='today-looking-ahead panel data-eq-looking-ahead-sm']/div[@class='wx-module-status-ready']/div[@class='panel-footer']/div/ul[@class='wx-details-block']/li[@class='wx-detail'][1]/span[@class='wx-detail-text']/span[@class='wx-detail-value wx-wind dir-ltr']"
        sunrise_xpath =      "/html[@class='js applicationcache geolocation history postmessage svg websockets promises fetch localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl cssgradients multiplebgs opacity no-csspositionsticky rgba inlinesvg hsla supports svgclippaths smil no-touchevents fontface generatedcontent textshadow indexeddb indexeddb-deletedatabase cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions no-touch']/body[@class='html not-front not-logged-in no-sidebars page-weather page-weather-today page-weather-today-l page-weather-today-l-template i18n-en-US section-weather page-panels ']/div[@class='berlin clearfix']/div[@class='center-col wx-mid-wrap']/main[@id='wx-main']/div[@class='today_looking_ahead width-100 float-left panel-pane content column module-padding data-eq-pane-sm']/section[@class='today-looking-ahead panel data-eq-looking-ahead-sm']/div[@class='wx-module-status-ready']/div[@class='panel-footer']/div/ul[@class='wx-details-block']/li[@class='wx-detail'][4]/span[@class='wx-detail-text']/span[@class='wx-detail-value']/span[@class='wx-dsxdate'][1]"
        sundown_xpath =      "/html[@class='js applicationcache geolocation history postmessage svg websockets promises fetch localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl cssgradients multiplebgs opacity no-csspositionsticky rgba inlinesvg hsla supports svgclippaths smil no-touchevents fontface generatedcontent textshadow indexeddb indexeddb-deletedatabase cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions no-touch']/body[@class='html not-front not-logged-in no-sidebars page-weather page-weather-today page-weather-today-l page-weather-today-l-template i18n-en-US section-weather page-panels ']/div[@class='berlin clearfix']/div[@class='center-col wx-mid-wrap']/main[@id='wx-main']/div[@class='today_looking_ahead width-100 float-left panel-pane content column module-padding data-eq-pane-sm']/section[@class='today-looking-ahead panel data-eq-looking-ahead-sm']/div[@class='wx-module-status-ready']/div[@class='panel-footer']/div/ul[@class='wx-details-block']/li[@class='wx-detail'][4]/span[@class='wx-detail-text']/span[@class='wx-detail-value']/span[@class='wx-dsxdate'][2]"

        search_bar = self.browser.find_element_by_xpath(search_bar_xpath)
        search_bar.send_keys(city_and_state)
        search_bar.send_keys(Keys.RETURN)

        time.sleep(5)

        self.current_temp = self.get_element_by_xpath(current_temp_xpath)
        self.feels_like = self.get_element_by_xpath(feels_like_xpath)
        self.high = self.get_element_by_xpath(high_xpath)
        self.low = self.get_element_by_xpath(low_xpath)
        self.todays_wind = self.get_element_by_xpath(todays_wind_xpath)
        self.sunrise = self.get_element_by_xpath(sunrise_xpath)
        self.sundown = self.get_element_by_xpath(sundown_xpath)

        return 

    def print_report(self):
        print "Here's today's weather in " + self.city_and_state + ": "
        print "Currently: " + self.current_temp
        print "Feels like: " + self.feels_like
        print "High: " + self.high
        print "Low:  " + self.low
        print "Wind: " + self.todays_wind
        print "Sunrise: " + self.sunrise
        print "Sundown: " + self.sundown
        return

    def __del__(self):
        self.browser.close()

def main():
    weather_report = weather()
    weather_report.get_weather("Cookeville, TN")
    weather_report.print_report()
    # time.sleep(5)
    return

if __name__ == "__main__":
    main()