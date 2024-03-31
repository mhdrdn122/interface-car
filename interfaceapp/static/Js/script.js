let isMouseDown = false;
var btnActive = ''
let btn = document.querySelectorAll('.btn')




setInterval(() => {
    if (isMouseDown) {
        SendReqoust(btnActive)        
    }
}, 100);




btn.forEach( item => {

    let  btnType = item.getAttribute("data-type")
item.addEventListener('mousedown', () => {
    isMouseDown = true;
    btnActive = btnType;

    });

    item.addEventListener('mouseup', () => {
        isMouseDown = false;
    });

    item.addEventListener('mouseleave', () => {
        isMouseDown = false;
    });

})

// fun fetching
const fetching = (Route) => {
    console.log(Route)

    fetch(`/${Route}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value: `${Route}` }) 
    })
    .then(response => {
        console.log(response);
    })
    .catch(error => {
        console.error('Error:', error);
    });
    
}




function SendReqoust(btnActive) {
    if (isMouseDown) {
        fetching(btnActive)
        setTimeout(fetching, 100);

    }
}


const ForWard_Led = () =>{
    fetching("ForWard_Led")
}
const BackWard_Led = () =>{
    fetching("backWard_Led")
}
const Power = () =>{
    fetching("Power")
}

// // set img screen start
// const videoElement = document.getElementById('camera-stream');

//         // Replace the IP address with your phone's IP address
//         const ipAddress = '192.168.137.21';
//         const streamURL = `http://${ipAddress}:8080/video`;

//         videoElement.src = streamURL;


setInterval(function() {
    document.getElementById('videoFeed').src = "http://192.168.137.21:8080/video?dummy=" + new Date().getTime() ;
    }, 1000);
// set img screen end