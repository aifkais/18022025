from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from main import *

class ChatbotApp(App):
    def build(self):
        # Hauptlayout
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        # Scrollbereich für die Nachrichtenanzeige
        self.scroll_view = ScrollView(size_hint=(1, 0.8))

        # Label für die Chat-Nachrichten (dynamische Breite)
        self.chat_output = Label(
            size_hint_y=None, 
            text_size=(self.layout.width, None),  # Breite an Layout anpassen
            valign='top', 
            halign='left',
        )
        self.chat_output.bind(texture_size=self.update_chat_size)
        self.scroll_view.add_widget(self.chat_output)
        self.layout.add_widget(self.scroll_view)

        # Eingabebereich und Buttons
        input_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)

        # Textfeld für die Benutzereingabe
        self.input_field = TextInput(hint_text="Geben Sie einen Befehl ein...", multiline=False)
        input_layout.add_widget(self.input_field)

        # Button zum Senden
        send_button = Button(text="Senden", size_hint=(0.3, 1))
        send_button.bind(on_press=self.handle_command)
        input_layout.add_widget(send_button)

        # Button zum Löschen
        clear_button = Button(text="Löschen", size_hint=(0.3, 1))
        clear_button.bind(on_press=self.clear_chat)
        input_layout.add_widget(clear_button)

        self.layout.add_widget(input_layout)

        return self.layout

    def update_chat_size(self, *args):
        """Aktualisiert die Größe des Labels, um die Breite des Layouts zu verwenden."""
        self.chat_output.text_size = (self.scroll_view.width, None)  # Breite anpassen
        self.chat_output.size = self.chat_output.texture_size  # Texturgröße übernehmen

    def handle_command(self, instance):
        # Reagiere auf Befehle
        nachrichten = []
        
        command = self.input_field.text.strip().lower()
        if command == "start":
            return
            

        elif command == "help":
            response = "Verfügbare Befehle: hallo, zeit, hilfe"
        elif command == "reset":
            response = "Verfügbare Befehle: hallo, zeit, hilfe"
        else:
            response = "Unbekannter Befehl. Versuchen Sie 'hilfe', um die verfügbaren Befehle zu sehen."

        #change1
        #startgame
        #resetgame

        # Nachricht hinzufügen
        self.chat_output.text += f"> Eingabe: {command}\n"
        for message in nachrichten:
            self.chat_output.text += f"Bot: {message}\n"
        self.chat_output.text += "\n"
        # Eingabefeld leeren
        self.input_field.text = ""

        # Automatisches Scrollen nach unten
        self.scroll_view.scroll_y = 0

    def clear_chat(self, instance):
        # Nachrichtenanzeige löschen
        self.chat_output.text = ""


if __name__ == '__main__':
    ChatbotApp().run()
