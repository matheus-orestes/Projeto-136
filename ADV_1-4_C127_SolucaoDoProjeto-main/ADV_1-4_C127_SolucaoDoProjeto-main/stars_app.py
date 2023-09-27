import pandas
import csv

stars_data_rows = rows[1:]
final_stars_list = []
for stars_data in stars_data_rows:
    temp_dict = {
        "name": stars_data[1],
        "distance_from earth": stars_data[2],
        "star_mass": stars_data[3],
        "stars_type": stars_data[6],
        "star_radius": stars_data[7],
        "distance_from_their_sun": planet_data[8],
        "orbital_period": planet_data[9],
        "gravity": planet_data[20],
        "orbital_speed": planet_data[21]
  }
    temp_dict["specifications"] = final_dict[planet_data[1]]
    final_planet_list.appemd[temp_dict]
    print(final_planet_list)
    


    
