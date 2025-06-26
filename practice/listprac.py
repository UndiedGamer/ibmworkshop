friends = ['a', 'b', 'c']
friends.append('d')
friends.remove('b')
friends.extend(['e', 'f'])
friend = friends.pop()
friends.reverse()

print(friend, friends)