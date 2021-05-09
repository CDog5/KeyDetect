from pynput import keyboard
#Represents a key, and has an opacity
#Opacity is lower when key is no longer pressed
class KeyRep:
    def __init__(self,key):
        self.key = key
        self.opacity = 255
    def __repr__(self):
        return f'KeyRep({self.key})'
queue = []
def find_key(key):
    idx = None
    #return the last index of that key being used
    for i,q in enumerate(queue):
        if q.key == key:
            idx = i
    return idx
def format_key(key):
    #Format the key nicely
    try:
        txt = key.char
    except AttributeError:
        txt = str(key).replace('Key.','').title()
    return txt
def on_release(key):
    global queue
    txt = format_key(key)
    if find_key(txt):
        queue[find_key(txt)].opacity = 150
def on_press(key):
    global queue
    txt = format_key(key)
    queue.append(KeyRep(txt))
    #only keep last 3 keypresses
    queue = queue[-3:]
# Collect events until released
listener = keyboard.Listener(
    on_press=on_press,on_release=on_release)
#Must be daemon so python quits properly
listener.daemon = True
listener.start()
