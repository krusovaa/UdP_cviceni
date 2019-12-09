import json

with open("DOP_PID_ZASTAVKY_B.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
print(len(data["features"]))

n = 0
for feat in data['features']:
    a = feat['properties']['ZAST_PASMO']
    if a == 'P':
        n = n + 1
print("Počet zastávek v pásmu P je: ", n)

#filtered_stops = []
#gj_structure = {'type': 'FeatureCollection'}
#gj_structure['features'] = filtered_stops
#with open("stops_out.json", "w", encoding="utf-8") as f:
#    json.dump(data, f)



filtered_stops = []
for feat in data['features']:
    a = feat['properties']['ZAST_PASMO']
    if a == 'P':
        filtered_stops.append(feat)
with open("zastavky.json", "w", encoding="utf-8") as f:
    json.dump(filtered_stops, f, indent=2, ensure_ascii=False)  # indent, ensure_ascii pro lepsi cteni


