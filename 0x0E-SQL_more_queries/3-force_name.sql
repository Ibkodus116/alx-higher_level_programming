-- Create a Taable id it doesn't exist
-- Queary the DB for table creation
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
