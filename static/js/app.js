var data = []
var token = ""

jQuery(document).ready(function () {

    $('#input_question').keyup(function (e) {
        if (e.which === 13) {
            $('#btn-process').click()
        }
    });

    $('#btn-process').on('click', function () {
        input_question = $('#input_question').val()

        $.ajax({
            url: '/question',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                "input_question": input_question
            }),
            beforeSend: function () {
                $('.overlay').show()
                $('#wiki_link').val('')
                $('#text_paragraphs').val('')
                $('#text_albert').val('')
            },
            complete: function () {
                $('.overlay').hide()
            }
        }).done(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $('#wiki_link').val(jsondata['link'])
            $('#text_paragraphs').val(jsondata['text_paragraphs'])
            $('#text_albert').val(jsondata['albert'])
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            alert(jsondata['responseText'])
        });
    })


})