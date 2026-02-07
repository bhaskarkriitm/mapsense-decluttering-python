# mapsense-decluttering-python
Priority-aware map decluttering simulation using pure Python
import random

# ----------------------------
# Road representation
# ----------------------------

def generate_roads():
    roads = []
    for i in range(10):
        road = {
            "id": i,
            "x": i,
            "priority": 100 if i % 4 == 0 else 50
        }
        roads.append(road)
    return roads


def declutter(roads):
    new_roads = []
    for r in roads:
        if r["priority"] < 100:
            shift = random.randint(-2, 2)
            new_roads.append({
                "id": r["id"],
                "x": r["x"] + shift,
                "priority": r["priority"]
            })
        else:
            new_roads.append(r)
    return new_roads


# ----------------------------
# Text Visualization
# ----------------------------

def print_roads(roads, title):
    print("\n" + title)
    print("-" * len(title))
    for r in roads:
        marker = "█" if r["priority"] == 100 else "-"
        print(f"Road {r['id']:2d}: {marker * (r['x'] + 1)}")


# ----------------------------
# Main
# ----------------------------

if __name__ == "__main__":
    roads = generate_roads()
    decluttered = declutter(roads)

    print_roads(roads, "BEFORE (Original Map)")
    print_roads(decluttered, "AFTER (Decluttered Map)")
