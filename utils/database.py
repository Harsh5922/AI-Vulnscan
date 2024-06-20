import sqlite3

class Database:
    def __init__(self, db_name="vulnerabilities.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
    
    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS vulnerabilities (
            id INTEGER PRIMARY KEY,
            cve_id TEXT,
            description TEXT,
            published_date TEXT,
            impact_score REAL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_vulnerability(self, vulnerability):
        query = '''
            INSERT INTO vulnerabilities (cve_id, description, published_date, impact_score)
            VALUES (?, ?, ?, ?)
        '''
        cve_id = vulnerability['cve']['CVE_data_meta']['ID']
        description = vulnerability['cve']['description']['description_data'][0]['value']
        published_date = vulnerability['publishedDate']
        impact_score = vulnerability.get('impact', {}).get('baseMetricV3', {}).get('impactScore', 0)
        self.conn.execute(query, (cve_id, description, published_date, impact_score))
        self.conn.commit()