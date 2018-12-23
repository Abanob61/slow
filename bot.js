const Discord = require('discord.js');

const client = new Discord.Client();

 

client.on('ready', () => {

    console.log('I am ready!');
    client.user.setPresence({ status: 'online', game: { name: 'SlowBall' } })
});

 

client.on('message', message => {

    if (message.content === '!ping') {

       message.reply('pong');

       }

});
client.login("NTIzMTcwMzQ4Nzg3Njk1NjE4.DvVrYg.lVYzS0VyPWLlBE57GeceMEM6IZo");
