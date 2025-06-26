import json
import random
from collections import defaultdict

# Define fixed options
testbench_types = ['tb1', 'tb2', 'tb3', 'tb4', 'tb5']
domain_types = ['ulphy', 'dlphy', ['ulphy', 'dlphy']]
channels_ulphy = ['pusch', 'prach', 'pucch']
channels_dlphy = ['pdsch', 'pdcch']
hardware_types = ['amd', 'nvidia', 'samsung', 'intel']
test_periodicities = ['daily', 'weekly']
test_types = ['functional', 'capacity']

# Function to generate appropriate channels
def generate_channels(domain_type):
    if domain_type == 'ulphy':
        return random.sample(channels_ulphy, random.randint(1, 3))
    elif domain_type == 'dlphy':
        return random.sample(channels_dlphy, random.randint(1, 2))
    elif domain_type == ['ulphy', 'dlphy']:
        ul = random.sample(channels_ulphy, random.randint(1, 3))
        dl = random.sample(channels_dlphy, random.randint(1, 2))
        return ul + dl

# Generate test cases
test_cases = defaultdict(list)

for i in range(1, 501):
    testbench_type = random.choice(testbench_types)
    domain_type = random.choice(domain_types)
    prb_length = random.randint(1, 250)
    cells = random.randint(1, 10)
    channel_type = generate_channels(domain_type)
    hardware_type = random.choice(hardware_types)
    test_periodicity = random.choice(test_periodicities)
    test_type = random.choice(test_types)

    test_case = {
        "test_case": f"test_case{i}",
        "domain_type": domain_type,
        "prb_length": prb_length,
        "cells": cells,
        "channel_type": channel_type,
        "hardware_type": hardware_type,
        "test_periodicity": test_periodicity,
        "test_type": test_type
    }

    test_cases[testbench_type].append(test_case)

# Save to JSON file
with open("generated_test_cases.json", "w") as f:
    json.dump(test_cases, f, indent=2)

print(" Test cases generated and saved to 'generated_test_cases.json'")
