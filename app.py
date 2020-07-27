# Imports
import os, flask, dash
from pathlib import Path
from random import randint
import dash_bootstrap_components as dbc

# Plots
from plotly.express import bar
import pandas as pd

# Import iPoster Object Class
from iposter.iposter import iPoster
import iposter.colors as colors

#*** Run Local Flag ***
RUN_LOCAL=False

# ******************Define Your Interactive Poster Here***************
# The following shows a sample interactive poster.
# Images for sections must be saved under the assets/ folder.
# You can import code from your own modules and construct the final dash
# interactive poster here.
def create_poster():

    # Instanitate an iPoster
    my_poster = iPoster(title="Transfer Learning with BERT Model and Search Algorithm", # Title of your poster
                        authors_dict={"Ajay Bati" : "Mission San Jose High School", # Authors in {student, mentors, PI} order
                                      "Rafael Zamora-Resendiz" : "Lawrence Berkeley National Laboratory",
                                      "Shirley Wang" : "Lawrence Berkeley National Laboratory",
                                      "Xinlian Liu" : "Hood College",
                                      "Silvia Crivelli" : "Lawrence Berkeley National Laboratory"},
                        logo = "msjhs.png", # Home institution logo
                        banner_color="#426cf5", # Color of banner header; colors has preset colors
                        text_color=colors.WHITE)

    # Add sections to first column then add new column
    my_poster.add_section(title="Research Question",
        text="How will BERT's word embeddings affect the fuzzy search performance for similar patients when compared to earlier methods, such as Regular Expressions?")
    my_poster.add_section(title="Abstract",color='#00cc63',
        text="The recent increase in data in the medical community, such as Electronic Health Records (EHR), allows us to access various features of patients over long periods of time.\
        Containing discharge summaries of patients diagnosed with one of the Diseases of Despair diagnoses - a set of diagnoses, including drug overdose, suicide, and alcohol-liver disease, relating to mental and behavioral issues for people who experience despair- \
        unstructured data may include a plethora of information missing in the labeled data. In this work, the trained BERT model's embedding representations is used\
        to conduct a fuzzy search on patients with similar conditions.")
    my_poster.add_section(title="Background Info",
        text="Suicide is a devastating global concern. Every 40 seconds, on average, one person takes their own life.\
        The backend of many medical software tools, regular expressions, does not capture many patients in a search. For example, UMLS is a widely-used software that combines biomedical information and services with EHR, but matching patients involves matching exact snippets of text, inefficient with language.\
        A more comprehensive search with deep learning methods captures the contextual representation of search query (through embeddings) and fuzzy searches for similar notes.")

    my_poster.add_section(title="MIMIC III - Unstructured Data",color='#00cc63',
        text="This work is based on the large, freely available dataset, MIMIC-III, containing patient visits to the Beth Isreal Deaconess Medical Center from June 2001 to October 2012; it provides us with patient visits, medical reports, ICD9-10 diagnoses, demographics, physician notes, and more.\
        Discharge summaries were compiled from patients with diagnoses in DoD. The BERT model was trained on sentences that were converted to vectorized representations by BERT's tokenizer, converting words into IDs. An attention mask is provided for the model to selectively pay attention to certain words.",
        img={"filename":"dataSS.png", "height":"4.35in", "width":"9in", "caption":"Example Input IDs and Attention Mask"})
    my_poster.next_column()

    # Add sections to second column then add new column
    my_poster.add_section(title="BERT",
        text="BERT (Bidirectional Encoder Representations from Transformers) makes use of transformers, an attention mechanism that is able to learn contextual relations between words using surrouding text.\
        It requires a '[MASK]' to inidicate what its predicting. After converting inputs into vectors, it passes through the classification layer and is multiplied to an embedding vocabulary matrix.\
        The encoder was trained so its word embeddings could be used to conduct our search.",
        img={"filename":"bert.png", "height":"6in", "width":"8in", "caption":"BERT architecture Photo Credit: Rani Horev"})
    # my_poster.add_section(title="Images",
    #     text="Save your image in the assets directory and set img to the filename.",
    #     img={"filename":"test.png", "height":"6in", "width":"8in", "caption":"Text for figure caption."})
    # my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.add_section(title="BERT Internal Representations",color='#00cc63', text="The plot on the left demonstrates how BERT represents the word 'lead' in two different contexts.\
    While there are two slightly different vectors for the 'lead' in BERT, Word2Vec categorizes this word, in two different sentences, the same way. Therefore, this model \
    can capture similar words in notes with similar context.",
    plot={"filename": 'embedeaaVisual.html',"height":"7in", "width":"12in", "caption": "2D Vector Representations of word embeddings"})

    my_poster.add_section(title="Acknowledgements",
        text="Thank you Destinee Morrow, Victor Adewopo, Rachel Thomas, Eric Vazquez Olivas, Praneetha Gouni, Masakatsu Watanabe, and everyone else for supporting this work. Thanks to the support of US Department of Energy, Lawrence Berkeley National Laboratory, the VA Million Veteran Program, and Dr. Leung's SHI program.")

    my_poster.next_column()

    # Add sections to third column then add new column
    my_poster.add_section(title="Cosine Distances",color='#00cc63', text="This heatmap represents an example of how BERT uses its internal representations for two different texts. After tokenizing each one, they are compared using a cosine distance, taking the harmonic mean, and setting a threshold for the fuzzy search. Dark patches are subwords that are closesly related.",plot={"filename": 'cos_dist.html',"height":"7in", "width":"12in", "caption": "Heatmap of Cosine Distances - dark Patches are closely related words."})
    my_poster.add_section(title="BERT",
        text="Down below is an overarching representation of the pipeline while querying UMLS. The search query is passed to the metathesaurus to search for similar concepts with a fuzzy search (using the boolean function).\
        It then returns a lexicon with these concepts, which will be used again to query notes to capture similar patients.",
        img={"filename":"umls.png", "height":"4in", "width":"8in", "caption":"BERT architecture"})
    my_poster.add_section(title="Conclusion",color='#00cc63',
        text="The BERT model offers a significant advantage over RegEx (and Word2Vec) as it captures UMLS concepts related to a given text. Instead of specifically matching exact text, the fuzzy search seeks relationships between words and phrases. \
        For example, if querying 'vomitting and nauseous', the search provides\
        concepts relating to alcohol, aggression, lung disease, liver problems, and more. Now, previously 'hidden' patients are captured and can be monitored (if necessary) \
        Similar diagnoses, conditions, histories, and medications can be searched to capture similar patients; in case of an emergency, dangerous situations can be predicted and preemptively dealt with.")
    my_poster.next_column()

    return my_poster.compile()

# **********************************************************************

# Dash App Configuration
if RUN_LOCAL:
    app = dash.Dash(__name__,
                    assets_folder= str(Path(__file__).parent.absolute())+"/assets",
                    assets_url_path='/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    suppress_callback_exceptions=True)
else:
    server = flask.Flask(__name__)
    server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
    app = dash.Dash(__name__,
                    server=server,
                    assets_folder= str(Path(__file__).parent.absolute())+"/assets",
                    assets_url_path='/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    suppress_callback_exceptions=True)
app.layout = create_poster()

# Main Function
if __name__ == "__main__":
    if RUN_LOCAL:
        app.run_server(debug=False, host="0.0.0.0", port="8888")
    else:
        app.server.run(debug=True, threaded=True)
