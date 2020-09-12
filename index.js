// See https://github.com/dialogflow/dialogflow-fulfillment-nodejs
// for Dialogflow fulfillment library docs, samples, and to report issues
'use strict';
const axios = require('axios'); 
 
const functions = require('firebase-functions');
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');
 
process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements
 
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
  
  function mutipleHandler(agent) {
    const currencyFrom = agent.parameters[`currencyFrom`];
    const currencyTo = agent.parameters.currencyTo;
   	const url = `https://api.exchangeratesapi.io/latest?base=${currencyFrom}`;
    
    //agent.add(url); //test parameter can send to variable url
  	return axios.get(url).then((response) => {
      console.log(response.data.base);
      console.log(response.data.rates[currencyTo]);
      const rate = response.data.rates[currencyTo].toFixed(2);
      
      let map = new Map();
      map.set('mapping', {'USD': 'mieyuan', 'CNY': 'renb', 'EUR': 'ouyuan', 'JPY': 'riyuan'});
      
      const resp = `今天 ${map.get('mapping').currencyFrom} 兑换 ${currencyTo} 的汇率是 ${rate}`;
      console.log(resp);
      agent.add(resp);
    });
  }
  
  let intentMap = new Map();
  intentMap.set('ExchangeRate', mutipleHandler);
  agent.handleRequest(intentMap);
});
