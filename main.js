function Voice(){
    var recognition = new webkitSpeechRecognition();
    recognition.lang = "en-IN";
    recognition.onresult = function(event) {
    var last = event.results.length - 1;
    var command = event.results[last][0].transcript;
    console.log(command)
    document.getElementById('TextSpeech').value = command
    // var res = command.includes("Python")
    // console.log(res)
    if(command.includes("Jai Shree Ram") || command.includes("Jay") || command.includes("Jai Shri Ram")) {
      window.location.href = "voice.html";
  }
}
recognition.start();
}
