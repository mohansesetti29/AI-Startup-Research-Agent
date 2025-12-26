
from .base_agent import BaseAgent
import json, os

class AlertAgent(BaseAgent):
    def __init__(self, storage_path="output/seen_urls.json"):
        super().__init__("AlertAgent")
        self.storage_path = storage_path

        # Create storage file if missing
        if not os.path.exists(storage_path):
            with open(storage_path, "w") as f:
                json.dump({}, f)

    def load_seen(self):
        with open(self.storage_path, "r") as f:
            return json.load(f)

    def save_seen(self, data):
        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=2)

    def check_new(self, query, sources_dict):
        seen = self.load_seen()
        old_urls = set(seen.get(query, []))
        new_found = set()

        # extract all URLs
        for section, urls in sources_dict.items():
            for url in urls:
                if url not in old_urls:
                    new_found.add(url)

        # update storage
        if new_found:
            seen[query] = list(old_urls.union(new_found))
            self.save_seen(seen)

        return list(new_found)
