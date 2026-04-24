-- Huntmaster database schema
-- SQLite-compatible and intended to migrate cleanly to Cloudflare D1.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS programs (
  id TEXT PRIMARY KEY,
  handle TEXT NOT NULL,
  name TEXT NOT NULL,
  min_bounty INTEGER,
  max_bounty INTEGER,
  last_tested TEXT,
  status TEXT NOT NULL DEFAULT 'active',
  policy_text TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS scope (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  program_id TEXT NOT NULL,
  asset_type TEXT NOT NULL,
  asset_value TEXT NOT NULL,
  eligible INTEGER NOT NULL,
  instruction TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (program_id) REFERENCES programs(id)
);

CREATE TABLE IF NOT EXISTS scope_decisions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  program_id TEXT NOT NULL,
  target TEXT NOT NULL,
  decision TEXT NOT NULL,
  reason TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (program_id) REFERENCES programs(id)
);

CREATE TABLE IF NOT EXISTS findings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  program_id TEXT NOT NULL,
  title TEXT NOT NULL,
  cvss_score REAL,
  cwe_id TEXT,
  asset TEXT NOT NULL,
  poc TEXT,
  evidence TEXT,
  apex_output TEXT,
  triage_status TEXT NOT NULL DEFAULT 'pending',
  triage_reason TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (program_id) REFERENCES programs(id)
);

CREATE TABLE IF NOT EXISTS reports (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  finding_id INTEGER NOT NULL,
  draft_markdown TEXT NOT NULL,
  h1_report_id TEXT,
  status TEXT NOT NULL DEFAULT 'draft',
  bounty_amount INTEGER,
  submitted_at TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (finding_id) REFERENCES findings(id)
);

CREATE TABLE IF NOT EXISTS skill_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  program_id TEXT,
  skill_name TEXT NOT NULL,
  outcome TEXT NOT NULL,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (program_id) REFERENCES programs(id)
);

CREATE INDEX IF NOT EXISTS idx_scope_program_id ON scope(program_id);
CREATE INDEX IF NOT EXISTS idx_findings_program_id ON findings(program_id);
CREATE INDEX IF NOT EXISTS idx_reports_finding_id ON reports(finding_id);
