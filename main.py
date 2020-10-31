import request
import sys

list_argv = sys.argv # Список аргументов из командной строки


def cmd_argum(list_argv):

   if len(list_argv) == 5:#Если 5 аргументов (leaderboard.py --mode <MODE> --count N) возвращаем значения для mode и count
      mode , count = list_argv[2] , int(list_argv[4])
      return [mode , count, None , None]
   elif len(list_argv) == 7:#Если 7 аргументов (leaderboard.py --mode <MODE> --count N --user_id <user_id> или --country <country>) возвращаем значения для mode, count, user_id или country
      mode, count , last_arg = list_argv[2], int(list_argv[4]), list_argv[6]
      if list_argv[5] == '--country': # Если 6 значение в списке '--country' возвращаем значение mode, count, country
         country = last_arg
         return [mode, count , None ,country]
      else:# Возвращаем значение mode, count, user_id
         user_id = last_arg
         return [mode , count , user_id, None]

   else: #Если значений в списке не 5 и не 7, значит неверно введены параметры в командную строку
      print('Oops. Error in entered params')
req = request.get_response(cmd_argum(list_argv))# Вызов скрипта, создающего запрос и обрабатывающего ответ

print(req)#Вывод результатов