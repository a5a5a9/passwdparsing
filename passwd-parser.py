import pwdd
import grpp
import json
import os
import argparse



# Forms a dictionary of users with matching key/values from database

def form_user_dict(user):
   user_dict = {}
   user_dict['name'] = user.pw_name
   user_dict['uid'] = user.pw_uid
   user_dict['full name'] = user.pw_gecos
   group_names = list ( g.gr_name for g in grpp.getgrall() if user.pw_name in g.gr_mem )
   user_dict['groups'] = group_names
   return user_dict

# Gets ALL users from database

def get_all_users():
    all_users = []
    all_users = pwdd.getpwall()
    all_user_list = []
    for user in all_users:
        user_dict = form_user_dict(user)
        all_user_list.append(user_dict)
    return {d.pop('name'): d for d in all_user_list}



def run_app(passwd_path, group_path):
 
    todo_users = get_all_users()
    print (json.dumps((todo_users), indent=5))
    

def main():
    parser = argparse.ArgumentParser(description = 'This is a Passwd Parser Program')
    parser.add_argument ('-r', '--run', action='store_true',  help='run the program')
    parser.add_argument ('-p','--passwd', help='passwd_path', default='/etc/passwd')
    parser.add_argument ('-g','--group', help='group_path',  default='/etc/group')
    args = parser.parse_args()
    os.environ["ETC_PASSWD"] = args.passwd
    os.environ["ETC_GROUP"] = args.group
   
    if args.run:
        run_app(passwd_path=args.passwd, group_path=args.group)
       
    else:
        print ("No arguments were introduced! Good Bye!")

    
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()