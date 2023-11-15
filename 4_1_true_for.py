# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:54:39 2020

@author: Geon
"""

import pandas as pd
import numpy as np
import os
import re
import difflib
import time
import warnings

from urllib import parse
from tqdm import tqdm
from datetime import datetime


######### 함수 #########

### 일반적인 파라미터 key=value 값 삭제
def check_1_general(data_list):
    
    list_len = len(data_list)
    return_value = []                                                           # 리턴값
    
    if list_len > 0:        
        key_1_regexp = re.compile(r'function')                                  # function
        key_2_regexp = re.compile(r'script')                                    # script
        key_3_regexp = re.compile(r'alert')                                     # alert
        key_4_regexp = re.compile(r'script')                                    # javascript
        key_5_regexp = re.compile(r'union')                                     # union
        key_6_regexp = re.compile(r'nslookup')                                  # nslookup
        key_7_regexp = re.compile(r'select ')                                   # select
        key_8_regexp = re.compile(r'insert ')                                   # insert
        key_9_regexp = re.compile(r'response')                                  # response
        key_10_regexp = re.compile(r'sleep')                                    # sleep
        key_11_regexp = re.compile(r'systemroot')                               # systemroot
        key_12_regexp = re.compile(r'replace')                                  # replace
        key_13_regexp = re.compile(r'cmdshell')                                 # cmdshell
        key_14_regexp = re.compile(r'ifconfig')                                 # ifconfig
        key_15_regexp = re.compile(r'servicecontrol')                           # servicecontrol
        key_16_regexp = re.compile(r'webserver')                                # webserver
        key_17_regexp = re.compile(r'document\.')                                 # document
        key_18_regexp = re.compile(r'contenteditable')                          # contenteditable
        key_19_regexp = re.compile(r'oneonerrorrror')                           # oneonerrorrror
        key_20_regexp = re.compile(r'onbeforeunload')                           # onbeforeunload
        key_21_regexp = re.compile(r'initmouseevent')                           # initmouseevent
        key_22_regexp = re.compile(r'automagictable')                           # automagictable
        key_23_regexp = re.compile(r'oncontextmenu')                            # oncontextmenu
        key_24_regexp = re.compile(r'ontouchcancel')                            # ontouchcancel
        key_25_regexp = re.compile(r'createelement')                            # createelement
        key_26_regexp = re.compile(r'openbugbounty')                            # openbugbounty
        key_27_regexp = re.compile(r'tomcat')                                   # tomcat
        
        for one in data_list:
            
            one = parse.unquote(one)
            one = parse.unquote(one)
            one = parse.unquote(one)
            one = parse.unquote(one)
            one = parse.unquote(one)
            
            one = one.strip()
        
            word_key = ''
            word_val = ''
        
            if len(one.split('=', 1)) == 2:
                word_key = one.split('=', 1)[0]
                word_val = one.split('=', 1)[1]
            else:
                word_key = one.split('=', 1)[0]
                word_val = ''
                
            word_key = re.sub(r'^amp;', '', word_key)
            
            check_val = 'T'
            
            if key_1_regexp.search(word_val) != None:
                check_val = 'F'                
            elif key_2_regexp.search(word_val) != None:
                check_val = 'F'                
            elif key_3_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_4_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_5_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_6_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_7_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_8_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_9_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_10_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_11_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_12_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_13_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_14_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_15_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_16_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_17_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_18_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_19_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_20_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_21_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_22_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_23_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_24_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_25_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_26_regexp.search(word_val) != None:
                check_val = 'F'
            elif key_27_regexp.search(word_val) != None:
                check_val = 'F'
                
            if word_key == '' and word_val == '':
                check_val = 'T'
                
            if check_val == 'F':
                return_value.append(one)
            
    return return_value


### 확장자 Group By 함수
def combine_1_exe(df):
    
    df2 = df[['file_ext', 'd_group', 'cnt']]
    #df2['cnt'] = pd.to_numeric(df2['cnt'], errors='coerce')
    #df2['cnt'] = df2['cnt'].fillna(1)
    
    df_1_ext = df2.groupby(['file_ext', 'd_group']).sum()['cnt']
    df_1_ext = df_1_ext.reset_index(drop=False)
    df_1_ext = df_1_ext.sort_values(by=['d_group', 'cnt', 'file_ext'], ascending=[True, False, True])            # 데이터프레임 정렬
    df_1_ext = df_1_ext.reset_index(drop=True)
    
    return df_1_ext



### 데이터 기준 Path 경로 추출
def making_1_path(df):
    
    df_0_path = df[['url_path_enc','cnt']]
    df_1_path = df_0_path.groupby('url_path_enc').sum()
    df_1_path = df_1_path.reset_index()
    
    df_1_path['url_path_enc'] = df_1_path['url_path_enc'].str.replace('\/$', '')
    df_1_path = df_1_path[df_1_path['url_path_enc'] != '']
    df_1_path['path'] = df_1_path['url_path_enc']
    
    df_2_path = df_1_path.set_index(['path', 'cnt'])['url_path_enc'].str.split('/', expand=True).reset_index(drop=False)

    return df_2_path
########################



######### 시작 #########
### 1차로 분류된 False 데이터에서 추가 전처리 과정
warnings.filterwarnings(action='ignore')

start = time.time()    

dir_path = './data/1_preprocessed/02_third/20201118_100105'
save_0_path = './data/1_preprocessed/03_data/01_1_true'
save_1_path = './data/1_preprocessed/03_data/02_1_false'
save_2_path = './data/1_preprocessed/03_data/03_1_file'

group_list = os.listdir(dir_path)

file_type = '_1_true_url.csv'

for group_nm in group_list:
    
    data_1_path = dir_path + '/' + group_nm

    print(data_1_path)

    file_list = os.listdir(data_1_path)
    file_list = sorted(file_list)
    
    save_true = save_0_path + '/' + group_nm
    save_false = save_1_path + '/' + group_nm
    save_file = save_2_path + '/' + group_nm
    
    if not os.path.isdir(save_true):
        os.makedirs(save_true, exist_ok=True)
    
    if not os.path.isdir(save_false):
        os.makedirs(save_false, exist_ok=True)
    
    if not os.path.isdir(save_file):
        os.makedirs(save_file, exist_ok=True)
    
    for file_nm in tqdm(file_list):
        
        if file_type in file_nm:
            
            df_1_all = pd.read_csv(data_1_path + '/' + file_nm, encoding = 'utf-8')
            
            df_1_all['cnt'] = pd.to_numeric(df_1_all['cnt'], errors='coerce')
            df_1_all['cnt'] = df_1_all['cnt'].fillna(0)                
            df_1_all = df_1_all[df_1_all['cnt'] > 0]      
            
            save_nm = file_nm.replace(file_type, '')
            #print(save_nm)
            
            if df_1_all.size > 0:
                
                del(df_1_all['Unnamed: 0'])

                df_2_all = df_1_all[['url', 'cnt', 'url_path', 'url_path_enc', 'file_name', 'file_ext', 'parameter', 'd_group', 'check']]
                df_2_all['ch_path'] = 'T'
                
                df_2_all['url_path'] = df_2_all['url_path'].fillna('')
                df_2_all['parameter'] = df_2_all['parameter'].fillna('')
                
                df_2_all['only_path'] = df_2_all['url'].str.split('#', 1).str[0]
                df_2_all['only_path'] = df_2_all['only_path'].str.split('?', 1).str[0]
                df_2_all['only_path'] = df_2_all['only_path'].str.split(';jsession', 1).str[0]
                
                for i in range(0, 5):
                    df_2_all['only_path'] = df_2_all['only_path'].apply(lambda x : parse.unquote(x))
                
                df_2_all['only_path'] = df_2_all['only_path'].str.split(';jsession', 1).str[0]
                df_2_all['only_path'] = df_2_all['only_path'].str.replace('/', '')
                
                df_2_all['ch_path'][df_2_all['only_path'].str.contains('^[a-zA-Z_\-0-9\.\$\:]+$') == False] = 'F'       # 영어, 숫자
                df_2_all['ch_path'][df_2_all['only_path'] == ''] = 'T'
                
                # 글짜가 깨진 경우가 있는 경우
                df_2_all['ch_path'][df_2_all['only_path'].str.contains('[^\u0000-\u007F\u3131-\u318E\uAC00-\uD7A3]+') == True] = 'F'

                df_2_all['parameter2'] = df_2_all['parameter'].str.replace('&amp;', '&')          # Parameter (&amp; >> & 으로 변경)
                df_2_all['parameter2'] = df_2_all['parameter2'].str.replace('^&', '')             # Parameter (가장 맨 앞의 & >> 삭제)
                df_2_all['parameter2'] = df_2_all['parameter2'].str.replace('&$', '')             # Parameter (맨 마지막 & >> 삭제)
                
                df_2_all['parameter2'] = df_2_all['parameter2'].fillna('')
                
                df_2_all['parameter3'] = df_2_all['parameter2'].str.split('&')
                df_2_all['parameter_new'] = df_2_all['parameter2'].str.split('&').apply(lambda x: check_1_general(x))
                
                df_2_all['check_len'] = df_2_all['parameter_new'].str.len()
                
                df_2_all['file_ext'] = df_2_all['file_ext'].fillna('')
                df_2_all['file_ext'] = df_2_all['file_ext'].str.lower()
                df_2_all['file_name'] = df_2_all['file_name'].fillna('')
                df_2_all['file_name'] = df_2_all['file_name'].str.lower()
                
                df_2_all['url_path_enc'] = df_2_all['url_path_enc'].str.lower()
                         
                df_2_all['check'][df_2_all['ch_path'] == 'F'] = 'F'
                df_2_all['check'][df_2_all['check_len'] > 0] = 'F'
                
                ### 관리자 페이지 접속 관련 키워드 추가 가능
                df_2_all['check'][(df_2_all['file_ext'] == 'ini') & (df_2_all['file_name'].str.contains('(boot)|(win)') == True)] = 'F'
                df_2_all['check'][(df_2_all['file_ext'] == 'xml') & (df_2_all['file_name'].str.contains('(config)|(browserconfig)|(wlwmanifest)|(web)|(servlet)|(root)|(database)|(datasource)|(sql_mysql)|(sql_oracle)|(sql_tibero)|(sql_altibase)') == True)] = 'F'
                df_2_all['check'][(df_2_all['file_ext'] == 'php') & (df_2_all['file_name'].str.contains('(wp-login)|(config)|(xmlrpc)|(phpadmin)|(phpmyadmin)|(phpinfo)|(phpmyadmin)|(phpwebshell)|(index)') == True)] = 'F'
                df_2_all['check'][(df_2_all['file_ext'] == 'asp') & (df_2_all['file_name'].str.contains('(cltreq)|(config)|(aspshell)|(aspxspy)|(aspcms)') == True)] = 'F'
                df_2_all['check'][(df_2_all['file_ext'] == 'aspx') & (df_2_all['file_name'].str.contains('(cltreq)|(config)|(aspshell)|(aspxspy)|(aspcms)') == True)] = 'F'
                df_2_all['check'][(df_2_all['file_ext'] == 'properties') & (df_2_all['file_name'].str.contains('(db)|(database)|(log4j)|(datasource)') == True)] = 'F'
                df_2_all['check'][(df_2_all['file_ext'] == 'txt') & (df_2_all['file_name'].str.contains('(robots)|(allowurl)') == True)] = 'F'
                df_2_all['check'][(df_2_all['file_ext'] == 'conf') & (df_2_all['file_name'].str.contains('(httpd)') == True)] = 'F'
                df_2_all['check'][df_2_all['url_path_enc'].str.contains('^\$\{[a-zA-Z0-9]+\}$') == True] = 'F'
                df_2_all['check'][df_2_all['url_path_enc'].str.contains('^\%[a-zA-Z0-9]+\%$') == True] = 'F'
                df_2_all['check'][df_2_all['url_path_enc'].str.contains('(phpmyadmin)|(wordpress)|(j_spring_security)|(wp-login)|(ymwears.cn)|(web-inf)|(wp-includes)') == True] = 'F'
                
                false_t_df = df_2_all[df_2_all['check'] == 'F']
                
                
                """
                false_0_df = df_2_all[df_2_all['check_len'] > 0]
                
                ### 관리자 페이지 접속 관련 키워드 추가 가능
                false_1_df = df_2_all[(df_2_all['file_ext'] == 'ini') & (df_2_all['file_name'].str.contains('(boot)|(win)') == True)]
                false_2_df = df_2_all[(df_2_all['file_ext'] == 'xml') & (df_2_all['file_name'].str.contains('(browserconfig)|(wlwmanifest)|(web)|(servlet)|(root)|(database)|(datasource)') == True)]
                false_3_df = df_2_all[(df_2_all['file_ext'] == 'php') & (df_2_all['file_name'].str.contains('(wp-login)|(config)|(xmlrpc)|(phpadmin)|(phpmyadmin)|(phpinfo)|(phpmyadmin)|(phpwebshell)|(index)') == True)]
                false_4_df = df_2_all[(df_2_all['file_ext'] == 'asp') & (df_2_all['file_name'].str.contains('(cltreq)|(config)|(aspshell)|(aspxspy)|(aspcms)') == True)]
                false_5_df = df_2_all[(df_2_all['file_ext'] == 'aspx') & (df_2_all['file_name'].str.contains('(cltreq)|(config)|(aspshell)|(aspxspy)|(aspcms)') == True)]
                false_6_df = df_2_all[(df_2_all['file_ext'] == 'properties') & (df_2_all['file_name'].str.contains('(db)|(database)|(log4j)|(datasource)') == True)]
                
                false_t_df = false_0_df.append(false_1_df)
                false_t_df = false_t_df.append(false_2_df)
                false_t_df = false_t_df.append(false_3_df)
                false_t_df = false_t_df.append(false_4_df)
                false_t_df = false_t_df.append(false_5_df)
                false_t_df = false_t_df.append(false_6_df)
                """
                                
                ### 최종 True, False Dataframe
                total_0_true = df_1_all.drop(false_t_df.index)
                total_1_false = df_1_all.drop(total_0_true.index)
                
                ### 파일 확장자 추출 Dataframe
                file_0_df = combine_1_exe(total_0_true)
                
                ### True 데이터 기반 Path Dataframe
                path_0_df = making_1_path(total_0_true)

                ### 데이터 저장 부분
                total_0_true.to_csv(save_true + '/' + save_nm + '_1_true_url' + '.csv', sep=',', na_rep='NaN', encoding='utf-8')
                total_1_false.to_csv(save_false + '/' + save_nm + '_1_false_url' + '.csv', sep=',', na_rep='NaN', encoding='utf-8')
                
                file_0_df.to_csv(save_file + '/' + save_nm + '_1_file_ext' + '.csv', sep=',', na_rep='NaN', encoding='utf-8')
                path_0_df.to_csv(save_file + '/' + save_nm + '_2_url_path' + '.csv', sep=',', na_rep='NaN', encoding='utf-8')
                                
                """
                if false_total.size > 0:
                    true_total.to_csv(save_path + '/' + save_nm + '_1_1_true_url' + '.csv', sep=',', na_rep='NaN', encoding='utf-8')
                    false_total.to_csv(save_path + '/' + save_nm + '_1_2_false_url' + '.csv', sep=',', na_rep='NaN', encoding='utf-8')
                else:
                    true_total.to_csv(save_path + '/' + save_nm + '_1_1_true_url' + '.csv', sep=',', na_rep='NaN', encoding='utf-8')
                """
print('---------------------------------')
print(time.time() - start)
print('---------------------------------')





