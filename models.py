from datetime import datetime
import random

bugs = []

class Bug:
    def __init__(self, created_by, priority, severity, title, description):
        self.bug_id = len(bugs) + 1
        self.created_by = created_by
        self.created_on = datetime.utcnow()
        self.updated_on = self.created_on
        self.priority = priority
        self.severity = severity
        self.title = title
        self.description = description 
