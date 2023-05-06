# Recommendation Model

Our SteamRec project utilized the [Steam Video Game and Bundle Data](https://cseweb.ucsd.edu/~jmcauley/datasets.html#steam_data), and the recommend model was followed the paper [*"Item Recommendation on Monotonic Behavior Chains"* by Mengting Wan, et al.](https://cseweb.ucsd.edu/~jmcauley/pdfs/recsys18b.pdf).

- The recommendation model was implemented using Python 3.6 and TensorFlow 1.15.

- To train and evaluate the model, use `python3 train.py`.

- To get recommendation, use `python3 recommend.py`. The recommedation result would be 
![](/recommend/image/result.png)