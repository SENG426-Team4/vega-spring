#! /usr/bin/env python3

import csv

NUM_USERS = 3010

if __name__ == "__main__":
    user_list = []
    
    for i in range(NUM_USERS):
            username = "test" + str(i+1)
            password = "test" + str(i+1) + "password"
            first_name = str(i+1) + "First"
            last_name = str(i+1) + "Last" 
            user = [username, password, first_name, last_name]
            user_list.append(user)

    with open("LoginData.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(user_list)