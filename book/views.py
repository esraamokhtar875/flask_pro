
from app.model import Book, db
from flask import render_template, request, redirect, url_for
import os
from app.book import books_blueprint
from werkzeug.utils import secure_filename
from app.book.forms import BookForm


@books_blueprint.route("/index" , endpoint='index')
def index():
    books=Book.query.all()
    return render_template("books/index.html", books=books)



@books_blueprint.route("/books/<int:id>", endpoint="show")
def show(id):
    book=Book.query.get_or_404(id)
    return render_template("books/show_book.html", book=book)



@books_blueprint.route("form/create", endpoint='form_create', methods=['GET','POST'])
def create_book():
    form = BookForm()
    if request.method == 'POST':
        if form.validate_on_submit():
           print(request.form)
           image = form.cover_photo.data
           image_name= secure_filename(image.filename)
           image.save (os.path.join('static/books/images/', image_name))
           print(image)
           book = Book(title=request.form['title'],
                    cover_photo=image_name,
                    description=request.form['description'],
                    pages = request.form ['pages']
           )
           db.session.add(book)
           db.session.commit()
           return redirect(url_for('books.index'))
    return render_template("books/create_book.html", form=form )


@books_blueprint.route('/book/<int:id>/edit', endpoint='form_edit', methods=['GET', 'POST'])
def edit_book(id):

    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if request.method == 'POST':

        if form.validate_on_submit():
            image = form.cover_photo.data
            image_name = secure_filename(image.filename)
            image.save(os.path.join('static/books/images/', image_name))
            print(image)
            book.title = form.title.data
            book.cover_photo = image_name
            book.pages = form.pages.data
            book.description = form.description.data
            db.session.commit()
            return redirect(url_for('books.show', id=book.id))
    return render_template('books/edit_book.html', form=form)

@books_blueprint.route("/Delete/<int:id>", endpoint="delete",methods=['POST'])
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books.index"))
