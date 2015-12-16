import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import math
import time

os.chdir("C:/Users/Kile/Desktop")

job_url_list = []

job_info_file = open("job_info_file.txt")
for i in job_info_file.readlines():
    job_url_list.append(i.split("~")[-1][:-1])

job_url_set = set(job_url_list)
print(len(job_url_set))
salary_list = []
n = 0

for i in  job_url_set:
    n+=1
    try:
        url = urllib.request.urlopen(i)
        bsobj = BeautifulSoup(url)
        Location = bsobj.findAll("span",{"class":"important"})[2].b.get_text().split(",")[-1].strip()
    except:
        continue
    
    Salary_para = bsobj.findAll("td", {"width":"530", "colspan":"2"})[8].get_text()
    
    if re.findall('[S|s]alary', Salary_para) != []:
        Salary = re.findall('\S[0-9]+,[0-9]+', Salary_para)
        if  Salary == []:
            Salary = "None"
        else:
            Salary = Salary[0]
    else:
        Salary = "None"

    salary_list.append(Location+";"+Salary+"\n")
    print(n)
    time.sleep(0.1)
    
Salary_info_file = open("Salary_info_file.txt", "w",errors='ignore')
Salary_info_file.writelines(salary_list)
Salary_info_file.close()    
    
    





"""
job_list = []
job_info = []
rs = requests.session()
res = rs.get("http://linguistlist.org/jobs/browse-jobs.cfm")
bsobj = BeautifulSoup(res.text)

job = bsobj.findAll("tr",{"title":"Click to view job details"})
job_info.append(job)
#print(job_info_detail)
#print(len(job_info_detail))
#for i in job_info_detail[0]:
#    print(i)
#print(repr(job[1].findAll("td")[3].get_text()))

for i in range(len(job)):
    temp = job[i].findAll("td")
    job_list.append({})
    job_list[i]["Employer"] = temp[0].get_text().replace("\n", "")
    job_list[i]["Location"] = temp[1].get_text().replace(" ","").replace("\n", "").split(":")
    job_list[i]["Title"] = re.split(",",temp[2].get_text().strip("\n").strip())
    job_list[i]["Title"][:] = [vac.replace("\n", "") for vac in  job_list[i]["Title"]]
    job_list[i]["Specialty"] = temp[3].get_text().replace("\n", "").split(";")
    job_list[i]["Specialty"][:] = [vac.strip() for vac in  job_list[i]["Specialty"]]
    job_list[i]["Date"] = temp[5].get_text().replace(" ","").replace("\n", "").split("-")[1:3]
    job_list[i]["Date"][1] = job_list[i]["Date"][1][0:4]
    print(job_list[i])    



"""
