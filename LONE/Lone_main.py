#@author        :   K S SARIKA
#@team_members  :   ABISHA K B, GAYATHRI GIREESH, VISHNUPRIYA

###############################################################################
################################################################################

#@Aim           :   Creating a new Interpreted Programing Language Named as LONE [Language Of New Era]
#======================++++++++++++++++++++++++++++++++++++++++++++==================================
#======================++++++++++++++++++++++++++++++++++++++++++++==================================

#Importing Run Module

import Run
while True:
  text = input('LONE> ')
  result, error = Run.run("<stdin>",text)       #Callung run function from Run Module

  if error : print(error.as_string())
  else: print(result)