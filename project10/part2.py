import random
import string

our_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

print(our_id)