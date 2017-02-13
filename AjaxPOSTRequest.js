function postData(input) {
    document.getElementById("info").innerHTML = "Analyzing Information, Please Stand By...";
    // send POST request using Ajax
    $.ajax({
        type: "POST",
        url: "/cgi-bin/test.py",
        data: input,
        success: callbackFunc
    })
}

function callbackFunc(response) {
    // do something with the response
    var info = response;
    console.log(response);
    console.log(typeof(response));
    document.getElementById("info").innerHTML = response;
}

// call function when click the button
$(document).ready(function(){
    $('#go').click(function(){
        postData($('#urlForm').val());
        $("#myModal").modal();
    });
});
