import requests


url = "https://adventofcode.com/2024/day/1/input"
cookies = {
    'session':'53616c7465645f5f15f1ad138ad6f9d9041544b563631c2b5e0eff1c63ab5520e735290493ea626cd959afc8d348b51e5370aef9f3a8748581cb4ac9caa4050d'
}

r = requests.get(url,cookies=cookies)

list1 = []
list2 = []
similarity = []

if r.status_code == 200:
    content = r.text.splitlines()  # Split by lines, for example
    for elem in content:
        items = elem.split()
        list1.append(items[0])
        list2.append(items[1])

    for elem in list1:
        occur = list2.count(elem)
        ans = int(elem) * int(occur)
        similarity.append(ans)
else:
    print('None')

print(sum(similarity))



