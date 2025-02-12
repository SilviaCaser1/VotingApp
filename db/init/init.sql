CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    option TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO votes (option) VALUES ('Option A'), ('Option B');
 
