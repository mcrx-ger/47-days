# Von der URL (Internetadresse) zur Website: Wie das Internet funktioniert

## Akteure

Die Akteure im Internet kann vereinfacht in Clients und Server aufgeteilt werden. Clients sind Endgeräte, die Anfragen an Server senden. Die Server nehmen diese Anfragen entgegen bearbeiten diese (bspw. durch bereitstellen einer Website).

## Mit Servern verbinden

Wenn man sich mit Servern verbinden möchte (bspw. beim Aufrufen einer Website), kann dies über einen Browser geschehen. Für den Verbindungsaufbau wird grundsätzlich die IP-Adresse des Servers benötigt. Dies ist das computernahe Äquivalent zur Domain, die für Menschen lesbarer ist.

### DNS-Tracing (Domain Name System)

Nach Eingabe einer URL muss der Browser die dazugehörige IP-Adresse des Servers herausfinden. Die kann über verschiedene Wege geschehen:
 
1. Browser-Cache: Für eine kurze Zeit werden die IP-Adressen kürzlich aufgerufener Websites gespeichert
2. OS-Cahce: Auch das Betriebssystem des Computers speichert IP-Adressen temporär
3. Resolver-Cache beim ISP (*Internet Service Provider*): Die nächste Instanz in der Hierarchie ist der Internetanbieter. Auch er könnte sie im Cache gespeichert haben.
4. Root-Server: Ist die Adresse auch beim Internetanbieter nicht gespeichert, startet er Abfragen bei anderen Servern, beginnend mit dem Root-Server, bis die IP-Adresse ermittelt wird.

### TCP-Three-Way-Handshake und TLS-Handshake

Sobald die IP-Adresse gefunden wurde, kann der Verbindungsaufbau erfolgen. Die Kommunikation zwischen Computern wird über sog. Protokolle geregelt - dazu gehören TCP (*Transmission Control Protocol*), TLS (*Transport Layer Security*) und HTTPS (*Hypertext Transfer Protocol Secure*)

Ablauf des TCP-Handshakes (Verbindungsaufbau):

1. SYN: Der Client fragt, ob Verbindungen verfügbar sind
2. SYN-ACK: Der Server sendet eine Synchronisierungsbestätigung, wenn er die Verbindung annehmen kann
3. ACK: Der Client bestätigt den Empfang des SYN-ACK-Pakets

Ablauf des TLS-Handshake (Authentifizierung und Verschlüsselung) (Version 1.2)

1. *Client hello* Nachricht: Enthält die TLS-Versionen und Verschlüsselungsmechanismen (*Cipher Suites*), die der Client unterstützt und einen Zufallswert (dient zur Eindeutigkeit der Session)
2. *Server hello* Nachricht: Enthält die ausgewählte TLS-Version und Cipher Suite und einen Zufallswert
3. Der Server sendet das Zertifikat einer vertrauten Certificate-Authority und belegt damit, dass sein Public-Key zur Domain gehört.
4. Um sicherzustellen, dass der Server auch der Besitzer des Public Keys des Servers ist und um den geheimen gemeinsamen Schlüssel auszutauschen, sendet der Client ein Pre-Master-Secret (Daten, die mit dem Public Key des Servers verschlüsselt sind - um diese zu entschlüsseln wird der Private Key benötigt). 
> In Version 1.3 wird an der Stelle *Diffie-Hellman key exchange* zum Ermitteln des Session keys verwendet. Außerdem ist der komplette Handshake auf einen Rundgang reduziert
5. Aus der gesamten Session samt Zufallswerten und Pre-Master-Secret wird jetzt der Session-Key generiert, der zur Verschlüsselung von Nachrichten dient
6. Client und Server schicken jeweils eine *Finished* Nachricht, die mit dem Session Key verschlüsselt ist, um sicherzustellen, dass beide auf denselben Key gekommen sind
7. Nun können Daten (bspw. Webseiten) verschlüsselt übertragen werden.

### HTTP-Request und Response

Nachdem die Verbindung über TLS aufgebaut wurde, kann der Client einen HTTPS-Request an den Server schicken, um Daten (Website) zu erhalten.

1. Ein HTTP-Request (Anfrage vom Client) ist folgendermaßen aufgebaut: Method (z.B. GET um Text zu laden, POST um Eingabe zu schicken) Path, Protocol Version, Headers (Host, Language), Body
2. Der Response (Antwort vom Server) ist ähnlich aufgebaut, enthält jedoch Statuscode (200 / 403) und Statusmessage (OK / forbidden) und einen *data block* (bspw. mit HTML / CS / javascript / bilder / audio)

> Auch Cookies werden mit HTTP-Requests und Responses. Cookies sind Daten, die zwischen Server und Browser ausgetauscht werden und die der Browser verändern/speichern kann. Sie ermöglichen Web-Apps, Daten zum Nutzer zu speichern, zum Beispiel Daten bzgl. Session-Status, Personalisierung und Nutzerverhalten. 
