// async function fetchData() {
//     const res = await fetch ("https://api.coronavirus.data.gov.uk/v1/data");
//     const record = await res.json();
// }

// // chrome.browserAction.onClicked.addListener(function(tab) {
// //     chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
// //       var url = tabs[0].url;
// //       console.log(url);
// //       // Here you should send `url` to your Python program.
// //       // You might need to setup a local server in Python to receive this url
// //     });
// // });

// fetchData();

// chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//     var url = tabs[0].url;
//     console.log(url);
// });

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var url = tabs[0].url;
    document.getElementById("modal-title").innerHTML="josue", url;
    
    fetch('http://localhost:5001/get_url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        url: url
      })
    }).then(response => response.json()) // handle response as JSON
      .then(data => {
        console.log(data);
        if (data.message === 'Success') {
          document.getElementById("modal-title").innerHTML="Downloaded";
        } else {
          document.getElementById("modal-title").innerHTML="Failed";
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        document.getElementById("modal-title").innerHTML="Bad";
      });    
  });