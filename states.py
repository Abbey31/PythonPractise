states = input(("Enter your state and get your geo political zone ")).title()

match states:
    case "Oyo"|"Ogun"|"Osun"|"ondo"|"Ekiti"|"Lagos":
          print("You are from the south-west") 
    case "Akwa Ibom"|"Bayelsa"|"Cross River"|"Delta"|"Edo"|"Rivers":
          print("You are from South South")
    case "Abia"|"Anambra"|"Ebonyi"|"Enugu"|"Imo":
        print("You are from south-east")
    case "Jigawa"|"Kaduna"|"Kano"|"Katsina"|"Kebbi"|"Sokoto"|"Zamfara":
        print("You are from North-west")
    case "Adamawa"|"Bauchi"|"Borno"|"Gombe"|"Taraba"|"Yobe":
        print("You are from North-East")
    case "Benue"|"Kogi"|"Kwara"|"Nassarawa"|"Niger"|"Plateau"|"FCT":
        print("You are from North-central")
