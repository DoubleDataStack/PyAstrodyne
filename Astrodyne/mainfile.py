import json
from starter import Start
from pathlib import Path

def read_config():
    config_path = Path("Astrodyne\config.json")
    with config_path.open("r") as config_file:
        config = json.load(config_file)
    return config

def main(n_body:int, 
         cgp:bool,
         mass_planet:float,
         radius_planet:float,
         color:dict[int,int,int],
         collision:bool,
         center_body:bool):
    
    Start().starter(n_body, cgp, mass_planet, radius_planet, color, collision, center_body)

if __name__ == "__main__":
    config = read_config()
    n_body = config["n_body"]
    cgp = config["generation_planet"]
    mass_planet = config["mass_planet"]
    radius_planet = config["radius_planet"]
    color_planet = config["color_planet"]
    collision:bool = config["collision"]
    center_body:bool = config["center_body"]
    main(n_body, cgp, mass_planet, radius_planet, color_planet, collision, center_body)
