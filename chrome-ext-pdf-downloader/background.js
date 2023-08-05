chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var url = tabs[0].url;
    console.log(url);
    document.getElementById("modal-title").innerHTML="Chrome extension";
  });