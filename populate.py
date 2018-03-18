import os
import profile
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pawpals_project.settings")

import django
django.setup()

from django.utils import timezone
from pawpals.models import *
from django.core.files import File


def populate():
    
    ### In Dogs We Trust data ###
    dog_trust_dogs = [
        {"name" : "Bailey",
         "bio" : "Very good boy.",
         "profile_picture" : "bailey.jpg",
         "breed" : "Chihuahua",
         "difficulty" : 1,
         "size" : "S",
         "gender" : "M",
         "is_puppy" : False,
         "is_childfriendly" : True},
        {"name" : "Difen",
         "bio" : "Extremely good boy.",
         "profile_picture" : "difen.jpg",
         "breed" : "Mongrel",
         "difficulty" : 1,
         "size" : "L",
         "gender" : "M",
         "is_puppy" : False,
         "is_childfriendly" : True},
        {"name": "Lisa",
         "bio": "Fluffy lady.",
         "profile_picture": "lisa.jpg",
         "breed": "Chow chow",
         "difficulty": 5,
         "size": "S",
         "gender": "F",
         "is_puppy": True,
         "is_childfriendly": True},
        {"name": "Atos",
         "bio": "Old but strong! Huge. Obedient. Protective.",
         "profile_picture": "atos.jpg",
         "breed": "Mongrel",
         "difficulty": 1,
         "size": "L",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": True},
        {"name": "Sawa",
         "bio": "Very playful, active, guard dog.",
         "profile_picture": "sawa.jpg",
         "breed": "Mongrel",
         "difficulty": 5,
         "size": "M",
         "gender": "F",
         "is_puppy": False,
         "is_childfriendly": False}
        ]
    
    dog_trust_manager = {"username" : "jsmith",
                        "fullname" : "John Smith",
                        "phone_contact" : "+44 1111111111",
                        "email" : "jsmith@mail.co.uk",
                        "profile_picture" : None
                        }

    ### Big Hearts For Pets data ###

    hearts_dogs = [
        {"name": "Bailey",
         "bio": "Calm, loves running.",
         "profile_picture": "husky.jpg",
         "breed": "Husky",
         "difficulty": 2,
         "size": "L",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": True},
        {"name": "Helix",
         "bio": "Loves purple balls",
         "profile_picture": "helix.jpg",
         "breed": "Shih-tzu",
         "difficulty": 3,
         "size": "S",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": True},
        {"name": "Orbit",
         "bio": "Loves cuddles and treats.",
         "profile_picture": "orbit.jpg",
         "breed": "Jisu-lee",
         "difficulty": 4,
         "size": "M",
         "gender": "N",
         "is_puppy": False,
         "is_childfriendly": False},
        {"name": "Amino",
         "bio": "Has a long tongue",
         "profile_picture": "amino.jpg",
         "breed": "Shih-tzu",
         "difficulty": 4,
         "size": "S",
         "gender": "N",
         "is_puppy": False,
         "is_childfriendly": True},
    ]

    hearts_manager = {"username": "abrown",
                         "fullname": "Anna Brown",
                         "phone_contact": "+44 2222222222",
                         "email": "abrown@mail.co.uk",
                        "profile_picture" : None
                         }
    
    ### Speedwagon Foundation data ###

    speedwagon_dogs = [
        {"name": "Jonathan",
         "bio": "Gentle and caring, very loyal.",
         "profile_picture": "jonathan.jpg",
         "breed": "Chow chow",
         "difficulty": 2,
         "size": "L",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": True},
        {"name": "Joseph",
         "bio": "Playful, very tricky!",
         "profile_picture": "joseph.jpg",
         "breed": "Shiba Inu",
         "difficulty": 5,
         "size": "L",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": False},
        {"name": "Jotaro",
         "bio": "Wary of strangers but has a heart of gold.",
         "profile_picture": "jotaro.jpg",
         "breed": "Shiba Inu",
         "difficulty": 4,
         "size": "L",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": False},
        {"name": "Josuke",
         "bio": "He's just crazy energetic",
         "profile_picture": "josuke.jpg",
         "breed": "Mongrel",
         "difficulty": 4,
         "size": "M",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": True},
        {"name": "Giorno",
         "bio": "Very charismatic dog",
         "profile_picture": "giorno.jpg",
         "breed": "Terrier",
         "difficulty": 4,
         "size": "M",
         "gender": "M",
         "is_puppy": True,
         "is_childfriendly": True},
        {"name": "Jolyne",
         "bio": "Loves long walks on a beach and warm bubbly baths.",
         "profile_picture": "jolyne.jpg",
         "breed": "Mongrel",
         "difficulty": 4,
         "size": "M",
         "gender": "F",
         "is_puppy": False,
         "is_childfriendly": True},
        {"name": "Johnny",
         "bio": "Tougher than he looks!",
         "profile_picture": "johnny.jpg",
         "breed": "Mongrel",
         "difficulty": 4,
         "size": "S",
         "gender": "M",
         "is_puppy": True,
         "is_childfriendly": True},
        {"name": "Josuke",
         "bio": "The other Josuke, not as energetic but very cute!",
         "profile_picture": "josuke2.jpg",
         "breed": "Mongrel",
         "difficulty": 4,
         "size": "M",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": True},
    ]

    speedwagon_manager = {"username": "speedwagon",
                         "fullname": "Robert E. O. Speedwagon",
                         "phone_contact": "+44 3333333333",
                         "email": "speedwagon@mail.co.uk",
                        "profile_picture" : None
                         }
    
    
    ### Wag&Bark Centre data ###

    wagbark_dogs = [
        {"name": "Seph",
         "bio": "Lazy, doesn't like walks.",
         "profile_picture": "seph.jpg",
         "breed": "Pug",
         "difficulty": 2,
         "size": "S",
         "gender": "M",
         "is_puppy": False,
         "is_childfriendly": True},
        {"name": "Jaga",
         "bio": "Always happy to go for a walk.",
         "profile_picture": "jaga.jpg",
         "breed": "Retriever",
         "difficulty": 3,
         "size": "L",
         "gender": "F",
         "is_puppy": False,
         "is_childfriendly": False},
    ]

    wagbark_manager = {"username": "wbman",
                         "fullname": "Rose Goldman",
                         "phone_contact": "+44 4444444444",
                         "email": "wagandbark@mail.co.uk",
                        "profile_picture" : None
                         }
    
    ### Shelters ###

    shelters = {"In Dogs We Trust" : {
                    "manager": dog_trust_manager,
                    "dogs": dog_trust_dogs,
                    "bio": "0/1 Doggo Road, Glasgow G0 A00",
                    "webpage": "https://www.dogstrust.org.uk/our-centres/glasgow/",
                    "phone_contact": "+44 1111111112",
                    "availability_info": "Everyday 8am-3pm",
                    "location": "Glasgow",
                    "avg_rating": 4,
                    "profile_picture" : "dog_trust.jpg"
                    },
                "Big Hearts For Pets" : {
                    "manager": hearts_manager,
                    "dogs": hearts_dogs,
                    "bio": "Rehoming for cats, dogs & rabbits",
                    "webpage": "https://www.bluecross.org.uk/yorkshire-thirsk-rehoming-centre",
                    "phone_contact": "+44 1111111113",
                    "availability_info": "Tuesday - Saturday 8am-3pm",
                    "location": "Yorkshire YO B11",
                    "avg_rating": 3,
                    "profile_picture" : "hearts.jpg"
                    },
                "Speedwagon Foundation" : {
                    "manager": speedwagon_manager,
                    "dogs": speedwagon_dogs,
                    "bio": "The foundation dedicates itself to animal care and environmental conservation.",
                    "webpage": "https://www.bluecross.org.uk/yorkshire-thirsk-rehoming-centre",
                    "phone_contact": "+44 1111111114",
                    "availability_info": "All week 6am-6pm",
                    "location": "Glasgow, 19 Speedwagon Road, G2 C22",
                    "avg_rating": 3,
                    "profile_picture" : "speedwagon.jpg"
                    },
                "Wag&Bark Centre" : {
                    "manager": wagbark_manager,
                    "dogs": wagbark_dogs,
                    "bio": "Wag&Bark centre is a small neighbourhood initiative focusing on helping homeless animals from Smallvile area.",
                    "webpage": "https://www.bluecross.org.uk/yorkshire-thirsk-rehoming-centre",
                    "phone_contact": "+44 1111111115",
                    "availability_info": "Wednesday 2pm - 8pm",
                    "location": "Smallvile",
                    "avg_rating": 3,
                    "profile_picture" : None
                    }}
    
    ### Shelter, dog, manager creation ###

    for shelter, shelter_data in shelters.items():
        manager_data = shelter_data["manager"]
        sh_manager = add_user(is_manager=True,
                             username=manager_data["username"],
                             fullname=manager_data["fullname"],
                             email=manager_data["email"],
                             phone_contact=manager_data["phone_contact"],
                             profile_picture = manager_data["profile_picture"])
            
        sh = add_shelter(manager=sh_manager,
                         name=shelter,
                         bio=shelter_data["bio"],
                         webpage=shelter_data["webpage"],
                         phone_contact=shelter_data["phone_contact"],
                         availability_info=shelter_data["availability_info"],
                         location=shelter_data["location"],
                         avg_rating=shelter_data["avg_rating"],
                         profile_picture = shelter_data["profile_picture"])
        
        for dog in shelter_data["dogs"]:
            add_dog(shelter=sh,
                    name=dog["name"],
                    bio=dog["bio"],
                    breed=dog["breed"],
                    difficulty=dog["difficulty"],
                    size=dog["size"],
                    gender=dog["gender"],
                    is_puppy=dog["is_puppy"],
                    is_childfriendly=dog["is_childfriendly"],
                    profile_picture=dog["profile_picture"])
    

    ### Users ###

    users = {"hendo": {"fullname" : "Henrietta Dobras",
                       "email" :"hendo@gmail.com",
                       "phone_contact" : "+44 2222222221",
                       "profile_picture" : "hendo.jpg"},
            "yerba4life": {"fullname" : "Elliot Black",
                        "email" : "optiplex@mail.com",
                        "phone_contact": "+44 2222222223",
                        "profile_picture" : "yerba4life.jpg"},
            "lilylith": {"fullname" : "Lily Lithium",
                         "email" : "llith@mail.com",
                         "phone_contact" : "+44 2222222224",
                         "profile_picture" : "lilylith.jpg"},
            }
    
    
    ### Users creation ###
    for user, user_data in users.items():
        u = add_user(is_manager=False,
                     username=user,
                     fullname=user_data["fullname"],
                     email=user_data["email"],
                     phone_contact=user_data["phone_contact"],
                     profile_picture=user_data["profile_picture"]
                     )

    ### Request creation ###
    requests = {0 : {"user" : StandardUser.objects.all().get(pk = "lilylith"), 
                     "shelter_manager" : ShelterManagerUser.objects.all().get(pk = "jsmith"), 
                     "dog" : Dog.objects.all().get(pk = 1), 
                     "date" : "2018-03-21T13:20:30+03:00",
                     "confirmation_status" : "C",
                     "message" : "Hi! Can I walk that doggie next week?"},
                1 : {"user" : StandardUser.objects.all().get(pk = "hendo"), 
                     "shelter_manager" : ShelterManagerUser.objects.all().get(pk = "jsmith"), 
                     "dog" : Dog.objects.all().get(pk = 2), 
                     "date" : "2018-03-21T13:20:30+03:00",
                     "confirmation_status" : "C",
                     "message" : "Next Friday 11am?"},
                2 : {"user" : StandardUser.objects.all().get(pk = "lilylith"), 
                     "shelter_manager" : ShelterManagerUser.objects.all().get(pk = "jsmith"), 
                     "dog" : Dog.objects.all().get(pk = 3), 
                     "date" : "2018-03-21T13:20:30+03:00",
                     "confirmation_status" : "C",
                     "message" : "Usual?"},
                }
    
    for request_id, request in requests.items():
        add_request(user = request["user"], 
                    shelter_manager = request["shelter_manager"], 
                    dog = request["dog"], 
                    date = request["date"], 
                    confirmation_status = request["confirmation_status"], 
                    message = request["message"])


    # Reviews creation
    reviews = {Request.objects.get(pk = 1) : {"user" : requests[0]["user"],
                                               "dog" : requests[0]["dog"],
                                               "rating": 5,
                                               "comment": "Good doggo!",
                                               "date": "2018-02-01T13:20:30+03:00"},
               Request.objects.get(pk = 2) : {"user" : requests[1]["user"],
                                               "dog" : requests[1]["dog"],
                                               "rating": 4,
                                               "comment": "Very playful.",
                                               "date": "2018-02-01T13:20:30+03:00"},
               Request.objects.get(pk = 3) : {"user" : requests[2]["user"],
                                               "dog" : requests[2]["dog"],
                                               "rating": 1,
                                               "comment": "Very badly behaved.",
                                               "date": "2018-02-01T13:20:30+03:00"},                               
            }
    
    for request, review_data in reviews.items():
         add_review(request = request,
                    user = review_data["user"],
                   dog=review_data["dog"],
                   date=review_data["date"],
                   rating=review_data["rating"],
                   comment=review_data["comment"]
                   )


    ### Print confirmation ###
    
    # Print shelter, dogs and manager
    print("\n>>> Shelters and dogs")
    for sh in Shelter.objects.all():
        print(str(sh) + " managed by: " +str(sh.manager))
        for dog in Dog.objects.filter(dog_shelter=sh):
            print("\t - " + str(dog.pk) + " | " + str(dog))
    print("\n>>> Users and comments")
    for user in StandardUser.objects.all():
        print(str(user) + "'s comments:")
        for review in Review.objects.filter(reviewing_user = user):
            print("\t - " + str(review))
    print("\n>>> Requests: ")    
    for request in Request.objects.all():
        print("\t - " + str(request))




def add_user(is_manager, username, fullname, email, phone_contact, profile_picture=None):
    
    if is_manager:
        user = ShelterManagerUser.objects.get_or_create(username=username)[0]
    else:
        user = StandardUser.objects.get_or_create(username=username)[0]

    user.fullname = fullname
    user.email = email
    user.phone_contact = phone_contact
    
    user.save()
    
    if profile_picture:
        user.profile_picture.save(profile_picture, File(open(os.path.join("population_files", "users", profile_picture), "rb")))
    else:
        user.profile_picture = profile_picture 
    
    return user


def add_shelter(manager, name, bio, webpage, phone_contact, availability_info, location, avg_rating, profile_picture=None):
    sh = Shelter.objects.get_or_create(manager=manager, name=name)[0]
    sh.bio = bio
    sh.webpage = webpage
    sh.profile_picture = profile_picture
    sh.phone_contact = phone_contact
    sh.availability_info = availability_info
    sh.location = location
    sh.avg_difficulty_rating = avg_rating
    sh.save()
    
    if profile_picture:
        sh.profile_picture.save(profile_picture, File(open(os.path.join("population_files", "shelters", profile_picture), "rb")))
    else:
        sh.profile_picture = profile_picture 
    
    return sh


def add_dog(shelter, name, bio, breed, difficulty, size, gender, profile_picture=None, is_puppy=False, is_childfriendly=False):
    
    
    d = Dog.objects.get_or_create(name=name, dog_shelter=shelter)[0]

    d.bio = bio 
      
    d.breed = breed 
    d.difficulty = difficulty
    d.size = size
    d.gender = gender        
    d.is_puppy = is_puppy
    d.is_childfriendly = is_childfriendly

    d.save()
    
    if profile_picture:
        d.profile_picture.save(profile_picture, File(open(os.path.join("population_files", "dogs", profile_picture), "rb")))
    else:
        d.profile_picture = profile_picture 
    
    return d


def add_review(user, dog, request, date, rating, comment):
    
    rev = Review.objects.get_or_create(reviewing_user=user, reviewed_dog=dog, date=date, request=request)[0]

    rev.difficulty_rating = rating
    rev.comment = comment
    
    rev.save()
    
    return rev

    
def add_request(user, shelter_manager, dog, date, confirmation_status, message):
    
    req = Request.objects.get_or_create(requesting_user=user, request_manager=shelter_manager, requested_dog=dog)[0]
    
    req.date = date
    
    req.status = confirmation_status 
    req.message = message  
    
    req.save()
    
    return req


if __name__ == "__main__":
    print("Starting population script...")
    populate()

