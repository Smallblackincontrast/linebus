"""
MECE原则 (发音 me-see,“Mutually Exclusive，Collectively Exhaustive”) 相互独立,完全穷尽,不重不漏
"""
if __name__ == '__main__':

    # if语句就是根据布尔值来判断程序的走向
    adult_min_age = 18
    infant_max_age = 3

    # if-elif-else
    the_age_of_light_snow = 3
    if the_age_of_light_snow <= infant_max_age:
        print("infant")
    elif the_age_of_light_snow >= adult_min_age:
        print("adult")
    else:
        print("children")
