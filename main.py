from hercules import Hercules
from zombie import Zombie
from lernaean import Lernaean

# print("You are Hercules, the greatest of the Greek Heroes!")
# print("You have been tasked by King Eurystheus to slay the vicious Nemean Lion!")
# print("Defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underwordl")

hercules_adventure = Hercules()
lernaeans_minions = Zombie()
lernaean_hydra = Lernaean()

# Camera fades onto the city of Athens, where villagers are running and screaming down the main city path.
# The great Nemean Lion has dispatched zombie like minions onto the city.
# These zombies are breaking into the homes of the villager and attacking them.
# The camera pans over to a muscled bound man wearing a golden chest plate, golden shin guards, golden forearm protectors, a golden helmet and a sword forged in the dying star of Nidavellir.
# As Hercules travels through Athens he can find various items that will regain his health

print(hercules_adventure.health_bar)
print(lernaeans_minions.health_bar)
print(lernaean_hydra.health_bar)