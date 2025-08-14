#!/usr/bin/env bash

from os import mkdir
import shutil
from os import system

Pres = ['1stPres', '2ndPres', '3rdPres']
#Pres = ['1st','2nd', '3rd']

categories = ['ALL', '2_20', '2_38', '2_52', '3_20', '3_34', '3_48', '4_20', '4_30', '4_40','5_20','5_28','5_38','6_20','6_26','6_32']

cont = 0
for precision in Pres:
        for cat in categories:
            
            path = precision + '/STN_Merged'
            comando = 'Rscript plot-merged.R {}'
            comando = comando.format(path+'/'+cat+'-merged.RData')
            print(comando)
            system(comando)
            #cont += 1
