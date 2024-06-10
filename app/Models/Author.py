class Author:
    authors = []


def create_author(self, name, email):
    """Creates a new author"""
    author = {}
    author["id"] = len(self.authors) + 1
    author["name"] = name
    author["email"] = email

    # check if email already exists
    result = [author for author in self.authors if author["email"] == email]
    if result:
        return "Email already exists"
    else:
        # Populate the authors list with the new author
        self.authors.append(author)
        return author


def update_author(self, id, data):
    """Update author details"""
    author = self.find_author(id)
    if author:
        author.update(
            {
                "name": data["name"],
                "email": data["email"],
            }
        )
        return author
    else:
        return None


def delete_author(self, id):
    """Delete author"""
    new_authors = []
    for author in self.authors:
        if author["id"] != id:
            new_authors.append(author)
            self.authors = new_authors
    return self.authors


def find_author(self, id):
    """Get author with the id from store"""
    author = [author for author in self.authors if author["id"] == id]
    if author:
        return author
    else:
        return None


def get_authors(self):
    """Return all registered authors"""
    return self.authors
