-- create an index on the first letter of name and the score
CREATE INDEX IF NOT EXISTS idx_first_letter_name_score ON names (name(1), score);
