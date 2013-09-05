function loadJSONResults() {
    this._data = "?pastedJSON=" + encodeURIComponent(document.getElementById("copypasta").value);

    // POST to server the results of the escaped JSON payload
    jsonpayload = new XMLHttpRequest();
    jsonpayload.open("POST", this._data, true);
    jsonpayload.send();

    jsonpayload.onreadystatechange = function()
    {
        if (jsonpayload.readyState==4 && jsonpayload.status==200)
        {
            document.getElementById("returnedJSON").innerHTML=jsonpayload.responseText;
        }
    };
};

function retrieveFile() {
    break;
};

function switchJSONFields() {
    var JSONType = document.getElementById("selectJSON").selectedIndex;

    switch (JSONType) {
        case 0:
        document.getElementById("fileSelect").style.display = "none";
        document.getElementById("copypasta").style.display = "inline-block";
        break;
        case 1:
        document.getElementById("fileSelect").style.display = "block";
        document.getElementById("copypasta").style.display = "none";
        break
    }

};

// Deprecated fn().  Replacing semicolons and `&` is no longer necessary as the request is now properly
// encoded.  Will remove later.
// TODO:  Remove in next release (alpha).
function replaceAllSemicolons(find, replace, str) {
    return str.replace(new RegExp(find, 'g'), replace);
};