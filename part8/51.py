import firebase_admin
from firebase_admin import credentials, db
import sys
import datetime
import json

key = "<path to json file>"
database_url = "https://<your firebase project name>.firebaseio.com"


cred = credentials.Certificate(key)
myapp = firebase_admin.initialize_app(cred, {'databaseURL' : database_url})

if len(sys.argv) <= 1:
    sys.argv.append('')

def write_note(content):
    root = db.reference("/")
    new_note = root.child('users').push({
        'date_and_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'content': content
    })

def read_note():
    notes = db.reference('users').get()
    note_list = []
    for note in notes:
        note_list.append("{} -- {}".format(notes[note]['date_and_time'], notes[note]['content']))
    note_list.sort()
    for note in note_list:
        print(note)

def check_valid_command(command):
    command_list = ['write_note', 'read_note']
    message = "\n'{}' is not a valid command. Valid commands are:\n'write_note'\n'read_note'"
    if command in command_list:
        return command
    else:
        print(message.format(command))

def do_command(command, content):
    if command == 'write_note':
        write_note(content)
    elif command == 'read_note':
        read_note()

def main():
    command = sys.argv[1]
    content_list = sys.argv[2:]
    content = ' '.join(content_list)
    check_valid_command(command)
    do_command(command, content)

main()
