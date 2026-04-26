# import pickle
# def main():
#     courses = [["Python", 3],
#                ["Trig", 3],
#                ["Physics", 4],
#                ["Yoga", 2]]
#     with open("classes.bin", "wb") as file:
#         pickle.dump(courses, file)
#     with open("classes.bin", "rb") as file:
#         course_list = pickle.load(file)
#     i = 0
#     while i < len(course_list):
#         course = course_list[i]
#         print(course[0], course[1], end=" ")
#         i += 2

# main()

# import csv
# def main():
#     courses = [["Python", 3],
#                ["Trig", 3],
#                ["Physics", 4],
#                ["Yoga", 2]]
#     with open("courses.csv", "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(courses)
#     course_list = []
#     with open("courses.csv", newline="") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             course_list.append(row)
#     for i in range(len(course_list) - 2):
#         course = course_list[i]
#         print(f"{course[0]} ({course[1]})")
       
# main()

# import csv
# def main():
#     courses = [["Python", 3],
#                ["Trig", 3],
#                ["Physics", 4],
#                ["Yoga", 2]]
#     with open("courses.csv", "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(courses)
#     course_list = []
#     with open("courses.csv", newline="") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             course_list.append(row)
#     for i in range(len(course_list) - 2):
#         course = course_list[i]
#         print(f"{course[0]} ({course[1]})")
       
# main()

import csv
import sys
FILENAME = "names.csv"
def main():
    try:
        names = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                names.append(row)
    except FileNotFoundError as e:
        print(f"Could not find {FILENAME} file.")
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()
    print(names)      
if __name__ == "__main__":
    main()