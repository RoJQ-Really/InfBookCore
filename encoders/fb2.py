from typing import TypedDict

# 1.1 Description
class TitleInfo(TypedDict): # TODO
    genre: list[str]
    author: list[dict]
    book_title: str
    annotation: dict| None
    keywords: dict|None
    data: dict|None
    coverpage: dict|None
    lang: str
    src_lang: str
    translator: list[dict] | None
    sequence: list[dict] | None


class DocumentInfo(TypedDict): # TODO
    author: list[dict] 
    program_used: str|None
    data: dict|None
    src_url: str| None
    src_ocr: str| None
    id: str
    version: str
    history: dict| None
    book_name: str
    publisher: list[str]|None
    city: list[str]|None
    year: str

class Description(TypedDict): # TODO
    title_info: TitleInfo
    document_info: DocumentInfo
    srt_title_info: TitleInfo | None
    publish_info: dict | None 
    custom_info: list[dict] 

class Body(TypedDict):
    pass

class Binary(TypedDict):
    pass

class FictionBook2(TypedDict):
    description: Description
    body: list[Body]
    binary: list[Binary]