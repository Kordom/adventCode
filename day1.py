
import requests

url = "https://adventofcode.com/2024/day/1/input"
cookies = {
    'session':'53616c7465645f5f15f1ad138ad6f9d9041544b563631c2b5e0eff1c63ab5520e735290493ea626cd959afc8d348b51e5370aef9f3a8748581cb4ac9caa4050d'
}

r = requests.get(url,cookies=cookies)

list1 = []
list2 = []
distance = []

if r.status_code == 200:
    content = r.text.splitlines()
    for elem in content:
        items = elem.split()
        list1.append(int(items[0]))
        list2.append(int(items[1]))

    for i in range(len(list1)):
        min_number_in_list1 = min(list1)
        min_number_index = list1.index(min_number_in_list1)

        min_number_in_list2 = min(list2)
        min_number_index2 = list2.index(min_number_in_list2)

        if min_number_in_list1 > min_number_in_list2:
            distance_value = min_number_in_list1 - min_number_in_list2
            distance.append(distance_value)
            list1.pop(min_number_index)
            list2.pop(min_number_index2)
        else:
            distance_value = min_number_in_list2 - min_number_in_list1
            distance.append(distance_value)
            list1.pop(min_number_index)
            list2.pop(min_number_index2)

    print(sum(distance))
else:
    print('None')




