from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(source)

    def create_dir(self, path):
        directory = self.dest / relative_to(self.source)
        directory.mkdir(parents = True, exist_ok = True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rgob("*"):
            if path is_dir():
                self.create_dir(path)
