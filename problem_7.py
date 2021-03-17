class RouteTrieNode:
    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler

    def insert(self, path):
        self.children[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        node = self.root
        for sub_path in path:
            if sub_path not in node.children:
                node.insert(sub_path)
            node = node.children[sub_path]
        node.handler = handler

    def find(self, path):
        if len(path) == 1 and path[0] == '':
            return self.root.handler

        node = self.root
        for sub_path in path:
            if sub_path not in node.children:
                return None
            node = node.children[sub_path]

        return node.handler

class Router:
    def __init__(self, root_handler, not_found_handler):
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        self.trie = RouteTrie(self.root_handler)

    def add_handler(self, path, handler):
        split_path = Router.split_path(path)
        self.trie.insert(split_path, handler)

    def lookup(self, path):
        split_path = Router.split_path(path)
        handler = self.trie.find(split_path)
        return handler if handler else self.not_found_handler

    @staticmethod
    def split_path(path):
        splitted = path.split('/')
        has_trailing_slash = splitted[-1] == ''
        if has_trailing_slash:
            splitted.pop()
        return splitted


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

# TEST CASE 1 -> routing to root
route = "/"
print('-----------\nLooking for route: ' + route)
handler = router.lookup(route)
print('handler_found: ' + handler + '\n') # should print 'root handler'
assert(handler == 'root handler')

# TEST CASE 2 -> routing to non-leaf route
route = "/home"
print('-----------\nLooking for route: ' + route)
handler = router.lookup(route)
print('handler_found: ' + handler + '\n') # should print 'not found handler'
assert(handler == 'not found handler')

# TEST CASE 3 -> routing to leaf route
route = "/home/about"
print('-----------\nLooking for route: ' + route)
handler = router.lookup(route)
print('handler_found: ' + handler + '\n')# should print 'about handler'
assert(handler == 'about handler')

# TEST CASE 4 -> routing to leaf route with trailing slashes
route = "/home/about/"
print('-----------\nLooking for route: ' + route)
handler = router.lookup(route)
print('handler_found: ' + handler + '\n')# should print 'about handler'
assert(handler == 'about handler')

# TEST CASE 5 -> routing to missing route
route = "/home/about/me"
print('-----------\nLooking for route: ' + route)
handler = router.lookup(route)
print('handler_found: ' + handler + '\n') # should print 'not found handler'
assert(handler == 'not found handler')

# TEST CASE 6 -> routing to missing route
route = "/login"
print('-----------\nLooking for route: ' + route)
handler = router.lookup(route)
print('handler_found: ' + handler + '\n') # should print 'not found handler'
assert(handler == 'not found handler')

# TEST CASE 7 -> route to root with no slashes
route = ""
print('-----------\nLooking for route: ' + route)
handler = router.lookup(route)
print('handler_found: ' + handler + '\n') # should print 'root handler'
assert(handler == 'root handler')
