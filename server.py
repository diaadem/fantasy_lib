from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import uuid
from datetime import datetime, date
import re
app = Flask(__name__)

data = {
    "1": {
        "id": "1",
        "title": "Mistborn",
        "author": "Brandon Sanderson",
        "rating": 4.48,
        "publisher": "Tor Books",
        "published date": "2006-07-17",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1617768316i/68428.jpg",
        "summary": "For a thousand years the ash fell and no flowers bloomed. For a thousand years the Skaa slaved in misery and lived in fear. For a thousand years the Lord Ruler, the Sliver of Infinity, reigned with absolute power and ultimate terror, divinely invincible. Then, when hope was so long lost that not even its memory remained, a terribly scarred, heart-broken half-Skaa rediscovered it in the depths of the Lord Rulers most hellish prison. Kelsier snapped and found in himself the powers of a Mistborn. A brilliant thief and natural leader, he turned his talents to the ultimate caper, with the Lord Ruler himself as the mark. Kelsier recruited the underworlds elite, the smartest and most trustworthy allomancers, each of whom shares one of his many powers, and all of whom relish a high-stakes challenge. Then Kelsier reveals his ultimate dream, not just the greatest heist in history, but the downfall of the divine despot. But even with the best criminal crew ever assembled, Kels plan looks more like the ultimate long shot, until luck brings a ragged girl named Vin into his life. Like him, shes a half-Skaa orphan, but shes lived a much harsher life. Vin has learned to expect betrayal from everyone she meets. She will have to learn trust if Kel is to help her master powers of which she never dreamed.",
        "genre": ["High Fantasy","Epic Fantasy", "Adult", "Magic", "Sci-Fi", "Young Adult", "Adventure"],
    },
        "2": {
        "id": "2",
        "title": "A Game of Thrones",
        "author": "George R.R. Martin",
        "rating": 4.44,
        "publisher": "Bantam",
        "published date": "1996-08-06",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1555398485i/45152283.jpg",
        "summary": "Long ago, in a time forgotten, a preternatural event threw the seasons out of balance. In a land where summers can last decades and winters a lifetime, trouble is brewing. The cold is returning, and in the frozen wastes to the north of Winterfell, sinister forces are massing beyond the kingdom’s protective Wall. To the south, the king’s powers are failing—his most trusted adviser dead under mysterious circumstances and his enemies emerging from the shadows of the throne. At the center of the conflict lie the Starks of Winterfell, a family as harsh and unyielding as the frozen land they were born to. Now Lord Eddard Stark is reluctantly summoned to serve as the king’s new Hand, an appointment that threatens to sunder not only his family but the kingdom itself. Sweeping from a harsh land of cold to a summertime kingdom of epicurean plenty, A Game of Thrones tells a tale of lords and ladies, soldiers and sorcerers, assassins and bastards, who come together in a time of grim omens. Here an enigmatic band of warriors bear swords of no human metal; a tribe of fierce wildlings carry men off into madness; a cruel young dragon prince barters his sister to win back his throne; a child is lost in the twilight between life and death; and a determined woman undertakes a treacherous journey to protect all she holds dear. Amid plots and counter-plots, tragedy and betrayal, victory and terror, allies and enemies, the fate of the Starks hangs perilously in the balance, as each side endeavors to win that deadliest of conflicts: the game of thrones.",
        "genre": ["High Fantasy", "Epic Fantasy", "Adult", "Adventure"]
    },
        "3": {
        "id": "3",
        "title": "The Name of the Wind",
        "author": "Patrick Rothfuss",
        "rating": 4.42,
        "publisher": "Penguin Group DAW",
        "published date": "2007-03-27",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1472068132i/2913377._SX300_.jpg",
        "summary": "Told in Kvothe's own voice, this is the tale of the magically gifted young man who grows to be the most notorious wizard his world has ever seen. The intimate narrative of his childhood in a troupe of traveling players, his years spent as a near-feral orphan in a crime-ridden city, his daringly brazen yet successful bid to enter a legendary school of magic, and his life as a fugitive after the murder of a king form a gripping coming-of-age story unrivaled in recent literature. A high-action story written with a poet's hand, The Name of the Wind is a masterpiece that will transport readers into the body and mind of a wizard.",
        "genre": ["High Fantasy", "Epic Fantasy", "Adult", "Magic", "Sci-Fi", "Young Adult", "Adventure"]
    },
        "4": {
        "id": "4",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "rating": 4.29,
        "publisher": "Houghton Mifflin",
        "published date": "1937-09-21",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1519739410i/38819529.jpg",
        "summary": "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort. Written for J.R.R. Tolkien’s own children, The Hobbit met with instant critical acclaim when it was first published in 1937. Now recognized as a timeless classic, this introduction to the hobbit Bilbo Baggins, the wizard Gandalf, Gollum, and the spectacular world of Middle-earth recounts of the adventures of a reluctant hero, a powerful and dangerous ring, and the cruel dragon Smaug the Magnificent. The text in this 372-page paperback edition is based on that first published in Great Britain by Collins Modern Classics (1998), and includes a note on the text by Douglas A. Anderson (2001).",
        "genre": ["Epic Fantasy"," Adventure", "Classic", "High Fantasy", "Magic", "Middle Grade", "Young Adult"]
    },
        "5": {
        "id": "5",
        "title": "Fourth Wing",
        "author": "Rebecca Yarros",
        "rating": 4.60,
        "publisher": "Entangled: Red Tower Books",
        "published date": "2023-05-02",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1701980900i/61431922.jpg",
        "summary": "Twenty-year-old Violet Sorrengail was supposed to enter the Scribe Quadrant, living a quiet life among books and history. Now, the commanding general—also known as her tough-as-talons mother—has ordered Violet to join the hundreds of candidates striving to become the elite of Navarre: dragon riders.But when you’re smaller than everyone else and your body is brittle, death is only a heartbeat away...because dragons don’t bond to “fragile” humans. They incinerate them. With fewer dragons willing to bond than cadets, most would kill Violet to better their own chances of success. The rest would kill her just for being her mother’s daughter—like Xaden Riorson, the most powerful and ruthless wingleader in the Riders Quadrant. She’ll need every edge her wits can give her just to see the next sunrise. Yet, with every day that passes, the war outside grows more deadly, the kingdom's protective wards are failing, and the death toll continues to rise. Even worse, Violet begins to suspect leadership is hiding a terrible secret. Friends, enemies, lovers. Everyone at Basgiath War College has an agenda—because once you enter, there are only two ways out: graduate or die",
        "genre": ["High Fantasy", "Magic", "Romance", "Adult", "Magic"]
    },
        "6": {
        "id": "6",
        "title": "The Way of Kings",
        "author": "Brandon Sanderson",
        "rating": 4.66,
        "publisher": "Tor Books",
        "published date": "2010-08-31",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1659905828i/7235533.jpg",
        "summary": "Roshar is a world of stone and storms. Uncanny tempests of incredible power sweep across the rocky terrain so frequently that they have shaped ecology and civilization alike. Animals hide in shells, trees pull in branches, and grass retracts into the soilless ground. Cities are built only where the topography offers shelter. It has been centuries since the fall of the ten consecrated orders known as the Knights Radiant, but their Shardblades and Shardplate remain: mystical swords and suits of armor that transform ordinary men into near-invincible warriors. Men trade kingdoms for Shardblades. Wars were fought for them, and won by them. One such war rages on a ruined landscape called the Shattered Plains. There, Kaladin, who traded his medical apprenticeship for a spear to protect his little brother, has been reduced to slavery. In a war that makes no sense, where ten armies fight separately against a single foe, he struggles to save his men and to fathom the leaders who consider them expendable. Brightlord Dalinar Kholin commands one of those other armies. Like his brother, the late king, he is fascinated by an ancient text called The Way of Kings. Troubled by over-powering visions of ancient times and the Knights Radiant, he has begun to doubt his own sanity. Across the ocean, an untried young woman named Shallan seeks to train under an eminent scholar and notorious heretic, Dalinar's niece, Jasnah. Though she genuinely loves learning, Shallan's motives are less than pure. As she plans a daring theft, her research for Jasnah hints at secrets of the Knights Radiant and the true cause of the war. The result of over ten years of planning, writing, and world-building, The Way of Kings is but the opening movement of the Stormlight Archive, a bold masterpiece in the making.",
        "genre": [ "High Fantasy", "Epic Fantasy", "Adult", "Magic", "Sci-Fi", "Young Adult", "Adventure"]
    },
        "7": {
        "id": "7",
        "title": "The Lion, the Witch and the Wardrobe",
        "author": "C.S. Lewis",
        "rating": 4.23,
        "publisher": "HarperCollins Publishers",
        "published date": "1950-10-16",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1353029077i/100915.jpg",
        "summary": "Narnia… the land beyond the wardrobe door, a secret place frozen in eternal winter, a magical country waiting to be set free. Lucy is the first to find the secret of the wardrobe in the professor's mysterious old house. At first her brothers and sister don't believe her when she tells of her visit to the land of Narnia. But soon Edmund, then Peter and Susan step through the wardrobe themselves. In Narnia they find a country buried under the evil enchantment of the White Witch. When they meet the Lion Aslan, they realize they've been called to a great adventure and bravely join the battle to free Narnia from the Witch's sinister spell.",
        "genre": ["Low Fantasy", "Epic Fantasy", "Middle Grade","Adventure", "Magic", "Young Adult"]
    },
        "8": {
        "id": "8",
        "title": "The Sword of Kaigen",
        "author": "M.L. Wang",
        "rating": 4.47,
        "publisher": "Amazon Digital Services",
        "published date": "2018-01-01",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1702907961i/41886271.jpg",
        "summary": "A mother struggling to repress her violent past. A son struggling to grasp his violent future, A father blind to the danger that threatens them all. When the winds of war reach their peninsula, will the Matsuda family have the strength to defend their empire? Or will they tear each other apart before the true enemies even reach their shores? High on a mountainside at the edge of the Kaigenese Empire live the most powerful warriors in the world, superhumans capable of raising the sea and wielding blades of ice. For hundreds of years, the fighters of the Kusanagi Peninsula have held the Empire’s enemies at bay, earning their frozen spit of land the name ‘The Sword of Kaigen.’ Born into Kusanagi’s legendary Matsuda family, fourteen-year-old Mamoru has always known his purpose: to master his family’s fighting techniques and defend his homeland. But when an outsider arrives and pulls back the curtain on Kaigen’s alleged age of peace, Mamoru realizes that he might not have much time to become the fighter he was bred to be. Worse, the empire he was bred to defend may stand on a foundation of lies. Misaki told herself that she left the passions of her youth behind when she married into the Matsuda house. Determined to be a good housewife and mother, she hid away her sword, along with everything from her days as a fighter in a faraway country. But with her growing son asking questions about the outside world, the threat of an impending invasion looming across the sea, and her frigid husband grating on her nerves, Misaki finds the fighter in her clawing its way back to the surface.",
        "genre": ["High Fantasy", "Epic Fantasy", "Adult", "Magic", "Sci-Fi", "Young Adult", "Adventure"]
    },
        "9": {
        "id": "9",
        "title": "The Night Circus",
        "author": "Erin Morgenstern",
        "rating": 4.02,
        "publisher": "Doubleday",
        "published date": "2011-09-13",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1387124618i/9361589.jpg",
        "summary": "The circus arrives without warning. No announcements precede it. It is simply there, when yesterday it was not. Within the black-and-white striped canvas tents is an utterly unique experience full of breathtaking amazements. It is called Le Cirque des Rêves, and it is only open at night. But behind the scenes, a fierce competition is underway—a duel between two young magicians, Celia and Marco, who have been trained since childhood expressly for this purpose by their mercurial instructors. Unbeknownst to them, this is a game in which only one can be left standing, and the circus is but the stage for a remarkable battle of imagination and will. Despite themselves, however, Celia and Marco tumble headfirst into love—a deep, magical love that makes the lights flicker and the room grow warm whenever they so much as brush hands. True love or not, the game must play out, and the fates of everyone involved, from the cast of extraordinary circus performers to the patrons, hang in the balance, suspended as precariously as the daring acrobats overhead. Written in rich, seductive prose, this spell-casting novel is a feast for the senses and the heart.",
        "genre": ["Low Fantasy","Historical Fiction", "Romance","Magic", "Adult", "Young Adult"]
    },
        "10": {
        "id": "10",
        "title": "Six of Crows",
        "author": "Leigh Bardugo",
        "rating": 4.49,
        "publisher": "Henry Holt & Company",
        "published date": "2015-09-29",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1651710803i/23437156.jpg",
        "summary": "Ketterdam: a bustling hub of international trade where anything can be had for the right price—and no one knows that better than criminal prodigy Kaz Brekker. Kaz is offered a chance at a deadly heist that could make him rich beyond his wildest dreams. But he can’t pull it off alone. . . . A convict with a thirst for revenge. A sharpshooter who can’t walk away from a wager. A runaway with a privileged past. A spy known as the Wraith. A Heartrender using her magic to survive the slums. A thief with a gift for unlikely escapes. Six dangerous outcasts. One impossible heist. Kaz’s crew is the only thing that might stand between the world and destruction—if they don’t kill each other first.",
        "genre": ["Romance", "Magic", "LGBTQ", "Young Adult", "High Fantasy", "Adventure"]
    }
}



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def homepage():
    sorted_items = sorted(data.values(), key=lambda x: x['rating'], reverse=True)
    popular_data = sorted_items[:4]
    return render_template('index.html', popular_data=popular_data)

