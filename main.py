from flask import render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from database import Books, db, app
from form import BooksForm, EditForm


Bootstrap(app)
app.secret_key = "dab54Ssdf5544S1DGaf35iul1b3fDGB"

@app.route('/')
def home():
    if request.args.get("id"):
        book_to_delete_id = request.args.get("id")
        book_to_delete = Books.query.get(book_to_delete_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for("home"))
    all_books = db.session.query(Books).all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BooksForm()
    if form.validate_on_submit():
        new_book = Books(
            title=form.book_title.data,
            author=form.book_author.data,
            rating=form.book_rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    edit_form = EditForm()
    book_to_update = Books.query.get(id)
    if edit_form.validate_on_submit():
        book_to_update.rating = edit_form.new_rating.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form, book_to_update=book_to_update)


if __name__ == "__main__":
    app.run(debug=True)

