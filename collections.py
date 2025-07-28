import random


# random number of dicts
num_dicts = random.randint(2, 10)
# source of elements for keys in random dictionary
population_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# source of elements for values in random dictionary
population_vals = range(0, 101)
# random number of keys
num_keys = random.randint(0, 25)
# numbers of values in dictionary based on keys
num_values = num_keys
# creating random dicts
rand_dicts = [dict(zip(random.sample(population_keys, num_keys), random.choices(population_vals, k=num_values))) for _ in range(num_dicts)]
# key: number of its occurrences


merged_dict = {}
key_sources = {}

for idx, d in enumerate(rand_dicts):
    for key, value in d.items():
        if key not in merged_dict:
            merged_dict[key] = value
            key_sources[key] = idx
        else:
            if value > merged_dict[key]:
                merged_dict[key] = value
                key_sources[key] = idx

final_dict = {}
for key, value in merged_dict.items():
    source_idx = key_sources[key]
    count = sum(key in d for d in rand_dicts)
    new_key = f"{key}_{source_idx + 1}" if count > 1 else key
    final_dict[new_key] = value

print(final_dict)








