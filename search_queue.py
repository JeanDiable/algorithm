from collections import deque
graph = {}
graph['you'] = ['Alice','Bob','Claire']
graph['Bob'] = ['Anuj', 'Peggy']
graph['Alice'] = ['Peggy']
graph['Claire'] = ['Thom', 'Jhonny']
graph['Anuj'] = []
graph['Peggy'] = []
graph['Thom'] = []
graph['jhonny'] = []


def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search('you')