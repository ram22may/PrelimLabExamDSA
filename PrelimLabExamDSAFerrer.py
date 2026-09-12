class Student:
    def __init__(self, student_id, student_name, course, year_level):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.year_level = year_level

        #self.student_id = student_id is just the same as $this->student_id = student_id in PHP OOP by sir Robi

    def display(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Course:", self.course)
        print("Year Level:", self.year_level)


class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.students = [None] * self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.students[i]

        self.students = new_array
        self.capacity = new_capacity

        print("Array capacity increased to", self.capacity)

    def add(self, student):
        if self.size == self.capacity:
            self.resize()

        self.students[self.size] = student
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            return None

        return self.students[index]

    def set(self, index, student):
        if index >= 0 and index < self.size:
            self.students[index] = student

    def search(self, student_id):
        for i in range(self.size):
            if self.students[i].student_id.lower() == student_id.lower():
                return i
                
        return -1

    def remove(self, student_id):
        index = self.search(student_id)

        if index == -1:
            return False

        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.students[i] = self.students[i + 1]

        self.students[self.size - 1] = None
        self.size -= 1

        return True

    def display(self):
        if self.size == 0:
            print("No students found.")
            return

        for i in range(self.size):
            print("\nStudent", i + 1)
            print("----------------------")
            self.students[i].display()

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity


def add_student(array):
    student_id = input("Enter Student ID: ")

    if array.search(student_id) != -1:
        print("studentId already exists.")
        return

    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    while True:
        try:
            year_level = int(input("Enter year level: "))

            if year_level <= 0:
                print("Year level must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a Valid Number.")

    student = Student(
        student_id,
        student_name,
        course,
        year_level
    )

    array.add(student)

    print("Student added successfully thank you.")


def search_student(array):
    student_id = input("Enter Student ID to search: ")

    index = array.search(student_id)

    if index == -1:
        print("Student not found.")
    else:
        print("\nStudent found:")
        array.get(index).display()


def update_student(array):
    student_id = input("Enter Student ID to update: ")

    index = array.search(student_id)

    if index == -1:
        print("Student not found.")
        return

    student = array.get(index)

    print("\nEnter new information:")

    student.student_name = input("Enter new Student Name: ")
    student.course = input("Enter new Course: ")

    while True:
        try:
            student.year_level = int(input("Enter new Year Level: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    print("Student updated successfully.")


def remove_student(array):
    student_id = input("Enter Student ID to remove: ")

    if array.remove(student_id):
        print("Student removed successfully.")
    else:
        print("Student not found.")


def display_array_info(array):
    print("Current number of students:", array.get_size())
    print("Current array capacity:", array.get_capacity())


def student_record_manager():
    students = DynamicArray()

    while True:
        print("\n================================")
        print("      STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            students.display()

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            remove_student(students)

        elif choice == "6":
            display_array_info(students)

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again and thank you!.")


student_record_manager()

class Song:
    def __init__(self, songId, songTitle, artist, duration):
        self.songId = songId
        self.songTitle = songTitle
        self.artist = artist
        self.duration = duration

    def display(self):
        print("Song ID:", self.songId)
        print("Song Title:", self.songTitle)
        print("Artist:", self.artist)
        print("Duration:", self.duration)


class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert_first(self, song):
        new_node = Node(song)

        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def insert_last(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self.size += 1

    def insert_at(self, song, position):
        if position < 1 or position > self.size + 1:
            return False

        if position == 1:
            self.insert_first(song)
            return True

        new_node = Node(song)

        current = self.head

        for i in range(1, position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.size += 1

        return True

    def search(self, songId):
        current = self.head

        while current is not None:

            if current.song.songId.lower() == songId.lower():
                return current.song

            current = current.next

        return None

    def remove(self, songId):
        if self.head is None:
            return False

        # If removing the first node
        if self.head.song.songId.lower() == songId.lower():
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head

        while current.next is not None:

            if current.next.song.songId.lower() == songId.lower():

                current.next = current.next.next
                self.size -= 1

                return True

            current = current.next

        return False

    def display(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        current = self.head
        number = 1

        while current is not None:
            print("\nSong", number)
            print("----------------------")
            current.song.display()

            current = current.next
            number += 1

        print("\nTotal songs:", self.size)

    def get_size(self):
        return self.size


def input_song():
    songId = input("Enter songId: ")
    songTitle = input("Enter songTitle: ")
    artist = input("Enter artist: ")
    duration = input("Enter duration: ")

    return Song(songId, songTitle, artist, duration)


def add_song_beginning(playlist):
    song = input_song()

    playlist.insert_first(song)

    print("Song added at the beginning.")


def add_song_end(playlist):
    song = input_song()

    playlist.insert_last(song)

    print("Song added at the end.")


def insert_song_position(playlist):
    while True:
        try:
            position = int(input("Enter position: "))
            break
        except ValueError:
            print("Please enter a valid number no words or random symbols please.")

    song = input_song()

    if playlist.insert_at(song, position):
        print("Song inserted successfully.")
    else:
        print("Invalid position.")


def search_song(playlist):
    songId = input("Enter songId to search: ")

    song = playlist.search(songId)

    if song is None:
        print("Song not found.")
    else:
        print("\nSong found:")
        song.display()


def remove_song(playlist):
    songId = input("Enter songId to remove: ")

    if playlist.remove(songId):
        print("Song removed successfully.")
    else:
        print("Song not found.")


def music_playlist_manager():
    playlist = LinkedList()

    while True:
        print("\n================================")
        print("       MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add song at the Beginning")
        print("2. Add Song at the End")
        print("3. Insert song at a Certain Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

        choice = input("Enter your choice please: ")

        if choice == "1":
            add_song_beginning(playlist)

        elif choice == "2":
            add_song_end(playlist)

        elif choice == "3":
            insert_song_position(playlist)

        elif choice == "4":
            playlist.display()

        elif choice == "5":
            search_song(playlist)

        elif choice == "6":
            remove_song(playlist)

        elif choice == "7":
            print("Playlist Size:", playlist.get_size())

        elif choice == "8":
            print("ExitingProgram...")
            break

        else:
            print("Not a Valid choice. Please try again.")


music_playlist_manager()