@app.route('/view/<id>')
def view_data(id):
    item_data = data.get(id)
    if item_data:
        success_message = request.args.get('success_message', None)
        return render_template('view_item.html', item=item_data, success_message=success_message)
    else:
        return redirect(url_for('page_not_found'))
        

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()

    if not query:
        return render_template('search_results.html', search_results=[], search_term="")

    search_results = [item for item in data.values() if query.lower() in item['title'].lower() or query.lower() in item['author'].lower() or any(query.lower() in genre.lower() for genre in item['genre'])]

    return render_template('search_results.html', search_results=search_results, query=query)


#@app.route('/search', methods=['GET'])
#def search():
#    search_term = request.args.get('search_term', '').strip()  # Use 'search_term' instead of 'query'
#
#    if not search_term:
#        return render_template('search_results.html', search_results=[], search_term=search_term)
#
#    search_results = [item for item in data.values() if search_term.lower() in item['title'].lower() or search_term.lower() in item['author'].lower() or any(search_term.lower() in genre.lower() for genre in item['genre'])]
#
#    return render_template('search_results.html', search_results=search_results, search_term=search_term)



#@app.route('/add', methods=['GET', 'POST'])
#def add_data():
#    if request.method == 'POST':
#        try:
#            title = request.form.get('title')
#            author = request.form.get('author')
#            rating = float(request.form.get('rating'))
#            publisher = request.form.get('publisher')
#            published_date = request.form.get('published_date')
#            image_url = request.form.get('image_url')
#            summary = request.form.get('summary')
#            genre = request.form.get('genre')
#
#            if not all([title, author, rating, publisher, published_date, image_url, summary, genre]):
#                return "Error: Missing required fields", 400
#
#            new_id = str(uuid.uuid4())
#
#            data[new_id] = {
#                "id": new_id,
#                "title": title,
#                "author": author,
#                "rating": rating,
#                "publisher": publisher,
#                "published date": published_date,
#                "image": image_url,
#                "summary": summary,
#                "genre": genre.split(',')
#            }
#
#            # Set success message
#            success_message = "Book added successfully."
#
#            # Redirect to the view page of the newly added item
#            return redirect(url_for('add_item', success_message=success_message))
#
#        except Exception as e:
#            print(f"Error adding book: {str(e)}")
#            return jsonify({"status": "error"})
#
#    # If the request method is GET, render the add_item.html template with an empty success message
#    return render_template('add_item.html')

