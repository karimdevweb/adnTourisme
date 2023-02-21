from flask import Flask, jsonify,render_template, request,Response
from flask_cors import CORS
import uuid
import json
import pandas as pd 
import numpy as np
import nltk 
import string
nltk.download('popular')
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# init  my app flask
app = Flask(__name__)
app.config.from_object(__name__)

 

CORS(app, resources={r"/*" : {'origin':"*"}})
# or
# CORS(app, resources={r"/*" : {'origin':"http://localhost:5173","allow_headers":"Access-Control-Allow-Origin" , "Access-Control-Allow-Headers": "*" , "Access-Control-Allow-Headers": "X-CSRF-Token"}})







df = pd.read_csv('adn_csv/df_renamed_adn.zip' ,index_col=False ).drop(columns= ['Unnamed: 0'])








        

















# get the restau data
@app.route('/resto' , methods = ['POST'])
def resto_filter():
    #  check if the request came with method POST
    if request.method == 'POST':
        query = request.get_json()
        asked_df = df[(df['category'].str.contains('|'.join(query['categories']), case=False)) & (df['name'].str.contains(query['query'] , case=False)) & (df['region'].str.contains('|'.join(query['regions']), case=False ))]
       
        # if len(asked_df) > 0 :
             #  return the response as json dictionnary
        return Response(asked_df.to_json(orient="records"), mimetype='application/json')
        # else:
        #      return 'sorry, but no POI correspond to your query'





# getting all unique region with its unique category to display them in table div
@app.route('/unique_reg_cat', methods= ['GET'])
def region_filter():
    #  check if the request cam with post method
    if request.method == 'GET':
        
        asked_df = df.groupby(['region'], as_index=False).agg(u_cat = ('category',np.unique),
                                    u_post_code = ('postal_code',np.unique),
                                    number_cat =('category','count'))
        
        
        return Response(asked_df.to_json(orient="records"), mimetype='application/json') 
     






# getting all departement in one region 
@app.route('/region_departement_filter',methods = ['POST'])
def departement_filter():
    # check if  ht request cam with post method 
    if request.method == 'POST':
        query = request.get_json()
        
        if len(query['asked_region']) == 0 :
            
            asked_df = df.groupby(['region'], as_index=False).agg(u_cat = ('category',np.unique),
                                    u_departement = ('departement',np.unique),
                                    number_cat =('category','count'))
        
        
            return Response(asked_df.to_json(orient="records" ),'region',  mimetype='application/json') 
        else:
            
            res = df[df['region'] == query['asked_region']]
            
            
            asked_df = res.groupby(['departement'], as_index = False).agg(n_poi = ('category','count'),
                                                    u_dep_cat = ('category',np.unique),
                                                    u_commune= ('commune', np.unique))
            
            return Response(asked_df.to_json(orient="records"), 'departement', mimetype='application/json') 








# getting all departement in one region 
@app.route('/departement_commune_filter',methods = ['POST'])
def commune_filter():
    # check if  ht request cam with post method 
    if request.method == 'POST':
        query = request.get_json()
        
        if len(query['asked_departement']) == 0 :
            
            asked_df = df.groupby(['departement'], as_index=False).agg(u_cat = ('category',np.unique),
                                    u_commune_dep = ('commune',np.unique),
                                    number_cat_in_depart =('category','count'))
        
        
            return Response(asked_df.to_json(orient="records" ), 'departement', mimetype='application/json') 
        else:
            
            res = df[df['departement'] == query['asked_departement']]
            
            
            asked_df = res.groupby(['commune'], as_index = False).agg(n_poi_in_commune = ('category','count'),
                                                    u_commune_cat = ('category',np.unique),
                                                    u_circonscription= ('postal_code', np.unique))
            return Response(asked_df.to_json(orient="records"), 'commune',  mimetype='application/json') 








# getting the groupement data for the graph output
@app.route('/graph_path', methods=['POST'])
def getDataForGraphFunc():
    #  check if it's a post method
    if request.method == 'POST':
        query = request.get_json()
        
        if len(query['graph_query']) == 0:
            asked_df = df.groupby(['category'], as_index=False).agg(category_number = ('category','count'))
            
            return Response(asked_df.to_json(orient="records"),  mimetype='application/json')
        
        elif len(query['graph_query']) > 0:
            
            res = df[df[query['graph_query']] == query['locality_name']]

            asked_df =  res.groupby(['category'], as_index=False).agg(category_number = ('category','count'))


            return Response(asked_df.to_json(orient="records"),  mimetype='application/json')



