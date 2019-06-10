import pwd
import grp
import json
import os
import argparse

def form_user_dict(user):
   user_dict = {}
   user_dict['name'] = user.pw_name
   user_dict['uid'] = user.pw_uid
   user_dict['full name'] = user.pw_gecos
   group_names = list ( g.gr_name for g in grp.getgrall() if user.pw_name in g.gr_mem )
   user_dict['groups'] = group_names
   return user_dict

def get_all_users():
    all_users = pwd.getpwall()
    all_user_list = []
    for user in all_users:
        user_dict = form_user_dict(user)
        all_user_list.append(user_dict)
    return {d.pop('name'): d for d in all_user_list}



def run_app(passwd_path, group_path):
    os.environ['ETC_PASSWD'] = passwd_path
    os.environ['ETC_GROUP'] = group_path
    all_users = get_all_users()
    print (json.dumps((all_users), indent=5))




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--run', '-r', action='store_true', help='run the program')
    parser.add_argument ('--passwd','-p', help='passwd_path', default="/etc/passwd")
    parser.add_argument ('--group','-g', help='group_path', default='/etc/group')
   
    args = parser.parse_args()

    if args.run:
        run_app(passwd_path=args.passwd, group_path=args.group)
       
    else:
        print ("No arguments were introduced! See ya!")

    
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()