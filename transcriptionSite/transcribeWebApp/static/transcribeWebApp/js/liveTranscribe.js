window.onload=function(){
    var transcribe = document.getElementById("transcribe");
    var stopTranscribe = document.getElementById("stopTranscribe");


transcribe.addEventListener('click', startSpeechRecognition);




function startSpeechRecognition() {
    window.SpeechRecognition = window.webkitSpeechRecognition;
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition
        || window.mozSpeechRecognition || window.msSpeechRecognition)();


    recognition.continuous = true;
    recognition.interimResults = true;


    stopTranscribe.addEventListener('click', function() {
        recognition.stop();
    })

    
    recognition.onstart = function() {


        console.log("microphone started")
    }


    recognition.addEventListener('result', e=>{
        const transcript = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)

        document.getElementById('transcript').value = transcript
    })

    // recognition.onresult = function(event){
    //     var text = event.results[0][0].transcript;
    //     document.getElementById('transcript').value = text;
    // };

    recognition.start();
    
}
  }




