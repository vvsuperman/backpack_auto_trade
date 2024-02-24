from datetime import date, datetime

import time
import os 

import schedule
import exchange
import logging

def log_init():
    logging.basicConfig(filename='log.txt',
                     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                     level=logging.INFO)

if __name__ == "__main__":

    log_init()
    logging.info("任务开始")

    # api json数组 api_key, api_secret
    apis=[
         
         ]
    
    # 每次刷的量
    vol =1000
       
    def job():
        for api in apis:
           exchange.foo(api["api_key"], api["api_secret"], vol)      
            
    schedule.every().day.at("22:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

    

