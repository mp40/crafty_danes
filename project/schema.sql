drop table if exists beers;

create table beers (
  id integer primary key autoincrement,
  name text not null,
  brewery text not null,
  abv float not null,
  type text not null,
  receptacle_size integer not null,
  receptacle_type text not null
);
