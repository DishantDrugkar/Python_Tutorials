info = {
    "name" : "Dishant",
    "age" : 21,
    "Address" : "Tokyo",
    "cgpa" : 7.4,
    "girlfriend" : False,

}
print(info)

print(info["age"])


#------------------------------------------ Nested Dictionary --------------------------------------------------

student = {
    "name" : "Roystu",
    "Subjects" : {
        "Phy" : 87,
        "Che" : 45,
        "Bio" : 96
    } 
}

print(student["Subjects"])