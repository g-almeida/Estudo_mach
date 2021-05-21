"""
The classic way to create dictionaries it would be:

contacts = {'gab':'9999-0000', 'sop':'3333-3333', 'gust':'4242-2422'}

But here I'm showing that you can create an empty one and then assign keys/values to them.
"""

# So here we're creating an empty dictionary 
contacts = {}

# The next 3 lines are creating keys ('gab', 'sop', 'gust') and assigning the respective values.
# This is my favorite way to create dictionaries
contacts['gab'] = '9999-0000'
contacts['sop'] = '3333-3333'
contacts['gust'] = '4242-2422'

print(contacts)

"""
Useful Methods: dictionary.get(key)        ; this will look for the value of the respective key called inside the parenthesis. 
                dictionary.update({key:value})    ; this updates the dictionary, if the key doesn't exists it will be created
"""
print(contacts.get('gab'))


"""
Below I coded an example of how you can create a dict by inputing the information
OBS.: we're using a new variable (<contacts2>), you also could use the variable <contacts> but it would add keys and values to the old dict
"""
contacts2 = {}
x = str(input("entre com seu contato"))
y = str(input("entre com seu número agora"))
contacts2[x] = y

print(contacts2)
