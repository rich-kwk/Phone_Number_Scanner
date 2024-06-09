from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['scam_numbers']
collection = db['numbers']

class ScamNumberCheckerApp(App):
    def build(self):
        # Create the main layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Button to create the collection and insert sample data
        self.create_button = Button(text="Create Collection")
        self.create_button.bind(on_press=self.create_collection)
        self.layout.add_widget(self.create_button)
        
        # Label and TextInput for the phone number
        self.label = Label(text="Enter Phone Number (xxx-xxx-xxxx):")
        self.layout.add_widget(self.label)
        
        self.entry = TextInput(multiline=False)
        self.layout.add_widget(self.entry)
        
        # Button to check the number
        self.check_button = Button(text="Check Number")
        self.check_button.bind(on_press=self.check_number)
        self.layout.add_widget(self.check_button)
        
        return self.layout

    def create_collection(self, instance):
        # Insert sample data into the collection
        sample_data = [
            {'number': '123-456-7890'},
            {'number': '987-654-3210'},
            {'number': '555-123-4567'}
        ]
        collection.insert_many(sample_data)
        self.show_popup("Collection Created", "Sample data inserted into the collection.")

    def check_number(self, instance):
        # Get the entered phone number
        phone_number = self.entry.text

        # Check if the phone number is in the database
        result = collection.find_one({'number': phone_number})

        # Display the result in a popup
        if result:
            self.show_popup("Scam Alert", "This phone number is a scam!")
        else:
            self.show_popup("Not a Scam", "This phone number is not on the scam list.")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_label = Label(text=message)
        popup_button = Button(text="OK", size_hint_y=None, height=40)
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    ScamNumberCheckerApp().run()
