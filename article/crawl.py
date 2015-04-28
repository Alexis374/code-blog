#coding:utf8
from bs4 import BeautifulSoup
import requests
from article.models import Article,Tag,Category
from ljcbeyondBlog.kvdb import kv
repo_url = u'https://github.com/Alexis374/tech_post'
github = u'https://github.com'

def get_soup(url):
    '''
    :param url:
    :return:soup
    '''
    res = requests.get(url,verify=False)
    if res.status_code!=200:
        return
    return BeautifulSoup(res.content)

def check_update(soup):
    '''
    检查是否更新，若更新则爬取
    :return: bool
    '''
    commit_digest = soup.find('span',class_='cha').text
    key = 'last_commit_digest'
    if commit_digest == kv.get(key):
        return False
    else:
        return True


def get_article_link(soup):
    '''
    获取文章链接。由于文章都是md结尾，用正则提取；
    同时遍历文件夹之内的文章
    用kvdb记录已经处理过的文章
    :return: 未处理过的文章链接列表
    '''
    #获取文件名为*.md的文章的链接
    article_link = lambda tag:tag.name=='a' and '.md' in tag.text
    link_list = [ a['href'] for a in  soup.find_all(article_link)
                  if not kv.get(a.text[:-3])]
    #获取文件夹链接
    icons = soup.find_all('span',attrs={'class':'octicon octicon-file-directory'})
    for icon in icons:
        dir_url = icon.findParent().findNextSibling().find('a')['href']
        dir_soup = get_soup(github+dir_url)
        link_list.extend([a['href'] for a in dir_soup.find_all(article_link)
                          if not kv.get(a.text[:-3])])
    return link_list

def get_article(url):
    article_soup = get_soup(url)
    title = article_soup


def cronjob(request,):
    soup = get_soup(repo_url)
    status = check_update(soup)
    if not status:
        return False
    uncrawl_links = get_article_link(soup)
