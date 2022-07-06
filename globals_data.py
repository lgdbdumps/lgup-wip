browser=None
list_of_books = []
class book_data:
    def __init__(self, filename, size):
        self.md5=None
        self.filename=filename
        self.isbn=None
        self.size=size
        self.is_duplicate=None
        self.is_well_formed=None
        self.is_size_ok=None
        self.is_ext_ok=None
        self.is_file_header_ok=None
        self.is_clean=None

