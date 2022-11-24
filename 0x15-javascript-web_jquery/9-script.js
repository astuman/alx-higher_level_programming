$(function () {  
    function getSalut () {
      return $.get({
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        dataType: 'json'
      });
    }
  
    getSalut().then((res) => {
        $('div#hello').text(res.hello);
    });
  });