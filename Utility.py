def asp(word,  desired_length ):

  # Überprüfe die Länge des Worts
  current_length = len(word)

  # Wenn die Länge des Worts bereits die gewünschte Länge erreicht hat, gib das Wort unverändert zurück
  if current_length >= desired_length:
    return word

  # Berechne die Anzahl der fehlenden Leerzeichen
  spaces_needed = desired_length - current_length

  # Füge die fehlenden Leerzeichen hinzu
  padded_word = word + " " * spaces_needed

  return padded_word


def asp2(word):
  desired_length = 4
  # Überprüfe die Länge des Worts
  current_length = len(word)

  # Wenn die Länge des Worts bereits die gewünschte Länge erreicht hat, gib das Wort unverändert zurück
  if current_length >= desired_length:
    return word

  # Berechne die Anzahl der fehlenden Leerzeichen
  spaces_needed = desired_length - current_length

  # Füge die fehlenden Leerzeichen hinzu
  padded_word = word + " " * spaces_needed

  return padded_word
