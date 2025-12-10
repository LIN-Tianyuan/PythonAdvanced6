def user_info(name, age, gender):
    print(f"Votre nom est {name}, votre âge est {age} et votre sexe est {gender}.")

# 位置参数 arguments positionnels
user_info("Alex", 18, "Homme")

# 关键字参数 arguments par mot-clé
# 关键字参数就可以不用按顺序传参
user_info(age=18, gender="Homme", name="Alex")
# 位置参数和关键字参数可以混着用，但是位置参数必须放前面
user_info("Alex", gender="Homme", age=18)

# 默认参数 arguments par défaut
def user_info1(name, age, gender="Homme"):
    print(f"Votre nom est {name}, votre âge est {age} et votre sexe est {gender}.")

user_info1("Alex", 18)
user_info1("Alex", 18, "Femme")

print("----------")

# 不定长参数 arguments de longueur indéterminée
# 位置参数 *args: arguments
def user_info2(*args):
    # print(args)
    for i in args:
        print(i)

# user_info2(1)
# user_info2(1, 2)
# user_info2(1, 2, 3)
user_info2("Alex", 18)

# 关键字参数 **kwargs: keyword arguments
def user_info3(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")

user_info3(name="Alex", age=18, gender="Homme")



