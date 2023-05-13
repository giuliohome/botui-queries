var botui = new BotUI('my-botui-app');

const Question = () => {
    botui.action.text({
    action: {
      placeholder: 'Enter your query'
    }
  }).then(function(res) {
  botui.message.add({
    content: 'You asked ' + res.value + '!'
  });

    botui.action.button({
      action: [
        {
        text: 'ask more',
        cssClass: 'ask-btn'
      },
        {
        text: 'Restart',
        cssClass: 'restart-btn'
      }]
    }).then(function(res) {
      // Restart the chat when the button is clicked
      if (res.text === 'Restart') {
        location.reload();
      }
      botui.message.add({
    content: 'You selected ' + res.text + '!'
  }).then(() => {
     Question()
  });
    });

});
}


botui.message.add({
  content: 'Hello! What is your query?'
}).then(function() {


    Question();


});

