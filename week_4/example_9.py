# # function of dic
# d = {"shir": 47, "yael": 44, "yuval": 13.5, "amir": 12, "ori": 6, "dubi": [9, 63]}
# print(d.get("shir"))
# print(d.get("Shir"))
# print(d.get("Shir", "Default!!!!"))
#
# d["shir"] = 8
# print(d)

d = {"shir": 47, "yael": 47, "yuval": 13.5, "amir": 12, "ori": 6, "dubi": [9, 63]}
# print(d.keys())

for key in d.keys():
    print(key)
for item in d.items():
    print(item)
# print(d.items())


# d = {"shir": 47}
# print(d)
# ls = [["yuval", 13.5], ["amir", 12], ["ori", 6], ["amir", 13]]
# # tu = [("yuval", 13.5), ("amir", 12), ("ori", 6)]
# print(ls)
# d.update(ls)
# print(d)