
import random

def generate_rect_polygon(x, y, width, height):
    """Generate a rectangle starting at x,y with given width and height"""
    box = [
        (x, y),
        (x + width, y),
        (x + width, y + height),
        (x, y + height),
        (x, y)
    ]
    coords = ", ".join([f"{lon:.6f} {lat:.6f}" for lon, lat in box])
    return f"POLYGON(({coords}))"

def generate_line_string(points):
    """Generate a LINESTRING from a list of (lon, lat) tuples"""
    coords = ", ".join([f"{lon:.6f} {lat:.6f}" for lon, lat in points])
    return f"LINESTRING({coords})"

def generate_london_dataset(output_file="Dataset_Real_World.wkt"):
    # Center on London
    base_lon = -0.1276
    base_lat = 51.5074
    
    scale = 0.002  # Approximately 200m spacing

    wkt_lines = []

    # 1. Main River (Thames-like curve)
    river_points = []
    for i in range(15):
        lon = base_lon - 0.02 + (i * 0.003)
        lat = base_lat - 0.005 + (0.002 * (i % 3)) # Wavy
        river_points.append((lon, lat))
    wkt_lines.append(generate_line_string(river_points))

    # 2. Grid of Roads (Horizontal)
    for i in range(5):
        lat = base_lat + (i * scale)
        start_lon = base_lon - 0.015
        end_lon = base_lon + 0.015
        wkt_lines.append(generate_line_string([(start_lon, lat), (end_lon, lat)]))

    # 3. Grid of Roads (Vertical)
    for i in range(8):
        lon = base_lon - 0.01 + (i * scale)
        start_lat = base_lat - 0.005
        end_lat = base_lat + 0.015
        wkt_lines.append(generate_line_string([(lon, start_lat), (lon, end_lat)]))

    # 4. Buildings (Polygons) intentionally overlapping roads to create conflicts
    for i in range(5):
        # Place buildings near intersections
        lon = base_lon - 0.01 + (i * scale)
        lat = base_lat + (0.002 * i) # Diagonal placement
        
        # Conflict 1: Overlapping road
        wkt_lines.append(generate_rect_polygon(lon, lat, 0.0008, 0.0008))
        
        # Conflict 2: Overlapping another building
        wkt_lines.append(generate_rect_polygon(lon + 0.0005, lat + 0.0005, 0.0008, 0.0008))

    with open(output_file, "w") as f:
        f.write("\n".join(wkt_lines))
    
    print(f"Generated {len(wkt_lines)} features in {output_file}")

if __name__ == "__main__":
    generate_london_dataset()