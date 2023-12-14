"""
    description of lab will go here
"""


def lab_load_csv():
    from langchain.document_loaders.csv_loader import CSVLoader

    loader = CSVLoader(file_path="resources/movies.csv")

    data = loader.load()

    print(len(data))
        
def lab_load_pdf():
    """
        this function requires the pypdf package via pip
    """
    from langchain.document_loaders import PyPDFLoader
    loader = PyPDFLoader("resources/The_Republic.pdf")
    pages = loader.load_and_split()
    print(len(pages))
    
def lab_load_dir():
    """
        Make sure to specify the loader_cls parameter, otherwise the app will hang
    """
    from langchain.document_loaders import DirectoryLoader, TextLoader
    loader = DirectoryLoader("resources/genres_organized", show_progress=True, loader_cls=TextLoader)
    docs = loader.load()
    print(len(docs))
    
def lab_load_md():
    """
        Unstructured currently does not work when auto-detecting file types without admin privileges. The
        first time I ran it with admin privileges, it downloaded NLTK data seperate from the nltk package 
        downloaded from pip. Even with this data admin mode was still needed.
    """
    from langchain.document_loaders import UnstructuredMarkdownLoader
    loader = UnstructuredMarkdownLoader("resources/genres.md", mode="elements") # this breaks the document into individual chunks (titles and "narrative text")can do single instead for one chunk
    data = loader.load()
    for d in data:
        print(d)
