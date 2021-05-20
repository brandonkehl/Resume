async function getVisitors(){
const response = await fetch('https://1xdilp5rt1.execute-api.us-east-1.amazonaws.com');
const data = await response.json();
const {visitorID} = data;

document.getElementById('visits').textContent = visitorID;
}