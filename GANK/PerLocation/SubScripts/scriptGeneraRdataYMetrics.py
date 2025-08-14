#!/usr/bin/env bash

from os import mkdir
import shutil
from os import system

#Pres = ['1stPres', '2ndPres', '3rdPres']
Pres = ['1stPres', '2ndPres']

Folder = 'STN_EvPS{}_R30'
Pop = ['10']
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
    for PS in Pop: 
        cont = 0
        workpath = precision+'/STN_P'+PS+'R30'
        mkdir(workpath)
        pathFolder = Folder.format(PS)
        for cat in categories:
            dirpath = workpath+'/'+cat
            mkdir(dirpath)
            filepath = precision + '/' + pathFolder + '/' + Prefix_file.format(PS) + files[cont] +'.out'
            shutil.copy(filepath, dirpath)
            comando = 'Rscript create.R {} 1'
            comando = comando.format(dirpath)
            print(comando)
            system(comando)
            comando = 'Rscript metrics-alg.R {} {}'
            comando = comando.format(dirpath+'-stn',cat)
            print(comando)
            system(comando)
            cont += 1
            newfold = precision + '/metrics_P_'+PS+'R30'
        mkdir(newfold)
        comando = 'mv *.csv {}'
        comando = comando.format(newfold)
        system(comando)
