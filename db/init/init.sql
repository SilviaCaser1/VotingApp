CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    vote TEXT NOT NULL
);
--CREATE TABLE IF NOT EXISTS votes (
--    id SERIAL PRIMARY KEY,
--    option TEXT NOT NULL,
--    created_at TIMESTAMP DEFAULT NOW()
--);

--INSERT INTO votes (vote) VALUES ('Option A'), ('Option B');