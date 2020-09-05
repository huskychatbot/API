app.post('/webhook', function(req,res) {
  console.log('Received a post request');
  if (!req.body) return res.sendStatus(400)
  res.setHeader('Content-Type', 'application/json');
  console.log('here is the post request from DialogFlow');
  console.log(req.body);
  console.log('God geo city parameter from DialogueFlow' + req.body.queryResult.parameters['geo-city']);
    var city = req.body.queryResult.parameters['geo-city'];
    var w = getWeather(city);
    let response = " ";
    let responseObj = {
        "fulfillmentText":responseObj
        ,"fulfillmentMessages":[{"text": {"text": [w]}}]
        ,"source":""
    }
    console.log('Here is the response to dialogflow');
    console.log(responseObj);
    return res.json(responseObj);
}

var apiKey = '88b029b2c8b1fc70a1a5f2cf57de2855'
var queryResult

function cb(err, response, body) {
  if(err) {
    console.log('error:', error);
  }
  var weather = JSON.parse(body)
  if (weather.message === 'city not found')
  {
    result = 'Unable to get weather ' + weather.message;
  }
  else {
    result = 'Right not its ' + weather.main.temp + 'degress with ' + weather.weather[0].description;
  }
}

function getWeather(city) {
  result = undefined;
  var url = 'https://home.openweathermap.org/data/2.5/weather?q=${city}&units=imperial&appid=${apiKey}';
  console.log(url);
  var req = request(url, cb);
  while(result === undefined) {
    require('deasync').runLoopOnce();
  }
  return result;
}
