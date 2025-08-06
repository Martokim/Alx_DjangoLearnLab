## Task 1: Custom Views and Generic Views in Django REST Framework

### Overview
This task implements CRUD (Create, Read, Update, Delete) operations on the `Book` model using Django REST Framework's **generic views** and permissions to control API access.

---

### Views Implemented
1. **BookListView (ListAPIView)**  
   - Endpoint: `/api/books/`  
   - Function: Lists all books.  
   - Permissions: Accessible to all users (read-only for unauthenticated users).  

2. **BookDetailView (RetrieveAPIView)**  
   - Endpoint: `/api/books/<id>/`  
   - Function: Retrieve a single book by its ID.  
   - Permissions: Read-only for unauthenticated users.  

3. **BookCreateView (CreateAPIView)**  
   - Endpoint: `/api/books/create/`  
   - Function: Create a new book entry.  
   - Permissions: Only authenticated users can create.  

4. **BookUpdateView (UpdateAPIView)**  
   - Endpoint: `/api/books/update/<id>/`  
   - Function: Update book details.  
   - Permissions: Only authenticated users can update.  

5. **BookDeleteView (DestroyAPIView)**  
   - Endpoint: `/api/books/delete/<id>/`  
   - Function: Delete a book.  
   - Permissions: Only authenticated users can delete.  

---

### Permissions
- `IsAuthenticatedOrReadOnly`: Grants read-only access to unauthenticated users but restricts write operations to authenticated users.
- `IsAuthenticated`: Restricts access entirely to authenticated users for create, update, and delete actions.

---

### URL Routing
URLs are configured in `api/urls.py` and included in `advanced_api_project/urls.py` under the `/api/` prefix.
