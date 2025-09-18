# This is not a fully pythonic way of implementing the Iterator Pattern.
# To make pythonic
# ✅ Removed Iterator/Iterable abstract classes → Python doesn’t need them.
# ✅ Used __iter__ + yield (generators) → clean and memory-efficient.
# ✅ Now you can directly use list(obj) or for x in obj: without a separate iterator class.


from collections import deque


# Iterator & Iterable Hierarchy
class Iterator:
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError


class Iterable:
    def get_iterator(self) -> Iterator:
        raise NotImplementedError


# Linked List
class LinkedList(Iterable):
    def __init__(self, value):
        self.data = value
        self.next = None

    def get_iterator(self):
        return LinkedListIterator(self)


# Binary Tree
class BinaryTree(Iterable):
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def get_iterator(self):
        return BinaryTreeInorderIterator(self)


# Song and Playlist
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist(Iterable):
    def __init__(self):
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def get_iterator(self):
        return PlaylistIterator(self.songs)


# Iterators
class LinkedListIterator(Iterator):
    def __init__(self, head: LinkedList):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        val = self.current.data
        self.current = self.current.next
        return val


class BinaryTreeInorderIterator(Iterator):
    def __init__(self, root: BinaryTree):
        self.stack = deque()
        self._push_lefts(root)

    def _push_lefts(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        val = node.data
        if node.right:
            self._push_lefts(node.right)
        return val


class PlaylistIterator(Iterator):
    def __init__(self, songs):
        self.songs = songs
        self.index = 0

    def __next__(self):
        if self.index >= len(self.songs):
            raise StopIteration
        song = self.songs[self.index]
        self.index += 1
        return song


# -------------------------
# Main (usage)
# -------------------------
if __name__ == "__main__":
    # LinkedList: 1 → 2 → 3
    list_head = LinkedList(1)
    list_head.next = LinkedList(2)
    list_head.next.next = LinkedList(3)

    print("LinkedList contents:", end=" ")
    for val in list_head.get_iterator():
        print(val, end=" ")
    print()

    # BinaryTree:
    #    2
    #   / \
    #  1   3
    root = BinaryTree(2)
    root.left = BinaryTree(1)
    root.right = BinaryTree(3)

    print("BinaryTree inorder:", end=" ")
    for val in root.get_iterator():
        print(val, end=" ")
    print()

    # Playlist
    playlist = Playlist()
    playlist.add_song(Song("Admirin You", "Karan Aujla"))
    playlist.add_song(Song("Husn", "Anuv Jain"))

    print("Playlist songs:")
    for song in playlist.get_iterator():
        print(f"  {song.title} by {song.artist}")
