# Sprint 4: Statisttical Data Analysis
# Chapter 2: Probability Theory
# Lesson 1: Experiments, Elementary Outcomes and Events

import pandas as pd

music = pd.DataFrame(
    {
        'Artist': [
            'Queen',
            'Queen',
            'Queen',
            'Pink Floyd',
            'Nirvana',
            'AC/DC',
            'AC/DC',
            'Scorpions',
            'Scorpions',
            'Scorpions',
            'BTS'
        ],
        'Song': [
            'The Show Must Go On',
            'Another One Bites The Dust',
            'We Will Rock You',
            'Wish You Were Here',
            'Smells Like Teen Spirit',
            'Highway To Hell',
            'Back in Black',
            'Wind Of Change',
            'Still Loving You',
            'Send Me An Angel',
            'Why'
        ],
    }
)
print(music)
print()

print(
    len(music[music['Song'] == 'Why']) / len(music)
)
print()