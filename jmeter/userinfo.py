#! /usr/bin/env python3

import csv

NUM_USERS = 200

if __name__ == "__main__":
    user_list = []
    
    for i in range(NUM_USERS):
            username = "test" + str(i)
            password = "test" + str(i) + "password"
            first_name = str(i) + "First"
            last_name = str(i) + "Last" 
            user = [username, password, first_name, last_name]
            user_list.append(user)

    with open("LoginData.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(user_list)