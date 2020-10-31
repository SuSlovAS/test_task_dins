import requests
import collections


def get_response(list_arg):#Функция создающая запрос и обрабатывающая ответ согласно п.1,п.2,п.3 задания
    try:
        response = requests.get('https://www.diabotical.com/api/v0/stats/leaderboard?mode=' + list_arg[0] +'&offset=0',
                                          timeout=(1,1))# запрос. list_arg[0] это значение <mode> из cmd

        ans = response.json()['leaderboard']

        if ans == []:
            return 'Oops. Error in entered params(Check <MODE>)' #Если вернулось пустое значение значит, неверно введено значение <MODE>
        if list_arg[2] == None and list_arg[3] == None:# Если значения user_id и country отсутствуют выполняем п.1 задания
            for item in ans:
                del item['user_id']# удаляем значение user_id из json-ответа, согласно заданию
            return ans[:list_arg[1]]# возврящаем ответ с учетом count
        elif list_arg[3] != None:# если есть значение country выполняем п.3 задания

            num_countries = collections.Counter()# создаем пустой словарь Counter
            for item in ans[:list_arg[1]]:# считаем каждое уникальное значие country в json-ответе с учетом count
                num_countries[item['country']] += 1
            return num_countries[list_arg[3]]#возвращаем количество уникальных игроков страны <country>
        else:# выполняем п.2
            for item in ans[:list_arg[1]]:
                if item['user_id'] == list_arg[2]:
                    return item


    except TypeError:
        print('Oops. Error in entered params')
    except ValueError:
        print('Oops. Error in entered params')
    except requests.exceptions.ConnectTimeout:
        print('Oops. Connection timeout occured!')
    except requests.exceptions.ReadTimeout:
        print('Oops. Read timeout occured')
    except requests.exceptions.HTTPError as err:
        print('Oops. HTTP Error occured')
        print('Response is: {content}'.format(content=err.response.content))

