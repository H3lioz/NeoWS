CREATE TABLE asteroids
(id text NOT NULL,
name text NOT NULL,
size numeric(7,3),
size_category text,
magnitude numeric(5,2),
latest_research_date date NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE observed_parameters
(id text NOT NULL,
close_approach_date date NOT NULL,
orbiting_body text NOT NULL,
relative_velocity_km_s numeric(5,2),
miss_distance_km numeric(12,2),
miss_distance_astr numeric(5,4),
observe_research_date date NOT NULL,
FOREIGN KEY(id)
   REFERENCES asteroids (id)
);

