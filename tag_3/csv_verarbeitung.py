""" 
CSV-Datei einlesen, bereinigen und neu schreiben
"""
import os 
import csv 
from pathlib import Path


filepath = Path(__file__).parent / "messdaten"
outfile_name = "alle_messergebnisse"

def get_files(filepath: Path):
    out_files = []
    for root, dirs, files in os.walk(filepath, topdown=False):
        for name in files:
            if outfile_name not in name:
                out_files.append(os.path.join(root, name))
    return out_files


def format_number(value: str):
    value = value.lower()
    try:
        return float(value.replace("mm", "").replace(",", "."))
    except ValueError:
        return ""


def get_teilnummer(filename: str):
    """Generiere aus Dateiname die Teilnummer."""
    teilnummer = filename.split("\\").pop().replace(".csv", "")
    return teilnummer


def write_data(filename: str, header: list, data: list):
    """Schreibe Header und Daten in eine CSV-Datei."""
    with open(filepath / filename, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(header)
        writer.writerows(data)


def read_file(filename, filepath, sep=";"):
    """CSV-Datei einlesen und von mm bereinigen."""

    output = []

    with open(filepath / filename, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=sep)
        header = next(reader)
        for row in reader:
            value = format_number(row[1])
            output.append(
                [row[0], value]
            )

        return output


def read_data(filenames):
    """Liste von Dateien einlesen und bereinigen.
    
    Returns:
        Tuple: Header, Liste von Listen
    """
    data_liste = []
    for index, filename in enumerate(filenames):
        teilnummer = get_teilnummer(filename)
        result = read_file(filename, filepath)
        # Transponieren einer Matrix
        resultT = [list(x) for x in zip(*result)]
        resultT[1].insert(0, teilnummer)
        data_liste.append(resultT[1])

        if index == 0:
            header = resultT[0]
            header.insert(0, "Teilnummer")
    return header, data_liste
    

header, data_list = read_data(get_files(filepath))
write_data(outfile_name + ".csv", header, data_list)

