-- Task : 9 index
CREATE INDEX idx_name_first_score ON names ( name(1), score );