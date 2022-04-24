import requests
import time
from pymongo import *
import requests
from bs4 import BeautifulSoup

def save_to_mongo(liepin_search_results):
    client = MongoClient()
    db = client.liepin
    collection = db.java
    try:
        if collection.insert_one(liepin_search_results):
            print('save to mongo succeed')
    except Exception as e:
        print(e.args)
        print('fail to save to mongo')

if __name__ == '__main__':
    url_pattern = "https://www.liepin.com/zhaopin/?headId=73f92ed1268fcf7607f7060f976fc2f7&ckId=t8thopwte9foere9q7ztk11hltjmkqub&oldCkId=73f92ed1268fcf7607f7060f976fc2f7&fkId=vk1tzxh58gvpmbxzgq1cnc8e6nglhtc8&skId=vk1tzxh58gvpmbxzgq1cnc8e6nglhtc8&sfrom=search_job_pc&key=java&currentPage={}&scene=page"
    for i in range(10):
        time.sleep(5)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest' # 异步请求
        }
        url_search = url_pattern.format(i)
        response = requests.get(url_search, headers=headers) # 发送网络请求
        response.raise_for_status() # 若出错则打印错误信息
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify()) # 查看爬取后html

        for i in soup.find_all('div', class_='job-detail-box'):
            # 解析标签
            job = i.find('div',class_='ellipsis-1').get_text() # 职位名称
            company = i.find('span',class_='company-name').get_text() # 公司
            place = i.find('span',class_='ellipsis-1').get_text() # 工作地点
            salary = i.find('span',class_='job-salary').get_text() # 薪水
            temp_str = i.find('div', class_='job-labels-box').get_text().strip() # 经验时长及教育背景
            temp_arr = temp_str.split('\n')
            correct_arr = [j for j in temp_arr if j != '']
            working_hour = correct_arr[0]
            education = correct_arr[1]
            detail_url = i.find('a')['href'] # 详细地址
            # 数据预处理
            if salary == '面议':
                continue
            marker_pos = 0
            marker_pos = salary.find('·')
            if marker_pos != -1:
                salary = salary[:marker_pos]
            salary = salary.replace('k', '千/月')
            marker_pos = place.find('-')
            if marker_pos != -1:
                place = place[:marker_pos]
            # 存数据库
            save_to_mongo({
                'job': job,
                'company': company,
                'place': place,
                'salary': salary,
                'working_hour': working_hour,
                'education': education,
                'detail_url': detail_url
            })


'''
第一页URL:
https://www.liepin.com/zhaopin/?headId=08b61676304a96ce382165b6f5072927&ckId=86i8139zbuwv68c28qp264iaoy336af8&oldCkId=08b61676304a96ce382165b6f5072927&fkId=15u805k8co00ikcqpdybf9k423xxvos8&skId=15u805k8co00ikcqpdybf9k423xxvos8&sfrom=search_job_pc&key=java&currentPage=0&scene=page

第二页URL:
https://www.liepin.com/zhaopin/?headId=08b61676304a96ce382165b6f5072927&ckId=98v7r61jump9mkipekyhvtwavgicejgb&oldCkId=08b61676304a96ce382165b6f5072927&fkId=15u805k8co00ikcqpdybf9k423xxvos8&skId=15u805k8co00ikcqpdybf9k423xxvos8&sfrom=search_job_pc&key=java&currentPage=1&scene=page
'''