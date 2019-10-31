import requests
import bs4
#Creating a list to categorize public/private/vendor
pub = []
priv = []
ven = []
page = requests.get("https://android.googlesource.com/platform/system/sepolicy/+/refs/tags/android-10.0.0_r6/public/")
soup = bs4.BeautifulSoup(page.text, 'html.parser')
filelist = soup.find(class_='FileList')
filelist_name = filelist.find_all('a')
for file_name in filelist_name:
    names = file_name.contents[0]
    if names[:-1] != '/':
        pub.append(names)
page = requests.get("https://android.googlesource.com/platform/system/sepolicy/+/refs/tags/android-10.0.0_r6/private/")
soup = bs4.BeautifulSoup(page.text, 'html.parser')
filelist = soup.find(class_='FileList')
filelist_name = filelist.find_all('a')
for file_name in filelist_name:
    names = file_name.contents[0]
    if names[:-1] != '/':
        priv.append(names)
page = requests.get("https://android.googlesource.com/platform/system/sepolicy/+/refs/tags/android-10.0.0_r6/vendor/")
soup = bs4.BeautifulSoup(page.text, 'html.parser')
filelist = soup.find(class_='FileList')
filelist_name = filelist.find_all('a')
for file_name in filelist_name:
    names = file_name.contents[0]
    if names[:-1] != '/':
        ven.append(names)
