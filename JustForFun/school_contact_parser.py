import re

class_name_prefix = "APR 2020 Class: "

child_entry_separator = " ; "
class_entry_separator = " ::: "

def load_directory_from_file(file="./data/example_school_directory.txt"):
    school_name = "example"
    directory_entries = []
    line_number = 1
    cur_record_name = ""
    cur_class = ""
    cur_child = ""
    records = {} # records => {"Parent":[0:"phone", 1:"email", 2:"children", 3:classes", 4:"Mom/Dad"]}

    with open(file, 'r', encoding="utf8") as lines:
        for line in lines:
            line = line.strip()
            cur_line = line.split(":")
            compare_string = cur_line[0].lower()

            # set current class
            if len(cur_line) == 1:
                cur_class = class_name_prefix + cur_line[0]

            # set current chile
            elif compare_string == "child's name":
                cur_child = cur_line[1]
            
            # set current parent and create a new record
            elif compare_string == "name (mom)" or compare_string == "name (dad)":
                cur_record_name = cur_line[1].strip()
                if cur_record_name not in records:
                    # records => [0:"phone", 1:"email", 2:"children", 3:"classes", 4:"Mom/Dad"]
                    status = "Mom" if "Mom" in cur_line[0] else "Dad"
                    new_class_entry = school_name + class_entry_separator + cur_class
                    records[cur_record_name] = ["", "", cur_child, new_class_entry, status]
                else:
                    records[cur_record_name][2] += child_entry_separator + cur_child
                    records[cur_record_name][3] += class_entry_separator + cur_class

            # add phone to current record
            elif compare_string == "phone number":
                if records[cur_record_name][0] == "":
                    clean_phone = re.sub("[^0-9]", "", cur_line[1])
                    records[cur_record_name][0] = clean_phone

            # add email to current record
            elif compare_string == "email":
                if records[cur_record_name][1] == "":
                    records[cur_record_name][1] = cur_line[1]
            
            else:
                print("Non Conforming Line # {}: {}".format(line_number, line))

            line_number += 1

    #convert dictionary to list
    for parent in records.keys():
        directory_entries.append([parent, *records[parent]])

    return directory_entries

def format_phone_number(unformatted_phone):
    return "({}){}-{}".format(unformatted_phone[:3],unformatted_phone[3:6], unformatted_phone[6:]) if unformatted_phone != "" else ""

def print_directory(directory):
    for entry in directory:
        print("| {name:25} | {phone:14} | {email:30} | {children:40} | {classes:60} | {status}".format(name=entry[0], phone=format_phone_number(entry[1]), email=entry[2], children=entry[3], classes=entry[4], status=entry[5]))

def output_to_google_csv(directory, file="student_parent_directory.csv"):
    with open(file, 'w', encoding="utf8") as lines:
        #output header
        #Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 - Type,E-mail 2 - Value,E-mail 3 - Type,E-mail 3 - Value,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value,Phone 3 - Type,Phone 3 - Value,Address 1 - Type,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address,Organization 1 - Type,Organization 1 - Name,Organization 1 - Yomi Name,Organization 1 - Title,Organization 1 - Department,Organization 1 - Symbol,Organization 1 - Location,Organization 1 - Job Description,Website 1 - Type,Website 1 - Value,Website 2 - Type,Website 2 - Value,Custom Field 1 - Type,Custom Field 1 - Value
        header = "Name,Given Name,Family Name,Gender,Notes,Group Membership,Phone 1 - Type,Phone 1 - Value,E-mail 1 - Type,E-mail 1 - Value"
        lines.write(header)


        #iterate across directory
        for parent in directory:
            Name = parent[0]
            phone = format_phone_number(parent[1])
            email = parent[2]
            children = parent[3]
            group_membership = parent[4]
            parental_status = parent[5]
            given_name = ""
            family_name = ""
            # break apart name
            if " " in Name:
                name_list = parent[0].split()
                given_name, family_name = name_list[0], name_list[1]
            else:
                given_name = Name
            gender = "Male" if parental_status == "Dad" else "Female"

            Notes = "{} of: {}".format(parental_status, children)

            lines.write("\n")
            lines.write("{},{},{},{},{},{},{},{},{},{}".format(Name, given_name, family_name, gender, Notes, group_membership, "", phone, "",email)) 

            

if __name__ == "__main__":
    directory = load_directory_from_file()

    print_directory(directory)
    output_to_google_csv(directory)