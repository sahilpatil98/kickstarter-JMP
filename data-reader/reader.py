from glob import glob
from flatten_json import flatten
import json
import pandas as pd

class Reader:
    def __init__(self, path):
        self.path = path
        # Create sets to store unique values
        self.creator_ids = set()
        self.project_ids = set()
        self.unique_rows = set()

        # States to Drop
        self.DROP_STATES = {'live': 0, 'started': 0, 'submitted': 0, 'suspended': 0}

        # Create counters
        self.CREATOR_COUNTER = 0
        self.PROJECT_COUNTER = 0
        self.SKIPPED_COUNTER = 0

        def reset_counters(self):
            self.CREATOR_COUNTER = 0
            self.PROJECT_COUNTER = 0
            self.SKIPPED_COUNTER = 0
            self.DROP_STATES = {state: 0 for state in self.DROP_STATES}
        

        def read_json(self):
            self.rows = []

            for file in glob(f"{self.path}/*.json"):
                print(f"Procfessing file: {file}")

                with open(file, 'r', encoding = 'utf-8') as f:
                    # Flatten JSON and Load Data
                    data = flatten(json.loads(line)['data'])
                    creator_id, project_id, state, launched_at = data['creator_id'], data['id'], data['state'].lower(), data['launched_at']
                
                    # Skip rows with drop states and update counter
                    if state in self.DROP_STATES:
                        self.DROP_STATES[state] += 1
                        continue
                
                    # Create a unique row identifier
                    row_id = (creator_id, project_id, state, launched_at)
                    
                    # Check if creator is unique
                    if creator_id not in self.creator_ids:
                        self.CREATOR_COUNTER += 1
                        self.creator_ids.add(creator_id)
                        self.project_ids.add(project_id)
                        self.unique_rows.add(row_id)
                        rows.append(data)
                        continue

                    else:
                        # Check for uniqueness
                        if row_id in self.unique_rows:
                            SKIPPED_COUNTER += 1
                            continue
                        else:
                            project_counter += 1
                            self.creator_ids.add(creator_id)
                            self.project_ids.add(project_id)
                            self.unique_rows.add(row_id)
                            rows.append(data)



                # Display counters
                print(f"Added by Creators: {self.CREATOR_COUNTER}, Added by Project: {self.PROJECT_COUNTER}, Skipped: {self.SKIPPED_COUNTER}")
                print(f"Skipped rows by state: {', '.join([f'{state}: {count}' for state, count in self.DROP_STATES.items()])}")
                print('\n')
                # Reset counters for the next file
                self.reset_counters()
            return self.rows

        def to_dataframe(self):
            return pd.DataFrame(self.rows)
        
        