import sys
import csv


DATA_DIR = "../data/"

def genre_preprocessing():
    sys.stdout.flush()

    genre_map = {}
    game_and_genre = {} 
    with open(DATA_DIR + 'steam_games.json') as game_info:
        with open(DATA_DIR + 'steam_genre_map','w') as f:
            for row in game_info:
                item_data = eval(row)
                this_game_genres = set()
                if "app_name" not in item_data:
                    continue
                if "genres" in item_data:
                    for genre in item_data["genres"]:
                        if genre not in genre_map:
                            genre_map[genre] = len(genre_map)
                            f.write(str({genre:genre_map[genre]}))
                            f.write('\n')
                        this_game_genres.add(genre_map[genre])
                if "tags" in item_data:
                    for genre in item_data["tags"]:
                        if genre not in genre_map:
                            genre_map[genre] = len(genre_map)
                            f.write(str({genre:genre_map[genre]}))
                            f.write('\n')
                        this_game_genres.add(genre_map[genre])
                game_and_genre[item_data["app_name"]] = this_game_genres


    item_genre_map = {}
    with open(DATA_DIR + 'steam_item_name.csv', newline='', encoding="utf-8") as csvfile:
        with open(DATA_DIR + 'steam_item_genre_map', 'w') as f:
            spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in spamreader:
                item_name = row[1]
                item_id = int(row[0])

                item_genre_map[item_id] = game_and_genre[item_name]
                f.write(str({"item_id":item_id, "genre":item_genre_map[item_id]}))
                f.write('\n')


    # user_id_genre_preference = {}
    # with open('steam.user_item_map') as f:
    #     with open('user_id_genre_preference', 'w') as w:
    #         with open('user_id_top_ten_genre_preference' , 'w') as w2:
    #             for row in f:
    #                 user = eval(row)
    #                 this_user_genre_preference = {}
    #                 uid = user["user_id"]
    #                 items = user["items"]
    #                 for item_id in items.keys():       
    #                     for genre in ken_id_and_genre[item_id]:
    #                         if genre not in this_user_genre_preference:
    #                             this_user_genre_preference[genre] = items[item_id]
    #                         else:
    #                             this_user_genre_preference[genre] += items[item_id]
    #                 user_id_genre_preference[uid] = this_user_genre_preference
    #                 top_ten_genre_preference = top_ten(this_user_genre_preference)
    #                 w.write(str({"user_id":uid,"genres":this_user_genre_preference}))
    #                 w.write("\n")
    #                 w2.write(str({"user_id":uid,"genres":top_ten_genre_preference}))
    #                 w2.write("\n")


# def top_ten(this_user_genre_preference):
#     sorted_list = sorted(list(this_user_genre_preference.items()),key=lambda x:x[1], reverse=True)
#     result = []
#     for i in range(min(len(sorted_list),10)):
#         result.append(sorted_list[i][0])
#     return result

if __name__ == "__main__":
    genre_preprocessing()
