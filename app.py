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
                                      "Xiange Wang" : "Lawrence Berkeley National Laboratory",
                                      "Xinlian Liu" : "Lawrence Berkeley National Laboratory",
                                      "Silvia Crivelli" : "Lawrence Berkeley National Laboratory"},
                        logo = "msjhs.png", # Home institution logo
                        banner_color="#426cf5", # Color of banner header; colors has preset colors
                        text_color=colors.WHITE)

    # Add sections to first column then add new column
    my_poster.add_section(title="Abstract",color='#00cc63',
        text="The recent increase in data in the medical community, such as Electronic Health Records (EHR), allows us to access health information of patients over long periods of time. In this study we focus on Diseases of Despair (DoD) diagnoses - a set of diagnoses, including drug overdose, suicide, and alcohol-liver disease, relating to mental and behavioral issues for people who experience despair. EHR contains structured (labeled) and unstructured (free text) data and studies usually focus on the former. However, information contained in the discharge summaries of patients diagnosed with DoD includes a plethora of information missing in the labeled data. In this work, the trained BERT (Devlin et al., 2018) model's embedding representations are used to conduct a fuzzy search on patients with similar conditions.")
    my_poster.add_section(title="Research Question",
        text="How will BERT's word embeddings affect the fuzzy search performance for similar patients when compared to earlier methods, such as Regular Expressions?")
    my_poster.add_section(title="Background Info",
        text="Suicide is a devastating global concern. Every 40 seconds, on average, one person takes their own life. The backend of many medical software tools, regular expressions, does not capture many patients in a search. For example, UMLS (Unified Medical Language System) (Bodenreider, 2004) is a widely-used software that combines biomedical information and services with EHR, but matching exact snippets of text will not capture synonyms and related conditions and diagnoses. A more comprehensive search with deep learning methods provides greater quantity and quality of results.")

    my_poster.add_section(title="MIMIC III - Unstructured Data",color='#00cc63',
        text="This work is based on the large, freely available dataset, MIMIC-III (Johnson, A., Pollard, T., Shen, L. et al., 2016), containing a decade worth of patient visits to the Beth Israel Deaconess Hospital; it provides us with medical reports, ICD9-10 diagnoses, demographics, and more. \
Discharge summaries were compiled from patients with ICD (International Classification of Diseases) codes in DoD.",
        img={"filename":"dataSS.png", "height":"4.35in", "width":"9in", "caption":"A sentence is separated from a note. The BERT tokenizer converts it to vectorized representation, with a length of 128 (97% of sentences have length 128). An attention mask is provided, so the model pays attention to 1 (real words) and not 0 (padding)."})
    my_poster.next_column()

    # Add sections to second column then add new column
    my_poster.add_section(title="BERT",
        text="BERT (Bidirectional Encoder Representations from Transformers) makes use of transformers, an attention mechanism that is able to learn contextual relations between words using surrouding text.\
        The encoder was trained so its word embeddings could be used to conduct our search.",
        img={"filename":"bert.png", "height":"6in", "width":"8in", "caption":"The model requires a '[MASK]' in the input to inidicate what it is predicting. After converting inputs into vectors, it passes through the classification layer and is multiplied to an embedding vocabulary matrix, which provides the top-k probabilities for the guessed '[MASK]'.\
        Photo Credit: Rani Horev"})
    # my_poster.add_section(title="Images",
    #     text="Save your image in the assets directory and set img to the filename.",
    #     img={"filename":"test.png", "height":"6in", "width":"8in", "caption":"Text for figure caption."})
    # my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.add_section(title="BERT Internal Representations",color='#00cc63', text="The BERT model learns contextual relationships of words, a characteristic absent in Word2Vec. Based on context, BERT will\
    capture similar concepts and patients during the fuzzy search.",
    plot={"filename": 'embedeaaVisual.html',"height":"7in", "width":"12in", "caption": "The plot on the left demonstrates how BERT represents the word 'lead' differently in three contexts, two sentences as verbs and one as a noun.\
    However, in two sentences where lead is a verb and noun, respectively, Word2Vec categorizes this word the same way, shown by one 'lead' coordinate."})

    my_poster.add_section(title="Acknowledgements",
        text="Thank you Destinee Morrow, Victor Adewopo, Rachel Thomas, Eric Vazquez Olivas, Praneetha Gouni, Masakatsu Watanabe, and everyone in team. Thanks to the support of US Department of Energy, Lawrence Berkeley Laboratory, the VA Million Veteran Program, and Dr. Leung's SHI program.")

    my_poster.next_column()

    # Add sections to third column then add new column
    my_poster.add_section(title="Cosine Distances",color='#00cc63', text="This heatmap is a representation of BERT using its internal representations for two different texts. After passing each text through the model, they are compared using a cosine distance, taking the harmonic mean for each comparison, and setting a threshold for the fuzzy search.",plot={"filename": 'cos_dist.html',"height":"7in", "width":"10in", "caption": "The darker \
    patches are subwords that have a low cosine distance and high similarity while lighter ones represent less correlated words. There are 128x128 comparisons and each are used to compute the harmonic mean for the threshold (not all text comparisons are shown)."})
    my_poster.add_section(title="BERT",
        text="The BERT model uses its word embeddings to build a comprehensive lexicon from UMLS. This lexicon is queried again to match against similar notes.",
        img={"filename":"umls.png", "height":"4in", "width":"8in", "caption":"This is an overarching representation of the pipeline while querying UMLS. The search query is passed to the UMLS metathesaurus to search for similar concepts with a fuzzy search (using the boolean function).\
        It then returns a lexicon with these concepts, which will be used again to query notes to capture similar patients."})
    my_poster.add_section(title="Conclusion",color='#00cc63',
        text="The BERT model offers a significant advantage over RegEx (and Word2Vec) as it captures UMLS concepts related to a given text. Instead of specifically matching exact text, the fuzzy search seeks relationships between words and phrases. \
        For example, if querying 'vomitting and nauseous', the search provides\
        concepts relating to alcohol, aggression, lung disease, liver problems, and more. \
        Similar diagnoses, conditions, histories, and medications can be searched to capture similar, previously 'unnoticed', patients; now, dangerous situations can be predicted and preemptively dealt with.")
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
