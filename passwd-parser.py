import pwd
import grp
import json

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

all_users = get_all_users()

print (json.dumps((all_users), indent=5))







    