# getting the groupement data for the graph output
@app.route('/statistic_func', methods=['POST'])
def getDataForStatisticFunc():
    #  check if it's a post method
    if request.method == 'POST':
        query = request.get_json()
        
        # stats dict to return
        data = {}
        
        
        
        if len(query['graph_query']) == 0:
            
            #  get numbers of poi
            data['poi_number'] = str(df.shape[0])
            data['main_territory'] = 'France'
            #  get numbers of circonsription in france territory
            asked_df = df.groupby(['region'], as_index=False).agg(category_number = ('category','count')).sort_values(by=['category_number'], ascending=False)
            data['circonscription_number'] = str(asked_df.shape[0])
            # get top region with most categories & how many
            data['top_circon'] = asked_df.iloc[0]['region']
            data['cat_num_in_circ'] = str(asked_df.iloc[0]['category_number'])
            # get flop circonscription
            data['flop_circon'] = asked_df.iloc[-1]['region']
            
            # get top categpry in france how many
            asked_cat = df.groupby(['category'], as_index=False).agg(category_number = ('category','count')).sort_values(by=['category_number'], ascending=False)
            data['top_category'] = asked_cat.iloc[0]['category']
            data['num_for_top_cat'] = str(asked_cat.iloc[0]['category_number'])

            
            
            return jsonify(data)
        
        
        
        elif len(query['graph_query']) > 0:
            
            res = df[df[query['graph_query']] == query['locality_name']]
            
            # check if the user click on a region, departement or commune
            if query['graph_query'] == 'region':
                territory = 'departement'
            elif query['graph_query'] == 'departement':
                territory = 'commune'
            elif query['graph_query'] == 'commune':
                territory = 'postal_code'

            #  get numbers of poi
            data['poi_number'] = str(res.shape[0])
            data['main_territory'] = query['locality_name']
            
            #  get numbers of circonsription in region territory
            asked_df = res.groupby([territory], as_index=False).agg(category_number = ('category','count')).sort_values(by=['category_number'], ascending=False)
            data['circonscription_number'] = str(asked_df.shape[0])
            
            # get top region with most categories & how many
            data['top_circon'] = asked_df.iloc[0][territory]
            data['cat_num_in_circ'] = str(asked_df.iloc[0]['category_number'])
            # get flop circonscription
            data['flop_circon'] = asked_df.iloc[-1][territory]
            
            
            # get top categpry in territory & how many
            asked_cat = res.groupby(['category'], as_index=False).agg(category_number = ('category','count')).sort_values(by=['category_number'], ascending=False)
            data['top_category'] = asked_cat.iloc[0]['category']
            data['num_for_top_cat'] = str(asked_cat.iloc[0]['category_number'])




            return jsonify(data)















# train my ML model 

def clean(texte):

    texte = texte.lower()
    tokens = nltk.word_tokenize(texte)
    liste_tokens = [x for x in tokens if x.isalpha()]  
    stops = nltk.corpus.stopwords.words("french")
    liste_tokens_clean = [word for word in liste_tokens if not word in stops]
    all_words = ' '.join([word for word in liste_tokens_clean])
    all_words_v = vectorizer.transform([ all_words])
    return all_words_v


X= df['description_clean'].fillna('')
y= df['category']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.75, random_state = 32)
        
#Entraîne ton modèle sur X_train, puis crée une matrice de features X_train_CV
vectorizer = CountVectorizer()
vectorizer.fit(X_train)

X_train_CV_matrix = vectorizer.transform(X_train)
                

# call my model and predict
modelLogisticRegression = LogisticRegression().fit(X_train_CV_matrix,y_train)




# getting the groupement data for the graph output
@app.route('/mlpredictionpath', methods=['POST'])
def getMlPredictionFunc():
    #  check if it's a post method
    if request.method == 'POST':
        query = request.get_json()
             
        if len(query['ml_description']) == 0:
            res =  "please , enter first a description"
            
            return Response(res,  mimetype='application/json')
        
        elif len(query['ml_description']) > 0:
            cleaned_text = clean(query['ml_description'])
            res = modelLogisticRegression.predict(cleaned_text)[0]
            
            
            quantity = df[df['category']== res].shape[0]
            
            res_dict = {'category' : res, 'quantity': quantity}
            
            return jsonify(res_dict)










# hello world route
@app.route('/',methods=['GET'])
def getAllinfo():
    if request.method == 'GET':
        res= df.sample(2000)
        return Response(res.to_json(orient="records"), mimetype='application/json')
















if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
