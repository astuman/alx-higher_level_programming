$(function () {
    $('btn_translate').click(function () {
        $.get('https://www.fourtonfish.com/hellosalut/hello/' +
        $('#language_code').val(), function (data, textStatus ) {
        if (textStatus === 'success' && data.query.results !== null){
            $('#hello').text(data.query.results);
        } else {
            $('#hello').text('Invalid entry');
        }
    });
    });
});