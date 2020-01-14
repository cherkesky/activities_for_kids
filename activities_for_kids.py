running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run(name):
  for runner in running_kids:
   print(f'{runner} is running fast!') if name==runner else None
    
def swing(name):
  for swinger in swinging_kids:
   print(f'{swinger} is a natural swinger!') if name==swinger else None

def slide(name):
  for slider in sliding_kids:
   print(f'{slider} is sliding like a pro!') if name==slider else None

def hide(name):
  for hider in hiding_kids:
   print(f'Where is {hider}? Such a good hider!') if name==hider else None


run("Pam")
swing("Courtney")
slide("Jack")
hide("Henry")