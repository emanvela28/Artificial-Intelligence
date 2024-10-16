#
# knowledge.py
#
# This file contains axioms for a midnight murder by monsters knowledge base.
#
# These sentences use the following ontology.
#
#   Bob, Celene, Lin, Alberto, Maria, Wanda : constants for individuals
#   Pale, Blue, Green, Purple : constants for skin complexion colors
#
#   Bitten(x) : true iff x has been bitten
#   Boils(x) : true iff the skin of x has boils
#   Cold(x) : true iff the body of x is cold to the touch
#   Complexion(x, y) : true iff the skin of x has the complexion y
#   Dead(x) : true iff x is dead
#   Disemboweled(x) : true iff the body of x is missing internal organs
#   Dismembered(x) : true iff the body of x is missing limbs
#   Drained(x) : true iff the body of x has been drained of blood
#   Eaten(x) : true iff x has been eaten
#   Incomplete(x) : true iff the body of x is missing parts
#   Intact(x) : true iff the body of x is relatively whole and intact
#   Killed(x, y) : true iff x murdered y
#   Monster(x) : true iff x is a monster
#   Person(x) : true iff x is a person
#   Poisoned(x) : true iff x has been poisoned
#   Present(x) : true iff x was present at the crime scene
#   Punctured(x) : true iff the body of x has puncture wounds
#   Suspect(x) : true iff x is a murder suspect
#   Vampire(x) : true iff x is a vampire
#   Victim(x) : true iff x was the victim of a murder
#   Werewolf(x) : true iff x is a werewolf
#   Witch(x) : true iff x is a witch
#
# No other constants, functions, or predicates should be used in the axioms
# contained in this file. All axioms must be definite clauses.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# I watched this video to expand my knowledge on first order logic: https://www.youtube.com/watch?v=ARywou8HLQk
# I read this article on FOL https://www.javatpoint.com/first-order-logic-in-artificial-intelligence
# I referred to Professor David's slides specifically from 10/17/23.
# I watched this video to help format FOL in python https://www.youtube.com/watch?v=5vlSloEdWcM
#
# Emmanuel Velazquez 10/30/23

crime_sentences = ['(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)',
                   'Owns(Nono, M1)',
                   'Missile(M1)',
                   '(Missile(x) & Owns(Nono, x)) ==> Sells(West, x, Nono)',
                   'Missile(x) ==> Weapon(x)',
                   'Enemy(x, America) ==> Hostile(x)',
                   'American(West)',
                   'Enemy(Nono, America)']


# Midnight Murder by Monsters Sentences

# The first-order logic definite clauses below are intended to express the
# following knowledge.

# PLACE YOUR FOL SENTENCES IN THIS LIST

monster_sentences = [
# Celene is a vampire.
    'Vampire(Celene)',

# Alberto is a werewolf.
    'Werewolf(Alberto)',

# Wanda is a witch.
    'Witch(Wanda)',

# Bob, Lin, and Maria are people.
    'Person(Bob)', 'Person(Lin)', 'Person(Maria)',

# A person who is dead is a victim.
    '(Person(x) & Dead(x)) ==> Victim(x)',

# All vampires, werewolves, and witches are monsters.
    'Vampire(x) ==> Monster(x)',

# All vampires, werewolves, and witches are monsters.
    'Werewolf(x) ==> Monster(x)',

# All vampires, werewolves, and witches are monsters.
    'Witch(x) ==> Monster(x)',

# Any monster present at the crime scene is a suspect.
    '(Monster(x) & Present(x)) ==> Suspect(x)',

# If a vampire is suspected and the victim was bitten, then the vampire killed the victim.
    '(Vampire(x) & Suspect(x) & Victim(y) & Bitten(y)) ==> Killed(x, y)',

# If a werewolf is suspected and the victim was eaten, then the werewolf killed the victim.
    '(Werewolf(x) & Suspect(x) & Victim(y) & Eaten(y)) ==> Killed(x, y)',

# If a witch is suspected and the victim was poisoned, then the witch killed the victim.
    '(Witch(x) & Suspect(x) & Victim(y) & Poisoned(y)) ==> Killed(x, y)',

# If a victim is drained of blood but has an intact body, then the victim was bitten.
    '(Victim(x) & Drained(x) & Intact(x)) ==> Bitten(x)',

# If a victim is drained of blood and has body pieces missing (i.e., is incomplete), then the victim was eaten.
    '(Victim(x) & Drained(x) & Incomplete(x)) ==> Eaten(x)',

# If a victim's body is intact, and the victim's skin complexion is green, blue, or purple, or if it is pale
# with boils, then the victim was poisoned.
    '(Victim(x) & Intact(x) & Complexion(x, Green)) ==> Poisoned(x)',

# If a victim's body is intact, and the victim's skin complexion is green, blue, or purple, or if it is pale
# with boils, then the victim was poisoned.
    '(Victim(x) & Intact(x) & Complexion(x, Blue)) ==> Poisoned(x)',

# If a victim's body is intact, and the victim's skin complexion is green, blue, or purple, or if it is pale
# with boils, then the victim was poisoned.
    '(Victim(x) & Intact(x) & Complexion(x, Purple)) ==> Poisoned(x)',

# If a victim's body is intact, and the victim's skin complexion is green, blue, or purple, or if it is pale
# with boils, then the victim was poisoned.
    '(Victim(x) & Intact(x) & Complexion(x, Pale) & Boils(x)) ==> Poisoned(x)',

# If a victim's skin complexion is pale and the body is either cold or punctured, then the victim is drained of blood.
    '(Victim(x) & Complexion(x, Pale) & Cold(x)) ==> Drained(x)',

# If a victim's skin complexion is pale and the body is either cold or punctured, then the victim is drained of blood.
    '(Victim(x) & Complexion(x, Pale) & Punctured(x)) ==> Drained(x)',

# If a victim's body is complete (i.e., not incomplete), then it is not dismembered or disemboweled.
    'Victim(x) & Dismembered(x) ==> Incomplete(x)',

# If a victim's body is complete (i.e., not incomplete), then it is not dismembered or disemboweled.
    'Victim(x) & Dismembered(x) ==> Incomplete(x)'
                     ]
