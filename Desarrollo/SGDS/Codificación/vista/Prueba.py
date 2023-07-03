# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Define the file path for the module 
db_path = os.path.join(current_dir,"..","modelo","Credencial.py")
# Load  the module from the file path
spec = importlib.util.spec_from_file_location("Credencial",db_path)
Credencial = importlib.util.spec_from_spec(spec)
spec.loader.exec_module(Credencial)
CredencialClass = getattr(Credencial, "Credencial")

