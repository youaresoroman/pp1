import re
samogloski = re.findall('[aąiouyeęó]', "To be, or not to be, that is the question")

print('Ilość samogłosek:', len(samogloski))