#@app.route('/add', methods=['GET', 'POST'])
#def add_data():
#    if request.method == 'POST':
#        title = request.form.get('title')
#        author = request.form.get('author')
#        rating = float(request.form.get('rating'))
#        publisher = request.form.get('publisher')
#        published_date = request.form.get('published_date')
#        image_url = request.form.get('image_url')
#        summary = request.form.get('summary')
#        genre = request.form.get('genre')
#
#        if not all([title, author, rating, publisher, published_date, image_url, summary, genre]):
#            return "Error: Missing required fields", 400
#
#        new_id = str(uuid.uuid4())
#
#        data[new_id] = {
#            "id": new_id,
#            "title": title,
#            "author": author,
#            "rating": rating,
#            "publisher": publisher,
#            "published date": published_date,
#            "image": image_url,
#            "summary": summary,
#            "genre": genre.split(',')
#        }
#
#        return redirect(url_for('add_success', id=new_id))
#    else:
#        return render_template('add_item.html', success_message="")
#
#@app.route('/add_success/<id>')
#def add_success(id):
#    item = data.get(id)
#    if item:
#        success_message = "Book added successfully."
#        return render_template('add_item.html', success_message=success_message, item=item)
#    else:
#        return redirect(url_for('page_not_found'))
@app.route('/all_books', methods=['GET'])
def all_books():
    all_books = list(data.values())
    return render_template('search_results.html', search_results=all_books, query="All Books")

