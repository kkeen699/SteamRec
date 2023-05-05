import sys
import csv
import json
import random
from bing_image_urls import bing_image_urls


def get_top_ten():
    user_top_ten_games = {i: [] for i in range(6)}
    user_top_five_genres = ['Guess You Like']
    genre_map = {}
    sys.stdout.flush()

    with open('genre_map') as f:
        for row in f:
            line = eval(row)
            for name in line.keys():
                genre_map[line[name]] = name

    with open('user0') as user0:
        user_ranking = []
        for ranking in user0:
            user_ranking.append(ranking)
    user_ranking = sorted(range(len(user_ranking)),
                          key=lambda i: user_ranking[i], reverse=True)
    user_top_ten_games[0] = sorted(
        range(len(user_ranking)), key=lambda i: user_ranking[i], reverse=True)[:10]
    new_user = [random.randint(0, 7000) for i in range(10)]

    sys.stdout.flush()
    with open('ken_id_and_genre') as f:
        game_genre_map = {}
        for row in f:
            line = eval(row)
            game_genre_map[line['ken_game_id']] = line['genre']

    sys.stdout.flush()
    with open('user_id_top_ten_genre_preference') as f:
        user_genre_map = {}
        for row in f:
            line = eval(row)
            user_genre_map[line['user_id']] = line['genres']

    for i in range(1, len(user_top_ten_games)):
        genre = user_genre_map[0][i-1]
        user_top_five_genres.append(genre_map[genre])
        for game_id in user_ranking:
            if genre in game_genre_map[game_id] and game_id != 14:
                user_top_ten_games[i].append(game_id)
                if len(user_top_ten_games[i]) == 10:
                    break

    sys.stdout.flush()
    with open('steam_item_name.csv', newline='', encoding="utf-8") as csvfile:
        game_id_name_map = {}
        spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
        for row in spamreader:
            game_id_name_map[int(row[0])] = row[1]

    sys.stdout.flush()
    for i in range(len(user_top_ten_games)):
        for idx, item in enumerate(user_top_ten_games[i]):
            user_top_ten_games[i][idx] = game_id_name_map[item]

    for idx, item in enumerate(new_user):
        new_user[idx] = game_id_name_map[item]

    with open('user_0_genre.json', 'w') as fp:
        json.dump(user_top_five_genres, fp)

    return new_user, user_top_ten_games


def get_image(user_top_ten_games):
    for i in user_top_ten_games.keys():
        for idx, query in enumerate(user_top_ten_games[i]):
            img_url = bing_image_urls(query, limit=3)[2]
            user_top_ten_games[i][idx] = [query, img_url]
    with open('user_0_result.json', 'w') as fp:
        json.dump(user_top_ten_games, fp)


def new_user_get_image(new_user):
    for idx, query in enumerate(new_user):
        img_url = bing_image_urls(query, limit=2)[1]
        new_user[idx] = [query, img_url]
    with open('new_user_result.json', 'w') as fp:
        json.dump(new_user, fp)

    # Download the image to your local machine


new_user, user_top_ten_games = get_top_ten()
get_image(user_top_ten_games)
new_user_get_image(new_user)
