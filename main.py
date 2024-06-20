from data_collection.data_collector import DataCollector
from utils.database import Database

def main():
    db = Database()
    collector = DataCollector()
    collector.run(db)
    print("Vulnerability data collection complete")

if __name__ == "__main__":
    main()