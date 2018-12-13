import requests
import sys


class OSRS_GE_Data:
    def __init__(self, **kwargs):
        url = "https://rsbuddy.com/exchange/summary.json"
        self.ge_json = self.update_json(url)
        if self.ge_json == None:
            print("No json object initialized. Terminating program.")
            sys.exit(1)
        if 'nature_rune' in kwargs:
            self.nature_rune = kwargs['nature_rune']
        else:
            self.nature_rune = self.ge_json['561']['overall_average']

    def update_json(self, url):
        r = requests.get(url)
        if r.status_code != 200:
            print("Failed to get new json.")
            return None
        try:
            return r.json()
        except:
            print("This isn't a json object.")
            return None

    def sort_json(self, json_obj, sort_function, direction):
        json_list = sorted(json_obj, key=sort_function, reverse=direction)
        return json_list

    def get_top_values(self, total, json_list):
        if total > len(json_list):
            print("Total is too high. Returning entire list")
            return json_list
        return json_list[:total]

    def get_list_by_value(self, json_list, key):
        value_list = []
        for id in json_list:
            value_list.append(self.lookup_item_by_id(id, key))
        return value_list

    def lookup_item_by_id(self, id, key):
        if id not in self.ge_json.keys():
            print("Invalid id.")
            return None
        return self.ge_json[id][key]

    def get_entry(self, id):
        return self.ge_json[id]


