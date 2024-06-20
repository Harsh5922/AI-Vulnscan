from .vulnerability_sources import NVD

class DataCollector:
    def __init__(self):
        self.vulnerabilities = []

    def collect_data(self):
        self.vulnerabilities.extend(NVD().get_vulnerabilities())

    def save_to_database(self, db):
        for vuln in self.vulnerabilities:
            db.insert_vulnerability(vuln)

    def run(self, db):
        self.collect_data()
        self.save_to_database(db)
    
    