@app.route('/add', methods=['GET'])
def add_data_get():
    return render_template('add_item.html')

@app.route('/add', methods=['POST'])
def add_data_post():
    try:
        title = request.form.get('title')
        author = request.form.get('author')
        rating = float(request.form.get('rating'))
        publisher = request.form.get('publisher')
        published_date = request.form.get('published_date')
        image_url = request.form.get('image_url')
        summary = request.form.get('summary')
        genre = request.form.get('genre')

        if not all([title, author, rating, publisher, published_date, image_url, summary, genre]):
            return jsonify({'success': False, 'error': 'Missing required fields'})

        new_id = str(uuid.uuid4())
        
#        published_date = datetime.strptime(published_date, '%Y-%m-%d').date()
#
#        if published_date > date.today():
#            return jsonify({'success': False, 'error': 'Publication date cannot be in the future.'})


        data[new_id] = {
            "id": new_id,
            "title": title,
            "author": author,
            "rating": rating,
            "publisher": publisher,
            "published date": published_date,
            "image": image_url,
            "summary": summary,
            "genre": genre.split(',')
        }

        return jsonify({'success': True, 'id': new_id})
    except Exception as e:
        print(f"Error adding book: {str(e)}")
        return jsonify({'success': False, 'error': 'Error adding book'})

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_data(id):
    item_data = data.get(id)

    if not item_data:
        return redirect(url_for('page_not_found'))

    if request.method == 'POST':
        try:
            title = request.form.get('title')
            author = request.form.get('author')
            rating = float(request.form.get('rating'))
            publisher = request.form.get('publisher')
            published_date = request.form.get('published_date')
            published_date = datetime.strptime(published_date, '%Y-%m-%d').date()

            if published_date > date.today():
                error_message = 'Publication date cannot be in the future.'
                return render_template('edit_item.html', item=item_data, error_message=error_message, max_date=date.today().isoformat())

            image_url = request.form.get('image_url')
            summary = request.form.get('summary')
            genre = request.form.get('genre')

            if not all([title, author, rating, publisher, published_date, image_url, summary, genre]):
                return "Error: Missing required fields", 400

            item_data['title'] = title
            item_data['author'] = author
            item_data['rating'] = rating
            item_data['publisher'] = publisher
            item_data['published date'] = published_date
            item_data['image'] = image_url
            item_data['summary'] = summary
            item_data['genre'] = [genre.strip() for genre in genre.split(',')]

            return redirect(url_for('view_data', id=id, success_message='Book updated successfully'))
        except Exception as e:
            print(f"Error updating book: {str(e)}")
            return render_template('edit_item.html', error_message='Error updating book')
    else:
        max_date = date.today().isoformat()
        return render_template('edit_item.html', item=item_data, max_date=max_date)

if __name__ == '__main__':
    app.run(debug=True)
