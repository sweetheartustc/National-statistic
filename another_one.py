from selenium import webdriver
import time
import sqlite3
import matplotlib.pyplot as plt

#class for cpi
def __cpiplus__(self):
    self.type = 1

#class for graduate
def __graduate__(self):
    self.type = 1

#crawl the cpi
def crawl_cpi(self):
# Create a new instance of the Chrome driver
    browser = webdriver.Chrome()

#use selenium to get data
    url = "http://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0301&sj=2018"
    browser.get(url)
    button = browser.find_element_by_id('treeZhiBiao_10_span')
    button.click()
    time.sleep(1)
    li = button.find_elements_by_class_name('dt_head')
    li[2].click()

#get and stick data
    tables = browser.find_elements_by_class_name("public_table")[3]
    tr = tables.find_elements_by_xpath("//tbody/tr")[13:20]
    print(tr)
# save the data to a dictionary
    td = {}
    for i in range(len(tr)):
        tmp = tr[i].find_elements_by_tag_name("td")
        td[i] = ['']
    for j in range(len(tmp)):
        td[i].append(tmp[j].text)
    print(td)
    self.cpi = td

def crawl_graduate(self):
    browser.get(url)
    button = browser.find_element_by_id('treeZhiBiao_23_a')
    button.click()
    time.sleep(1)
    li = button.find_elements_by_class_name('treeZhiBiao_63_span')
    li[2].click()

#get and stick data
    tables = browser.find_elements_by_class_name("public_table")[3]
    trplus = tables.find_elements_by_xpath("//tbody/tr")[13:20]
    print(trplus)
# save the data to a dictionary
    tdplus = {}
    for i in range(len(trplus)):
        tmpplus = trplus[i].find_elements_by_tag_name("td")
        tdplus[i] = ['']
    for j in range(len(tmpplus)):
        tdplus[i].append(tmpplus[j].text)
    print(tdplus)
    self.cpi = tdplus

# Connect a database and create a table
conn = sqlite3.connect('population.db')
print("Opened database successfully")
c = conn.cursor()
# c.execute('''CREATE TABLE POPULATION
#        (ID INT PRIMARY KEY     NOT NULL,
#        EN_NAME        TEXT    NOT NULL,
#        ZH_NAME        TEXT    NOT NULL);''')
# print("Population Table Created!")
conn.commit()
c.execute("select name from sqlite_master where type='table' order by name;")
print(c.fetchall())
c.execute("PRAGMA table_info(POPULATION)")
print(c.fetchall())

# make sure you already have the dict td in the memory
for i, k in enumerate(td):
    sql = "INSERT INTO POPULATION (ID,EN_NAME,ZH_NAME) \
      VALUES (%d, '%s', '%s');" % (i, k, td[k])
    print(sql)
    c.execute(sql)

print("Records created successfully")
conn.close()

x=[1999:1:2018]
y=[tdplus]
fig.ax = plt.subplots()
plt(x,y)
plt.savefig("static/image/graduate_figure.png")
plt.show()

__cpiplus__()
crawl_graduate()