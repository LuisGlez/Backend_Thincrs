from dotenv import load_dotenv
from app import create_app # pylint: disable=import-self

load_dotenv()
app = create_app()