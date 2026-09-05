#!/usr/bin/env python3
import json
import re
import sqlite3
import sys

DB = "/Users/ozzy/Library/Application Support/com.teamos.teamosFlutter/TeamOS/episodic_memory/faa8e9ce454f3b41e38119ee896f6180.sqlite3"
query = " ".join(sys.argv[1:]).strip()
terms = list(dict.fromkeys(re.findall(r"[\w-]{2,}", query.lower())))[:20]
if not terms:
    print("[]")
    raise SystemExit(0)
match = " OR ".join('"' + term.replace('"', '""') + '"' for term in terms)
connection = sqlite3.connect(DB)
rows = connection.execute("""
  SELECT e.id, e.run_id, e.stage, e.kind, e.created_at,
         snippet(episodic_events_fts, 0, '[', ']', ' … ', 40)
  FROM episodic_events_fts
  JOIN episodic_events e ON e.rowid = episodic_events_fts.rowid
  WHERE episodic_events_fts MATCH ?
  ORDER BY bm25(episodic_events_fts), e.created_at DESC
  LIMIT 12
""", (match,)).fetchall()
print(json.dumps([
  {"episode_id": row[0][:12], "run_id": row[1], "stage": row[2],
   "kind": row[3], "created_at": row[4], "excerpt": row[5]}
  for row in rows
], indent=2))
