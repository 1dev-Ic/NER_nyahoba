import json
import random

# ---------------------------
# STEP 1. Fixed lists
# ---------------------------
time_words = [
    "Zǝkǝu", "Sakana", "ǝna", "ǝhna", "Pǝshinda", "Pishinda",
    "Fer pǝchingǝ zekeu", "Pǝr pǝchingǝ zekeu", "Pǝchi", "Hya"
]

animal_words = [
    "Kwa", "Mabǝlang", "Tǝga", "Gwanba", "Ha'l", "Dlǝgwam", "Thla",
    "Kǝtǝn", "Chiwar", "Lǝvari", "Mapǝla'u", "Litsa"
]

person_words_fixed = [
    "Chahyaandida", "Chabiya", "Hyellama", "Hyelnaya", "Wandiya", "Hyel", "Yesu",
    "Chataimada", "Chatramada", "Nanunaya", "Mapida", "Shimbal", "Chai",
    "Hyellachardati", "Hyellachardati", "Wamanyi", "Miyaninyi", "Miyakindahyelni", "Miyaninyi"
]

# ---------------------------
# STEP 2. Synthetic PERSON names
# ---------------------------
base_names = [
    "Abubakar", "Ibrahim", "Musa", "Usman", "Kabiru", "Bello", "Suleiman",
    "Ahmad", "Aliyu", "Shehu", "Aminu", "Habiba", "Fatima", "Aisha", "Zainab", "Hauwa",
    "Ruqayya", "Maryam", "Khadija", "Sa'adatu", "Yakubu", "Ismaila", "Nasiru", "Idris",
    "John", "Paul", "Peter", "James", "Joseph", "Stephen", "Samuel",
    "David", "Daniel", "Thomas", "Andrew", "Philip", "Simon", "Nathaniel",
    "Grace", "Joyce", "Ruth", "Esther", "Naomi", "Sarah", "Deborah",
    "Ndyako", "Pwakina", "Gargam", "Kwada", "Tizhe", "Lazarus", "Kwapre",
    "Nzoka", "Jauro", "Birma", "Fwa", "Tumba", "Dlama", "Nuhu", "Zira", "Bitrus",
    "Vandi", "Nggada", "Gimba", "Danjuma"
]

prefixes = ["Alhaji", "Malam", "Doctor", "Pastor", "Chief", "Prince", "Princess", "Rev"]
suffixes = ["Abubakar", "Musa", "Ibrahim", "Aliyu", "Yakubu", "Bitrus", "Danjuma", "Zira", "Vandi", "Nuhu"]
syllables = ["Nga", "Fwa", "Tiz", "Lam", "Bok", "Ngu", "Pwa", "Kiri", "Shaf", "Loru", "Baga", "Dla", "Hoba", "Zar", "Yam", "Kwada"]

def make_variants(base_list, prefixes, suffixes, syllables, target=2000, max_attempts=20000):
    items = set(base_list)
    attempts = 0
    while len(items) < target and attempts < max_attempts:
        r = random.random()
        if r < 0.3 and prefixes:
            new = random.choice(prefixes) + " " + random.choice(base_list)
        elif r < 0.6 and suffixes:
            new = random.choice(base_list) + " " + random.choice(suffixes)
        elif r < 0.8 and syllables:
            new = random.choice(syllables) + random.choice(syllables)
        else:
            new = random.choice(base_list) + " " + random.choice(base_list)
        items.add(new)
        attempts += 1

    # Fill with duplicates if still short
    items = list(items)
    while len(items) < target:
        items.append(random.choice(items))
    return items[:target]

random.seed(2025)
all_person_names = make_variants(base_names + person_words_fixed, prefixes, suffixes, syllables, 2000)

# ---------------------------
# STEP 2b. Expand TIME and ANIMAL with variants to 2000
# ---------------------------
time_prefixes = ["Early", "Late", "Mid", "Pre", "Post"]
time_suffixes = ["time", "hour", "day", "night", "season"]
time_syllables = ["Zi", "Sa", "Na", "Ku", "Lo", "Mi", "Ta"]

animal_prefixes = ["Wild", "Big", "Little", "Young", "Old"]
animal_suffixes = ["beast", "cub", "ling", "hunter", "creature"]
animal_syllables = ["Ka", "Mo", "La", "Ti", "Ro", "Zu", "Ba"]

all_time_words = make_variants(time_words, time_prefixes, time_suffixes, time_syllables, 2000)
all_animal_words = make_variants(animal_words, animal_prefixes, animal_suffixes, animal_syllables, 2000)

# ---------------------------
# STEP 3. Location generator
# ---------------------------
base_places = [
    "Yola", "Jimeta", "Numan", "Ganye", "Gombi", "Hong", "Mubi", "Michika", "Madagali",
    "Maiha", "Fufore", "Song", "Demsa", "Guyuk", "Jada", "Lamurde", "Mayo-Belwa",
    "Shelleng", "Toungo", "Pella", "Uba", "Dirma", "Holma", "Kala'a", "Garkida",
    "Borrong", "Mayo-Lope", "Shuwa", "Mayo-Balewa", "River Benue", "Mayo Ine",
    "Mayo Nguli", "Mayo Sanzu", "Kiri Dam", "Mandara Mountains", "Zumo Hill", "Fali Hills"
]

prefixes_loc = ["New", "Old", "Upper", "Lower", "North", "South", "East", "West", "Mayo", "Wuro", "Gidan", "Bari"]
suffixes_loc = ["Gari", "Ward", "Hill", "Village", "Settlement", "Bridge", "Camp", "Market", "River", "Valley", "Peak", "Forest", "Reserve", "Dam"]
syllables_loc = ["Kwa", "Ngu", "Mayo", "Zar", "Kiri", "Wuro", "Tula", "Nguwa", "Ganye", "Song", "Lam", "Mubi", "Pella", "Hoba", "Beli", "Tambo", "Shaf", "Loru", "Baga", "Zumo"]

all_places = make_variants(base_places, prefixes_loc, suffixes_loc, syllables_loc, 2000)

# ---------------------------
# STEP 4. Annotation helper
# ---------------------------
def make_annotation(word, label):
    return {
        "data": {"text": word},
        "annotations": [{
            "result": [{
                "value": {
                    "start": 0,
                    "end": len(word),
                    "text": word,
                    "labels": [label]
                },
                "from_name": "label",
                "to_name": "text",
                "type": "labels"
            }]
        }]
    }

# Build datasets
time_tasks = [make_annotation(w, "TIME") for w in all_time_words]          # expanded 2000
animal_tasks = [make_annotation(w, "ANIMAL") for w in all_animal_words]    # expanded 2000
person_tasks = [make_annotation(w, "PERSON") for w in all_person_names]    # expanded 2000
location_tasks = [make_annotation(loc, "LOCATION") for loc in all_places]  # expanded 2000

# ---------------------------
# STEP 5. Merge datasets
# ---------------------------
merged = time_tasks + animal_tasks + person_tasks + location_tasks

with open("merged_dataset.json", "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)

print(f"✅ Saved {len(merged)} tasks -> merged_dataset.json")
print(f"  TIME: {len(time_tasks)}")
print(f"  ANIMAL: {len(animal_tasks)}")
print(f"  PERSON: {len(person_tasks)}")
print(f"  LOCATION: {len(location_tasks)}")
