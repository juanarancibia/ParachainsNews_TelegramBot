class News:
    def __init__(self,
                 _parachain_name: str,
                 _parachain_logo: str,
                 _date: str,
                 _title: str,
                 _type: str,
                 _url: str):
        self.parachain_name = _parachain_name
        self.parachain_logo = _parachain_logo
        self.date = _date
        self.title = _title
        self.type = _type
        self.url = _url

    def to_string(self) -> None:
        print()
        print(self.parachain_name)
        print(self.parachain_logo)
        print(self.date)
        print(self.type)
        print(self.title)
        print(self.url)
