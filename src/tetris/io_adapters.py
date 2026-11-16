class FileReader:
    def read(self, path: str) -> str:
        with open(path, encoding="utf-8") as f:
            return f.read()
