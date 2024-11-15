function addItem() {
    var title = $("#title").val();
    var author = $("#author").val();
    var rating = parseFloat($("#rating").val());
    var publisher = $("#publisher").val();
    var publishedDate = $("#publishedDate").val();
    var imageUrl = $("#imageUrl").val();
    var summary = $("#summary").val();
    var genre = $("#genre").val();

    if (title == "" || author == "" || isNaN(rating) || publisher == "" || publishedDate == "" || imageUrl == "" || summary == "" || genre == "") {
        alert("Please fill in all fields");
    } else {
        $.ajax({
            type: "POST",
            url: "addItem",
            dataType: "json",
            data: {
                "title": title,
                "author": author,
                "rating": rating,
                "publisher": publisher,
                "published_date": publishedDate,
                "image_url": imageUrl,
                "summary": summary,
                "genre": genre
            },
            success: function(data) {

                $("#successMessage").html('New item successfully created. <a href="/view/' + data.id + '">View it here</a>').show();
                $("#addItemForm")[0].reset();
                $("#title").focus();
            },
            error: function(jqXHR) {
                console.log("Error: " + jqXHR.status);
                $("#errorMessage").text("Error adding item. Please try again.").show();
            }
        });
    }
}




