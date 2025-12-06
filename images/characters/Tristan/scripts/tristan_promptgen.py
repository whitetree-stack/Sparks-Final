import random
import csv

# ---------------------------
# CORE CHARACTER DESCRIPTION
# ---------------------------
core = "absurdres, masterpiece, high quality, best quality, 1boy, young, male child, two-tone hair, short hair, blonde hair, auburn streaked hair, brown eyes,  white background, plain background, simple background, full body, simple clothes, brown tunic, rugged boots, medievel attire, looking to right, <lora:DisneyStudios_style:1> <lora:Disney_Animation_v5-V7:1>"

# ---------------------------
# VARIABLE LISTS
# ---------------------------

expressions = ["neutral expression", "smiling", "laughing", "frowning", "angry glare", "serious expression", "surprised", "shocked", "embarrassed blush", "determined look", "confident smirk", "sad expression", "crying", "worried", "focused gaze"]

poses = [ 
    "battle stance", "guard up", "attack follow-through", "charging forward", "power-up pose", "running start", "sliding crouch", "mid-air jump", "wall lean", "commanding gesture", "hand on hip", "reaching out", "wounded but standing", "back-turned silhouette", "victory pose"]

# ---------------------------
# GENERATION SETTINGS
# ---------------------------
num_prompts = 4  # change this to how many lines you want (100–1000 recommended)
output_file = "tristan_promptgen.csv"
output = 0

# ---------------------------
# CSV GENERATION
# ---------------------------
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for i in expressions:
        for k in poses:
        
            exp = i
            pose = k
            output += 1


            prompt = f"{core}, {exp}, {pose}"
            writer.writerow([prompt])

print(f"✅ '{output}' prompts saved to '{output_file}'")
