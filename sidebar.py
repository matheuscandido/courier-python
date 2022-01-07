from gi.repository import Gtk, GObject
from collection_manager import CollectionManager

import constants

TYPE = 0
METHOD = 1
NAME = 2

JSON_REQUESTS = (
    ("GET", "Get Item"),
    ("POST", "Create Item"),
    ("PUT", "Change Item"),
    ("PATCH", "Amend Item"),
    ("DELETE", "Delete Item")
)

TREE_COLLECTION = 0
TREE_REQUEST = 1

class Sidebar(Gtk.ScrolledWindow):

    def __init__(self, collection_manager: CollectionManager):
        super().__init__()
        self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

        self.collection_manager = collection_manager
        self.collection_manager.load_all_collections()

        self.tree_view = Gtk.TreeView.new()
        self.setup_tree_view()

        # Type, Method, Method
        self.model_store = Gtk.TreeStore.new((
            GObject.TYPE_BOOLEAN, 
            GObject.TYPE_STRING, 
            GObject.TYPE_STRING
        ))

        for collection in self.collection_manager.colletions:
            coll_iter = self.model_store.append(None)
            self.model_store.set(coll_iter, TYPE, TREE_COLLECTION, METHOD, "", NAME, collection["info"]["name"])

            for item in collection["item"]:
                item_iter = self.model_store.append(coll_iter)
                self.model_store.set(item_iter, TYPE, TREE_REQUEST, METHOD, item["request"]["method"], NAME, item["name"])
        
        self.tree_view.set_model(self.model_store)

        self.add(self.tree_view)
    
    def setup_tree_view(self):
        renderer = Gtk.CellRendererText.new()
        column = Gtk.TreeViewColumn("Method", renderer, text=METHOD)
        self.tree_view.append_column(column)

        renderer = Gtk.CellRendererText.new()
        column = Gtk.TreeViewColumn("Name", renderer, text=NAME)
        self.tree_view.append_column(column)
