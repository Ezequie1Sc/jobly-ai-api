from io import BytesIO

from pypdf import PdfReader


def extract_text_from_pdf(file_content: bytes) -> str:
    """
    Extrae el texto de todas las páginas de un PDF.
    """

    pdf_stream = BytesIO(file_content)
    reader = PdfReader(pdf_stream)

    pages_text: list[str] = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages_text.append(text)

    return "\n".join(pages_text).strip()