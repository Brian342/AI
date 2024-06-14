# from pomegranate import *
#
# # Define starting probabilities
# start = DiscreteDistribution({
#     "sun": 0.5,
#     "rain": 0.5
# })
#
# # Define transition model
# transitions = ConditionalProbabilityTable([
#     ["sun", "sun", 0.8],
#     ["sun", "rain", 0.2],
#     ["rain", "sun", 0.3],
#     ["rain", "rain", 0.7]
# ], [start])
#
# # Create Markov chain
# model = MarkovChain([start, transitions])
#
# # sample 50 states from chain
# print(model.sample(50))
#
# # from rembg import remove
# # from PIL import Image
# # input_path = "/Users/briankimanzi/Documents/html-doc/Portfolio/Kim.png"
# # output_path ="/Users/briankimanzi/Documents/html-doc/Portfolio/Kim.png"
# # inp = Image.open(input_path)
# # output = remove(inp)
# # output.save(output_path)
# # Image.open("/Users/briankimanzi/Documents/html-doc/Portfolio/Kim.png")
#
