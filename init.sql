CREATE TABLE github_actions (
    id SERIAL PRIMARY KEY,
    workflow_name TEXT,
    status TEXT,
    conclusion TEXT,
    created_at TIMESTAMP
);
