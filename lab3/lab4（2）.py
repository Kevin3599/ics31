phonebook = {}
entries = dict(item.split(',') for item in input().split())
search_name = input()
print(entries[search_name])