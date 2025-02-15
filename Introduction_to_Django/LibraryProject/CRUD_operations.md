echo "# CRUD Operations in Django Shell" > CRUD_operations.md
echo "## 1. Create a Record" >> CRUD_operations.md
echo '```python' >> CRUD_operations.md
echo 'from bookshelf.models import Book' >> CRUD_operations.md
echo 'book = Book.objects.create(title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)' >> CRUD_operations.md
echo 'print("✅ Book created:", book)' >> CRUD_operations.md
echo '```' >> CRUD_operations.md

echo "## 2. Read Records" >> CRUD_operations.md
echo '```python' >> CRUD_operations.md
echo 'books = Book.objects.all()' >> CRUD_operations.md
echo 'print(books)' >> CRUD_operations.md
echo '```' >> CRUD_operations.md

echo "## 3. Update a Record" >> CRUD_operations.md
echo '```python' >> CRUD_operations.md
echo 'book = Book.objects.get(title="The Great Gatsby")' >> CRUD_operations.md
echo 'book.title = "The Great Gatsby - Revised"' >> CRUD_operations.md
echo 'book.save()' >> CRUD_operations.md
echo 'print("✅ Book title updated successfully!")' >> CRUD_operations.md
echo '```' >> CRUD_operations.md

echo "## 4. Delete a Record" >> CRUD_operations.md
echo '```python' >> CRUD_operations.md
echo 'book = Book.objects.get(title="The Great Gatsby - Revised")' >> CRUD_operations.md
echo 'book.delete()' >> CRUD_operations.md
echo 'print("✅ Book deleted successfully!")' >> CRUD_operations.md
echo '```' >> CRUD_operations.md

echo "## 5. Confirm Deletion" >> CRUD_operations.md
echo '```python' >> CRUD_operations.md
echo 'books = Book.objects.all()' >> CRUD_operations.md
echo 'print(books)' >> CRUD_operations.md
echo '```' >> CRUD_operations.md

echo "✅ CRUD operations saved in CRUD_operations.md"

