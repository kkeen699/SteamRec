import ast
import numpy as np
import gzip


DATA_DIR = "../data/"
USER_ITEM = "australian_users_items.json"
REVIEW = "australian_user_reviews.json"

def user_item_preprocessing():
  data = {}
  user_map = {}
  item_map = {}
  item_name_map = {}

  delete_game = []
  with open(DATA_DIR + "delete_game", 'r') as f:
    for line in f.readlines():
      delete_game.append(line[:-1])
  
  print("processing user-item data...")
  with open(DATA_DIR + USER_ITEM, 'r', encoding='utf-8') as f:
    for line in f.readlines():
      d_in = ast.literal_eval(line)

      items = d_in["items"]
      u_item = {}
      for item in items:
        item_id = item["item_id"]
        item_name = item["item_name"]
        play_time = int(item["playtime_forever"])

        if item_name not in delete_game:
          # item_id is new or not
          iid = len(item_map)
          if item_id in item_map:
            iid = item_map[item_id]
          else:
            item_map[item_id] = iid
            item_name_map[iid] = item_name
          
          # purchase = 0, play = 1, play > 10hr = 2
          if play_time > 0:
            if play_time >= 600:
              u_item[iid] = 2
            else:
              u_item[iid] = 1
          else:
            u_item[iid] = 0
      
      if len(u_item) > 0:
        user_id = d_in["user_id"]
        uid = len(user_map)
        if user_id in user_map:
          uid = user_map[user_id] 
          data[uid].update(u_item)
        else:
          user_map[user_id] = uid
          data[uid] = u_item
  
  print("processing review data...")
  with open(DATA_DIR + REVIEW, 'r', encoding='utf-8') as f:
    for line in f.readlines():
      d_in = ast.literal_eval(line)

      reviews = d_in["reviews"]
      u_item = {}
      for review in reviews:
        item_id = review["item_id"]
        recommend = review["recommend"]

        if item_id in item_map:
          iid = item_map[item_id]
          if recommend:
            u_item[iid] = 3
      
      user_id = d_in["user_id"]
      if user_id in user_map:
        uid = user_map[user_id] 
        data[uid].update(u_item)

  print("output file...")
  with gzip.open(DATA_DIR+"steam.user_item_map.gz", "w") as f:
    for uid in data:
      dout = {}
      dout['user_id'] = uid
      dout['items'] = data[uid]
      f.write((str(dout)+"\n").encode("utf-8"))

  np.savetxt(DATA_DIR + "steam_user_map.csv", np.array(list(user_map.items())), fmt="%s", delimiter=",")
  np.savetxt(DATA_DIR + "steam_item_map.csv", np.array(list(item_map.items())), fmt="%s", delimiter=",")
  np.savetxt(DATA_DIR + "steam_item_name.csv", np.array(list(item_name_map.items())), fmt="%s", delimiter=",")

if __name__ == "__main__":
  user_item_preprocessing()