#!/usr/bin/env bash

from os import mkdir
import shutil
from os import system

#Pres = ['1stPres', '2ndPres', '3rdPres']
Pres = ['1stPres','2ndPres', '3rdPres']

Folder = 'STN_P{}'

Pop = ['10', '20', '50']

Prefix_file = 'P{}_'
files = ['EVOCA.log_GA_FALL_S',
'EVOCA.log_GA_Fnk_2_20_S',
'EVOCA.log_GA_Fnk_2_38_S',
'EVOCA.log_GA_Fnk_2_52_S',
'EVOCA.log_GA_Fnk_3_20_S',
'EVOCA.log_GA_Fnk_3_34_S',
'EVOCA.log_GA_Fnk_3_48_S',
'EVOCA.log_GA_Fnk_4_20_S',
'EVOCA.log_GA_Fnk_4_30_S',
'EVOCA.log_GA_Fnk_4_40_S',
'EVOCA.log_GA_Fnk_5_20_S',
'EVOCA.log_GA_Fnk_5_28_S',
'EVOCA.log_GA_Fnk_5_38_S',
'EVOCA.log_GA_Fnk_6_20_S',
'EVOCA.log_GA_Fnk_6_26_S',
'EVOCA.log_GA_Fnk_6_32_S']

categories = ['ALL', '2_20', '2_38', '2_52', '3_20', '3_34', '3_48', '4_20', '4_30', '4_40','5_20','5_28','5_38','6_20','6_26','6_32']

cont = 0
for precision in Pres:
        #cont = 0
        workpath = precision+'/STN_Merged'
        mkdir(workpath)
        for cat in categories:
            dirpath = workpath+'/'+cat
            mkdir(dirpath)
            for PS in Pop: 
                pathFolder = Folder.format(PS)
                filepath = precision + '/' + pathFolder + '/' + cat+'-stn/*.RData'
                comando = 'cp {} {}'
                comando = comando.format(filepath,dirpath)
                print(comando)
                system(comando)
                #shutil.copy(filepath, dirpath)
            
            comando = 'Rscript merge.R {}'
            comando = comando.format(dirpath)
            print(comando)
            system(comando)
            
            comando = 'Rscript metrics-merged.R {}'
            comando = comando.format(workpath+'/'+cat+'-merged.RData')
            print(comando)
            system(comando)
            #cont += 1
        
        newfold = precision +'/STN_Merged' + '/metrics'
        mkdir(newfold)
        comando = 'mv STN_Merged/*.csv {}'
        comando = comando.format('metrics/')
        system(comando)
